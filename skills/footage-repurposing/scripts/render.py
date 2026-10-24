#!/usr/bin/env python3
"""Edit reviewed filmed stock; never generate scene footage or substitute reference films."""
import argparse, hashlib, json, math, subprocess, tempfile
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
FONT='/System/Library/Fonts/Supplemental/Arial.ttf'
BOLD='/System/Library/Fonts/Supplemental/Arial Bold.ttf'
def digest(path):
    with Path(path).open("rb") as f:return hashlib.file_digest(f,"sha256").hexdigest()
def probe(path):
    return json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(path)]))
def font(size,bold=False): return ImageFont.truetype(BOLD if bold else FONT,size)
def overlay(scene,w,h,index,total,presentation=None,layer='all'):
    cfg=presentation or {};v=h>w
    safe=cfg.get('safe_area',[.08,.12,.82,.80] if v else [.075,.08,.925,.92])
    if len(safe)!=4 or not all(math.isfinite(x) for x in safe) or not (0<=safe[0]<safe[2]<=1 and 0<=safe[1]<safe[3]<=1):raise ValueError('Invalid safe area')
    left,top,right,bottom=[round(n*(w if i%2==0 else h)) for i,n in enumerate(safe)]
    im=Image.new('RGBA',(w,h));d=ImageDraw.Draw(im);unit=w/1080 if v else h/1080
    regular=cfg.get('font',FONT);bold=cfg.get('bold_font',BOLD)
    def draw_lines(value,x,y,size,b=False,limit=None):
        f=ImageFont.truetype(bold if b else regular,round(size*unit));limit=bottom if limit is None else limit
        for line in value.split('\n'):
            box=d.textbbox((x,y),line,font=f)
            if box[2]>right:raise ValueError('Text overflow: '+line)
            if box[3]>limit or box[1]<top:raise ValueError('Vertical text overflow or reserved UI overlap: '+line)
            d.text((x,y),line,font=f,fill='#fff7e9',stroke_width=1,stroke_fill='#222222')
            y+=round(size*unit*1.23)
        return y
    notice=scene.get('disclosure',cfg.get('disclosure','ILLUSTRATIVE STOCK · CONCEPT'))
    notice_y=bottom-round((notice.count('\n')+1)*27*unit)
    if layer in ('all','message'):
        y=round(h*scene.get('text_y',cfg.get('text_y',.52 if v else .60)))
        if y<top+round(50*unit):raise ValueError('Text overlaps brand or top UI reserve')
        for yy in range(max(top,y-20),bottom):
            d.line((left-10,yy,right+10,yy),fill=(0,0,0,95))
        y=draw_lines(scene.get('title',''),left,y,cfg.get('title_size',60),True,notice_y-16)
        y+=round(14*unit)
        draw_lines(scene.get('caption',''),left,y,cfg.get('caption_size',30),False,notice_y-16)
    if layer in ('all','base'):
        draw_lines(cfg.get('brand',''),left,top,24,True)
        draw_lines(notice,left,notice_y,22)
    return im

