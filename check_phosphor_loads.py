import glob
import re

for f in sorted(glob.glob('*.html')):
    with open(f, 'r', encoding='cp1252', errors='replace') as fp:
        txt = fp.read()
    matches = re.findall(r'<script[^>]*phosphor[^>]*>.*?</script>|<link[^>]*phosphor[^>]*>', txt, re.IGNORECASE | re.DOTALL)
    print(f"=== {f} ===")
    for m in matches:
        print("  ", m.strip()[:100])
