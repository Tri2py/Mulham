# -*- coding: utf-8 -*-
import re

with open('index.html', 'r', encoding='windows-1252', errors='ignore') as f:
    idx = f.read()

with open('contacts.html', 'r', encoding='windows-1252', errors='ignore') as f:
    cnt = f.read()

idx_match = re.search(r'<header id="bringer-header".*?</header>', idx, re.DOTALL)
cnt_match = re.search(r'<header id="bringer-header".*?</header>', cnt, re.DOTALL)

if idx_match and cnt_match:
    idx_str = idx_match.group(0).strip()
    cnt_str = cnt_match.group(0).strip()
    
    # Ignore the current-menu-item difference
    idx_str = idx_str.replace('<li class="current-menu-item">', '<li>')
    cnt_str = cnt_str.replace('<li class="current-menu-item">', '<li>')
    
    if idx_str == cnt_str:
        print("The header HTML is EXACTLY identical.")
    else:
        print("The header HTML is DIFFERENT.")
        # Find first diff
        for i, (a, b) in enumerate(zip(idx_str, cnt_str)):
            if a != b:
                print(f"Diff at index {i}:")
                print(f"Index.html: {idx_str[max(0, i-20):i+20]}")
                print(f"Contacts.html: {cnt_str[max(0, i-20):i+20]}")
                break
        print("Length diff:", len(idx_str), len(cnt_str))
