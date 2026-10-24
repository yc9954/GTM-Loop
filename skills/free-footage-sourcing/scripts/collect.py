#!/usr/bin/env python3
"""Download explicitly reviewed Pexels assets. Default is a no-network plan."""
import argparse, hashlib, json, subprocess, urllib.request, urllib.parse
from pathlib import Path

def collect(manifest,root,download=False):
    for a in manifest['assets']:
        if a['decision']!='selected': continue
        url=a['download_url']; u=urllib.parse.urlparse(url)
        if u.scheme!='https' or u.hostname!='www.pexels.com' or not u.path.startswith('/download/video/'):
            raise ValueError('Use the download link inspected on the original Pexels page')
        if not a.get('source_url') or not a.get('license_url') or not a.get('reviewed_at'):
            raise ValueError('Missing source/license review evidence')
        dest=(root/a['local_path']).resolve()
        if not dest.is_relative_to(root.resolve()): raise ValueError('Destination escapes workspace')
        if dest.exists():
            digest=hashlib.sha256(dest.read_bytes()).hexdigest()
            if a.get('sha256') and digest!=a['sha256']: raise ValueError('Existing source hash mismatch')
            print('Verified existing:',a['id']);continue
        print('Download' if download else 'Planned:',a['id'],a['source_url'])
        if not download:continue
        dest.parent.mkdir(parents=True,exist_ok=True)
        # Exclusive create: never replace a user file. Partial downloads remain explicit.
        partial=dest.with_suffix(dest.suffix+'.partial')
        with urllib.request.urlopen(url,timeout=30) as response, partial.open('xb') as out:
            size=0
            while chunk:=response.read(1024*1024):
                size+=len(chunk)
                if size>300*1024*1024:raise ValueError('Asset exceeds 300 MiB limit')
                out.write(chunk)
        subprocess.run(['ffprobe','-v','error',str(partial)],check=True)
        digest=hashlib.sha256(partial.read_bytes()).hexdigest()
        if a.get('sha256') and digest!=a['sha256']:raise ValueError('Downloaded bytes differ; review before reuse')
        # Hard link creates destination exclusively, then remove only our temporary link.
        import os
        os.link(partial,dest);partial.unlink()
        print('Saved:',dest,'sha256:',digest)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('manifest',type=Path);p.add_argument('--root',type=Path,default=Path.cwd());p.add_argument('--download',action='store_true');args=p.parse_args()
    collect(json.loads(args.manifest.read_text()),args.root,args.download)
