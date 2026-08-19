# -*- coding: utf-8 -*-
import re

with open('index.html', 'r', encoding='windows-1252', errors='ignore') as f:
    content = f.read()

# Fix the button
content = content.replace("getElementById('cv-preview')", "getElementById('about')")
content = content.replace('href="#cv-preview"', 'href="#about"')

with open('index.html', 'w', encoding='windows-1252') as f:
    f.write(content)

print("Fixed scroll button!")
