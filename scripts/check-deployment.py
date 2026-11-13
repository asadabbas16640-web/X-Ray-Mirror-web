#!/usr/bin/env python3
"""Static deployment checks. Does not substitute for camera or clinical validation."""
from html.parser import HTMLParser
from pathlib import Path
import subprocess
import tempfile

ROOT=Path('_site')
import hashlib
reference=ROOT/'original-reference.html'
assert reference.is_file(), 'Original source reference missing'
expected='b5e12cd0755ac0976e655c4f9ac914c2a7a6b54474455d66549cbdfa6511dfb0'
actual=hashlib.sha256(reference.read_bytes()).hexdigest()
assert actual==expected, 'Original X-Ray Mirror source has changed unexpectedly'
for asset in ['vendor/mediapipe/vision_bundle.mjs','vendor/mediapipe/wasm/vision_wasm_internal.wasm','vendor/mediapipe/models/pose_landmarker_lite.task']:
    p=ROOT/asset
    assert p.is_file() and p.stat().st_size>1000, f'Missing local MediaPipe asset: {asset}'
PAGES=['index.html','medical-review.html','dicom-review.html','ct-series.html','ct-3d.html','full-body-lab.html','anatomy-3d.html']
class Parser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.scripts=[]
        self.current=None
        self.ids=set()
        self.links=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if a.get('id'):
            if a['id'] in self.ids: raise AssertionError(f'duplicate id: {a["id"]}')
            self.ids.add(a['id'])
        if tag=='script' and not a.get('src') and a.get('type','').lower() in ('','text/javascript','application/javascript','module'):
            self.current={'module':a.get('type')=='module','text':''}
            self.scripts.append(self.current)
        if tag=='a' and a.get('href','').startswith('./'):
            self.links.append(a['href'].split('?')[0][2:])
    def handle_data(self,data):
        if self.current is not None:self.current['text']+=data
    def handle_endtag(self,tag):
        if tag=='script':self.current=None
for page in PAGES:
    p=ROOT/page
    assert p.is_file() and p.stat().st_size>500,f'missing or empty: {page}'
    html=p.read_text(encoding='utf-8')
    parser=Parser();parser.feed(html)
    for link in parser.links:
        assert (ROOT/link).exists(),f'{page} links to missing {link}'
    for i,script in enumerate(parser.scripts):
        with tempfile.TemporaryDirectory() as d:
            path=Path(d)/('check.mjs' if script['module'] else 'check.js')
            path.write_text(script['text'],encoding='utf-8')
            subprocess.run(['node','--check',str(path)],check=True)
    print(f'PASS {page}: {len(parser.scripts)} inline scripts syntax-checked')
print('Static checks passed. Live browser, anatomical accuracy, and clinical performance remain unverified.')
