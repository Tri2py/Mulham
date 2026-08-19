# -*- coding: utf-8 -*-
import re

files_to_fix = ['contacts.html', 'portfolio.html']

for filename in files_to_fix:
    with open(filename, 'r', encoding='windows-1252', errors='ignore') as f:
        content = f.read()
    
    # Strip data-appear attributes to prevent conflict with our custom observer
    content = re.sub(r'\sdata-appear="[^"]*"', '', content)
    content = re.sub(r'\sdata-unload="[^"]*"', '', content)
    content = re.sub(r'\sdata-stagger-appear="[^"]*"', '', content)
    content = re.sub(r'\sdata-stagger-unload="[^"]*"', '', content)
    content = re.sub(r'\sdata-delay="[^"]*"', '', content)
    content = re.sub(r'\sdata-stagger-delay="[^"]*"', '', content)

    with open(filename, 'w', encoding='windows-1252') as f:
        f.write(content)
        
    print(f"Stripped legacy GSAP animation attributes from {filename}")

