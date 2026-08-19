# -*- coding: utf-8 -*-
import re

with open('index.html', 'r', encoding='windows-1252', errors='ignore') as f:
    content = f.read()

# Revert height back to 100vh
content = content.replace('height: 115vh;', 'height: 100vh;')

# Change margin-bottom from 0 to 20vh (so the curtain starts fully off-screen)
content = content.replace('margin-bottom: 0;', 'margin-bottom: 20vh;')

with open('index.html', 'w', encoding='windows-1252') as f:
    f.write(content)

print("Hero sticky sizing fixed!")
