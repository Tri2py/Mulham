# -*- coding: utf-8 -*-
import re

files_to_fix = ['contacts.html', 'portfolio.html']

for filename in files_to_fix:
    with open(filename, 'r', encoding='windows-1252', errors='ignore') as f:
        content = f.read()
    
    # Remove the entire block of legacy CSS that breaks the layout
    # We'll use a regex to match the comment and the blocks associated with it
    content = re.sub(r'/\*\s*Logo - Outside navbar.*?\s*body:has\(#bringer-header\.is-sticky\) \.bringer-header-lp\s*{[^}]*}\s*', '', content, flags=re.DOTALL)
    
    # Also just manually replace any leftover .bringer-header-lp { position: fixed !important; ... } if the regex missed it
    content = re.sub(r'\.bringer-header-lp\s*{\s*position: fixed !important;.*?transition: all 0\.3s ease !important;\s*}', '', content, flags=re.DOTALL)
    
    # Let's remove any style block that contains this to be safe, if it's isolated
    content = re.sub(r'<style>\s*/\*\s*Logo - Outside navbar.*?</style>', '', content, flags=re.DOTALL)

    with open(filename, 'w', encoding='windows-1252') as f:
        f.write(content)
        
    print(f"Removed legacy breaking CSS from {filename}")

