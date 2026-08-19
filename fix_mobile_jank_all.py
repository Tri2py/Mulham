# -*- coding: utf-8 -*-
import re

files = ['contacts.html', 'portfolio.html']
header_mobile_css = '''        @media (max-width: 768px) {
            #bringer-header {
                min-width: 0;
                width: calc(100% - 40px) !important;
                padding: 0 20px !important;
            }'''

header_mobile_css_new = '''        @media (max-width: 768px) {
            #bringer-header {
                min-width: 0;
                width: calc(100% - 40px) !important;
                padding: 0 20px !important;
                backdrop-filter: none !important;
                -webkit-backdrop-filter: none !important;
                background: rgba(14, 8, 20, 0.95) !important;
            }'''

for filename in files:
    with open(filename, 'r', encoding='windows-1252', errors='ignore') as f:
        content = f.read()

    if header_mobile_css in content:
        content = content.replace(header_mobile_css, header_mobile_css_new)
        with open(filename, 'w', encoding='windows-1252') as f:
            f.write(content)
        print("Fixed " + filename)
