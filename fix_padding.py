# -*- coding: utf-8 -*-
import re

files_to_fix = ['contacts.html', 'portfolio.html']

for filename in files_to_fix:
    with open(filename, 'r', encoding='windows-1252', errors='ignore') as f:
        content = f.read()
    
    # Add a global style to push the main content down since the navbar is floating
    padding_css = '''
    <style>
        main#bringer-main {
            padding-top: 150px !important;
        }
    </style>
    '''
    
    if "padding-top: 150px" not in content:
        content = content.replace('</head>', padding_css + '\n</head>')
    
    with open(filename, 'w', encoding='windows-1252') as f:
        f.write(content)
        
    print(f"Added top padding to {filename}")

