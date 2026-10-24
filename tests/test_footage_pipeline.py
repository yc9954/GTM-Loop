import copy,importlib.util,json,unittest
from pathlib import Path
from unittest.mock import patch
ROOT=Path(__file__).resolve().parents[1]
def load(name,path):
 s=importlib.util.spec_from_file_location(name,ROOT/path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
collect=load('collect','skills/free-footage-sourcing/scripts/collect.py')
render=load('render','skills/footage-repurposing/scripts/render.py')
class PipelineTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.plan=json.loads((ROOT/'docs/seoul-short.json').read_text())
 @unittest.skipUnless((ROOT/"assets/source/pexels-30975008.mp4").exists(),"Download reviewed source media before integration checks")
 def test_plans_and_source_bounds(self):
  for name in ['short','wide','explainer']:render.validate(json.loads((ROOT/f'docs/seoul-{name}.json').read_text()),ROOT)
 def test_food_is_not_presented_as_actual_menu(self):
  p=json.loads((ROOT/"docs/seoul-explainer.json").read_text())
  food=[s for s in p["scenes"] if "17598915" in s["source"]]
  self.assertEqual(len(food),2)
  for s in food:self.assertIn("NOT OUR MENU OR VENUE",s["disclosure"])
 def test_procedural_scene_rejected(self):
  p=copy.deepcopy(self.plan);p['scenes'][0]['kind']='projection'
  with self.assertRaisesRegex(ValueError,'Only filmed_stock'):render.validate(p,ROOT)
 def test_unlisted_reference_rejected(self):
  manifest=json.loads((ROOT/self.plan['manifest']).read_text())
  manifest['assets'][0]['usage']='reference_only'
  manifest['assets'][0]['local_path']='README.md'
  plan=copy.deepcopy(self.plan);plan['scenes'][0]['source']='README.md'
  with patch.object(render.json,'loads',return_value=manifest):
   with self.assertRaisesRegex(ValueError,'not cleared'):render.validate(plan,ROOT)
 @unittest.skipUnless((ROOT/"assets/source/pexels-30975008.mp4").exists(),"Download reviewed source media before integration checks")
 def test_trim_past_end_rejected(self):
  p=copy.deepcopy(self.plan);p['scenes'][0]['start']=999
  with self.assertRaisesRegex(ValueError,'Trim outside'):render.validate(p,ROOT)
 def test_text_overflow_rejected(self):
  s=copy.deepcopy(self.plan['scenes'][0]);s['title']='W'*100
  with self.assertRaisesRegex(ValueError,'overflow'):render.overlay(s,1080,1920,0,1)
 def test_untrusted_download_host_rejected(self):
  with self.assertRaises(ValueError):collect.collect({'assets':[{'id':'x','decision':'selected','download_url':'https://example.org/download/video/1'}]},ROOT)
 def test_file_is_not_overwritten(self):
  with self.assertRaises(ValueError):render.render({'size':[1080,1920]},ROOT/'README.md')

class LayoutTests(unittest.TestCase):
 def test_vertical_overflow_rejected(self):
  s={'title':'Hello','caption':'Line\n'*30}
  with self.assertRaisesRegex(ValueError,'Vertical text overflow'):render.overlay(s,1080,1920,0,1)
 def test_right_ui_reserve_rejected(self):
  with self.assertRaisesRegex(ValueError,'overflow'):render.overlay({'title':'W'*14},1080,1920,0,1,{'safe_area':[.08,.12,.50,.80]})
 def test_brand_is_input(self):
  im=render.overlay({'title':'A new table','caption':'A new experience'},1080,1920,0,1,{'brand':'ANOTHER BRAND'})
  self.assertEqual(im.size,(1080,1920))
 @unittest.skipUnless((ROOT/"assets/source/pexels-30975008.mp4").exists(),"Download reviewed source media before integration checks")
 def test_invalid_text_window_rejected(self):
  p=json.loads((ROOT/'docs/seoul-short.json').read_text());p['scenes'][0]['text_window']=[0,999]
  with self.assertRaisesRegex(ValueError,'Invalid text window'):render.validate(p,ROOT)

if __name__=='__main__':unittest.main()
