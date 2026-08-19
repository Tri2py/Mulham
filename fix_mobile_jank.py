# -*- coding: utf-8 -*-
import re

with open('index.html', 'r', encoding='windows-1252', errors='ignore') as f:
    content = f.read()

# 1. Fix iOS viewport jump
content = content.replace('height: 100vh;', 'height: 100dvh;')

# 2. Add backdrop-filter removal to the mobile media query
# First, let's find the @media (max-width: 900px) block for hero elements
hero_mobile_css = '''                /* Center the scroll button */
                .hero-scroll-btn { 
                    width: 70px !important; 
                    height: 70px !important; 
                    bottom: 6vh !important; 
                    right: 50% !important; 
                    transform: translateX(50%) !important; 
                    font-size: 0.55rem !important;
                }'''

hero_mobile_css_new = '''                /* Center the scroll button */
                .hero-scroll-btn { 
                    width: 70px !important; 
                    height: 70px !important; 
                    bottom: 6vh !important; 
                    right: 50% !important; 
                    transform: translateX(50%) !important; 
                    font-size: 0.55rem !important;
                    backdrop-filter: none !important;
                    -webkit-backdrop-filter: none !important;
                    background: rgba(14, 8, 20, 0.8) !important;
                }'''
content = content.replace(hero_mobile_css, hero_mobile_css_new)

# 3. Find the @media (max-width: 768px) block for the header and remove its backdrop-filter
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
content = content.replace(header_mobile_css, header_mobile_css_new)

with open('index.html', 'w', encoding='windows-1252') as f:
    f.write(content)

print("Mobile scroll jank fixes applied!")
