# -*- coding: utf-8 -*-
import re

with open('index.html', 'r', encoding='windows-1252', errors='ignore') as f:
    idx = f.read()

with open('contacts.html', 'r', encoding='windows-1252', errors='ignore') as f:
    cnt = f.read()

# 1. Grab everything from <body> to <!-- Page Main --> from index.html
top_match_idx = re.search(r'(<body>.*?<!-- Page Main -->)', idx, re.DOTALL)
if top_match_idx:
    idx_top = top_match_idx.group(1)
    
    # In idx_top, we must fix the active menu
    idx_top = idx_top.replace('<li class="current-menu-item">\n                            <a href="index.html">Home</a>', '<li>\n                            <a href="index.html">Home</a>')
    idx_top = idx_top.replace('<li>\n                            <a href="contacts.html">Contacts</a>', '<li class="current-menu-item">\n                            <a href="contacts.html">Contacts</a>')
    
    # 2. Replace the same region in contacts.html
    cnt = re.sub(r'<body>.*?<!-- Page Main -->', idx_top, cnt, flags=re.DOTALL)
    
    with open('contacts.html', 'w', encoding='windows-1252') as f:
        f.write(cnt)
    print("Successfully replaced everything from <body> to <main> in contacts.html!")
else:
    print("Could not find top block in index.html")
