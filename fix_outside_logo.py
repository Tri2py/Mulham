# -*- coding: utf-8 -*-
import re

files_to_fix = ['contacts.html', 'portfolio.html']

for filename in files_to_fix:
    with open(filename, 'r', encoding='windows-1252', errors='ignore') as f:
        content = f.read()
    
    # Remove the logo that is outside the header
    content = re.sub(r'<!-- Logo - Outside navbar.*?</div>\s*<!-- Header -->', '<!-- Header -->', content, flags=re.DOTALL)
    
    with open(filename, 'w', encoding='windows-1252') as f:
        f.write(content)
        
    print(f"Removed redundant outside logo from {filename}")

