"""Régénère png/ depuis lucide-static : npm i lucide-static ; python3 build.py <dossier icons>"""
import os, sys, subprocess, json, concurrent.futures as cf
src = sys.argv[1]
names = sorted(f[:-4] for f in os.listdir(src) if f.endswith('.svg'))
os.makedirs('png', exist_ok=True); os.makedirs('/tmp/svg_pictos', exist_ok=True)
def r(n):
    t = open(f'{src}/{n}.svg').read().replace('currentColor', '#000000') \
        .replace('stroke-width="2"', 'stroke-width="1"').replace('viewBox="0 0 24 24"', 'viewBox="1.5 1.5 21 21"')
    p = f'/tmp/svg_pictos/{n}.svg'; open(p, 'w').write(t)
    return subprocess.run(['rsvg-convert', '-w', '512', '-h', '512', '-o', f'png/{n}.png', p]).returncode
with cf.ThreadPoolExecutor(8) as ex:
    assert sum(ex.map(r, names)) == 0
tags = json.load(open(os.path.join(src, '..', 'tags.json')))
json.dump({n: tags.get(n, []) for n in names}, open('catalogue.json', 'w'), ensure_ascii=False, indent=0)
print(len(names), 'icônes')
