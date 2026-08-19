# -*- coding: utf-8 -*-
import re

# Read index.html for the new preloader and scroll scripts
with open('index.html', 'r', encoding='windows-1252', errors='ignore') as f:
    index_content = f.read()

# Extract preloader
preloader_match = re.search(r'(<!-- Preloader -->.*?<!-- Header -->)', index_content, re.DOTALL)
new_preloader = preloader_match.group(1) if preloader_match else ''

# Extract scroll scripts
scroll_script_match = re.search(r'(<!-- Two-Way Scroll Reveal Engine -->.*?)</body>', index_content, re.DOTALL)
new_scroll_script = scroll_script_match.group(1) if scroll_script_match else ''

# Read contacts.html
with open('contacts.html', 'r', encoding='windows-1252', errors='ignore') as f:
    port_content = f.read()

# 1. Replace Preloader
if new_preloader:
    port_content = re.sub(r'<!-- Preloader -->.*?<!-- Header -->', new_preloader, port_content, flags=re.DOTALL)

# 2. Replace Logo
port_content = re.sub(r'<img src="img/mulham_logo\.png".*?>', 'Mulham', port_content)
port_content = re.sub(r'<img src="img/mulham_logo_dark\.png".*?>', 'Mulham', port_content)

# 3. Add Custom Styles (Accent color & Black Background)
custom_styles = '''
    <style>
        :root {
            --bringer-s-accent: #8C2DF6 !important;
            --bringer-s-accent-hover: #ffffff !important;
            --bringer-s-body-bg: #000000 !important;
        }
        .bringer-accent { color: #8C2DF6 !important; }
        .bringer-header-inner {
            background: rgba(0, 0, 0, 0.7) !important;
            backdrop-filter: blur(20px);
        }
        .bringer-header-logo a {
            font-size: 24px;
            font-weight: 700;
            color: #fff;
            text-decoration: none;
            font-family: 'Playfair Display', serif;
        }
    </style>
</head>'''
port_content = port_content.replace('</head>', custom_styles)

# 4. Inject Two-Way Scroll Engine
if new_scroll_script:
    # Remove old if exists
    port_content = re.sub(r'<!-- Two-Way Scroll Reveal Engine -->.*?</body>', '</body>', port_content, flags=re.DOTALL)
    port_content = port_content.replace('</body>', new_scroll_script + '\n</body>')

with open('contacts.html', 'w', encoding='windows-1252') as f:
    f.write(port_content)

print("Synced contacts.html!")
