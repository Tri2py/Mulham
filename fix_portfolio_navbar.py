# -*- coding: utf-8 -*-
import re

# Grab the correct header from index.html
with open('index.html', 'r', encoding='windows-1252', errors='ignore') as f:
    index_content = f.read()

header_match = re.search(r'(<header id="bringer-header".*?</header>)', index_content, re.DOTALL)
if header_match:
    correct_header = header_match.group(1)

    # Inject it into portfolio.html
    with open('portfolio.html', 'r', encoding='windows-1252', errors='ignore') as f:
        port_content = f.read()
        
    port_content = re.sub(r'<header id="bringer-header".*?</header>', correct_header, port_content, flags=re.DOTALL)
    
    with open('portfolio.html', 'w', encoding='windows-1252') as f:
        f.write(port_content)
    
    print("Portfolio navbar fixed successfully!")
