# -*- coding: utf-8 -*-
import re

files_to_fix = ['index.html', 'contacts.html', 'portfolio.html']

for filename in files_to_fix:
    with open(filename, 'r', encoding='windows-1252', errors='ignore') as f:
        content = f.read()
    
    # Force position fixed and z-index on the glass navbar
    if "position: fixed !important;" not in content and "#bringer-header {" in content:
        content = content.replace('#bringer-header {\n            background', '#bringer-header {\n            position: fixed !important;\n            z-index: 9999 !important;\n            background')
    
    with open(filename, 'w', encoding='windows-1252') as f:
        f.write(content)
        
    print(f"Forced fixed positioning on {filename}")

