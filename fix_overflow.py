# -*- coding: utf-8 -*-
import re

files = ['index.html', 'contacts.html', 'portfolio.html']

for filename in files:
    with open(filename, 'r', encoding='windows-1252', errors='ignore') as f:
        content = f.read()

    # Add overflow-x: hidden to body
    if '<style>\n        body { overflow-x: hidden; }\n    </style>' not in content:
        content = content.replace('</head>', '    <style>\n        body { overflow-x: hidden !important; }\n    </style>\n</head>')

    with open(filename, 'w', encoding='windows-1252') as f:
        f.write(content)

print("Added overflow-x: hidden to all pages!")
