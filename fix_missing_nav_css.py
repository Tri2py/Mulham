# -*- coding: utf-8 -*-
import re

with open('index.html', 'r', encoding='windows-1252', errors='ignore') as f:
    index_content = f.read()

# Extract the glass navbar css
nav_css_match = re.search(r'(/\* Elegant Glass Navbar \*/.*?</style>)', index_content, re.DOTALL)
if nav_css_match:
    nav_css = '<style>\n' + nav_css_match.group(1)
else:
    print("Could not find glass navbar css in index.html")
    exit()

# We also need to extract the global color variables if not already present
color_vars = '''<style>
        :root {
            --bringer-s-accent: #8C2DF6 !important;
            --bringer-s-accent-hover: #ffffff !important;
            --bringer-s-body-bg: #000000 !important;
        }
        .bringer-accent { color: #8C2DF6 !important; }
    </style>'''

for filename in ['contacts.html', 'portfolio.html']:
    with open(filename, 'r', encoding='windows-1252', errors='ignore') as f:
        content = f.read()

    # Strip out the previous bad style blocks I added
    content = re.sub(r'<style>\s*:root\s*{.*?--bringer-s-accent.*?}.*?</style>', '', content, flags=re.DOTALL)
    
    # Also strip any leftover "Hide the misaligned JS active menu indicator" block
    content = re.sub(r'/\* Hide the misaligned JS active menu indicator \*/.*?</style>', '', content, flags=re.DOTALL)

    # Re-inject the clean blocks right before </head>
    new_head_injection = color_vars + '\n' + nav_css + '\n</head>'
    content = content.replace('</head>', new_head_injection)

    with open(filename, 'w', encoding='windows-1252') as f:
        f.write(content)
        
    print(f"Injected elegant glass navbar CSS into {filename}")

