import glob
import re

for f in sorted(glob.glob('*.html')):
    with open(f, 'r', encoding='cp1252', errors='replace') as fp:
        txt = fp.read()
    icons = re.findall(r'ph-[a-z0-9-]+', txt)
    if icons:
        print(f"{f:22} | {len(set(icons))} unique icons: {sorted(list(set(icons)))}")