def validate(plan,root):
    root=Path(root).resolve();w,h=plan['size']
    if any(not isinstance(n,int) or n<2 or n%2 for n in (w,h)):raise ValueError('Even positive dimensions required')
    manifest=(root/plan['manifest']).resolve()
    if not manifest.is_relative_to(root):raise ValueError('Manifest outside workspace')
    assets={a['local_path']:a for a in json.loads(manifest.read_text())['assets']}
    if not plan.get('scenes'):raise ValueError('No shots')
    checked={}
    for s in plan['scenes']:
        if s.get('kind')!='filmed_stock':raise ValueError('Only filmed_stock scenes accepted')
        src=(root/s['source']).resolve();a=assets.get(s['source'],{})
        if not src.is_relative_to(root) or not src.is_file():raise ValueError('Source unavailable or outside workspace')
        if a.get('usage')!='production' or a.get('decision')!='selected' or a.get('origin')!='filmed_stock':raise ValueError('Source not cleared filmed production stock')
        if not all(a.get(k) for k in ['source_url','license_url','creator','inspection','sha256']):raise ValueError('Source evidence incomplete')
        if src not in checked:
            if digest(src)!=a['sha256']:raise ValueError('Source hash changed')
            checked[src]=float(probe(src)['format']['duration'])
        start=float(s.get('start',0));duration=float(s['duration'])
        if not math.isfinite(start+duration) or start<0 or not 0<duration<=30 or start+duration>checked[src]+.02:raise ValueError('Trim outside source bounds')
        if not 0<=s.get('crop_x',.5)<=1:raise ValueError('crop_x must be 0–1')
        window=s.get('text_window',[0,duration])
        if len(window)!=2 or not all(math.isfinite(x) for x in window) or not 0<=window[0]<window[1]<=duration:raise ValueError('Invalid text window')
        overlay(s,w,h,0,len(plan['scenes']),plan.get('presentation'))
    return checked

def render(plan,out,root=None):
    out=Path(out);root=Path.cwd() if root is None else Path(root)
    if out.exists():raise ValueError('Output exists; choose a new filename')
    validate(plan,root);w,h=plan['size'];fps=24
    out.parent.mkdir(parents=True,exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='soban-edit-') as td:
        tmp=Path(td);parts=[]
        for i,s in enumerate(plan['scenes']):
            layer=tmp/f'{i}.png';base=tmp/f'{i}-base.png'
            overlay(s,w,h,i,len(plan['scenes']),plan.get('presentation'),'message').save(layer)
            overlay(s,w,h,i,len(plan['scenes']),plan.get('presentation'),'base').save(base)
            a,b=s.get('text_window',[0,s['duration']])
            part=tmp/f'{i}.mp4';parts.append(part)
            # Scale/reframe actual footage; preserve motion and speed. No generated backgrounds.
            vf=f"[0:v]setpts=PTS-STARTPTS,scale={w}:{h}:force_original_aspect_ratio=increase,crop={w}:{h}:(iw-ow)*{s.get('crop_x',.5)}:(ih-oh)/2,setsar=1,fps={fps}[v];[v][2:v]overlay=0:0:shortest=1[base];[base][1:v]overlay=0:0:shortest=1:enable='between(t,{a},{b})'[out]"
            subprocess.run(['ffmpeg','-v','error','-ss',str(s['start']),'-i',str(root/s['source']),'-loop','1','-i',str(layer),'-loop','1','-i',str(base),'-filter_complex',vf,'-map','[out]','-t',str(s['duration']),'-an','-c:v','libx264','-preset','veryfast','-crf','20','-pix_fmt','yuv420p',str(part)],check=True)
            print(f'Edited {i+1}/{len(plan["scenes"])}',flush=True)
        listing=tmp/'concat.txt';listing.write_text(''.join(f"file '{p}'\n" for p in parts))
        subprocess.run(['ffmpeg','-v','error','-n','-f','concat','-safe','0','-i',str(listing),'-c','copy','-movflags','+faststart',str(out)],check=True)
    info=probe(out);v=next(x for x in info['streams'] if x['codec_type']=='video');expected=sum(s['duration'] for s in plan['scenes'])
    if (v['width'],v['height'])!=(w,h) or abs(float(info['format']['duration'])-expected)>.1:raise RuntimeError('Output dimensions/duration mismatch')
    subprocess.run(['ffmpeg','-v','error','-i',str(out),'-f','null','-'],check=True)
    out.with_suffix('.verification.json').write_text(json.dumps({'size':[w,h],'duration':float(info['format']['duration']),'full_decode':'pass','background':'reviewed filmed stock only','audio':'silent edit draft; no music license assumed','sha256':digest(out)},indent=2))
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('plan',type=Path);p.add_argument('output',type=Path);p.add_argument('--root',type=Path,default=Path.cwd());a=p.parse_args();render(json.loads(a.plan.read_text()),a.output,a.root)
