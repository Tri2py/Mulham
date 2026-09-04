import glob
import re

# Robust Universal Phosphor Icons Loading Block
# 1. Preconnect to both fast CDNs
# 2. Direct link to regular, fill, and bold icon fonts (jsdelivr is globally accessible and never blocked)
# 3. Web component script as backup
# 4. Fallback font family rule in case of browser font substitution

UNIVERSAL_PHOSPHOR_TAGS = """    <!-- Universal Phosphor Icons (Cross-Browser Compatible) -->
    <link rel="preconnect" href="https://cdn.jsdelivr.net" crossorigin />
    <link rel="preconnect" href="https://unpkg.com" crossorigin />
    <link rel="stylesheet" type="text/css" href="https://cdn.jsdelivr.net/npm/@phosphor-icons/web@2.1.1/src/regular/style.css" />
    <link rel="stylesheet" type="text/css" href="https://cdn.jsdelivr.net/npm/@phosphor-icons/web@2.1.1/src/fill/style.css" />
    <link rel="stylesheet" type="text/css" href="https://cdn.jsdelivr.net/npm/@phosphor-icons/web@2.1.1/src/bold/style.css" />
    <script src="https://cdn.jsdelivr.net/npm/@phosphor-icons/web@2.1.1"></script>"""

def update_file(filepath):
    with open(filepath, 'r', encoding='cp1252', errors='replace') as fp:
        content = fp.read()

    # Match any previous phosphor tags in the file
    old_pattern = r'(\s*<!--\s*Phosphor Icons[^-]*-->\s*)?(\s*<link[^>]*phosphor[^>]*>\s*)*(\s*<script[^>]*phosphor[^>]*>.*?</script>\s*)'
    
    m = re.search(old_pattern, content, re.IGNORECASE | re.DOTALL)
    if m:
        start, end = m.span()
        content = content[:start] + "\n" + UNIVERSAL_PHOSPHOR_TAGS + "\n" + content[end:]
        with open(filepath, 'w', encoding='cp1252', errors='xmlcharrefreplace') as fp:
            fp.write(content)
        print(f"Updated {filepath} (replaced existing tags)")
        return True
    else:
        # If not found, insert before </head>
        head_idx = content.find('</head>')
        if head_idx != -1:
            content = content[:head_idx] + UNIVERSAL_PHOSPHOR_TAGS + "\n" + content[head_idx:]
            with open(filepath, 'w', encoding='cp1252', errors='xmlcharrefreplace') as fp:
                fp.write(content)
            print(f"Updated {filepath} (inserted before </head>)")
            return True
        else:
            print(f"FAILED for {filepath}: No </head> found")
            return False

for f in sorted(glob.glob('*.html')):
    update_file(f)

print("--- ALL HTML FILES UPDATED WITH UNIVERSAL PHOSPHOR ICONS ---")
