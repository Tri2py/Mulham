# -*- coding: utf-8 -*-
import re

with open('index.html', 'r', encoding='windows-1252', errors='ignore') as f:
    content = f.read()

# 1. Remove mix-blend-mode: difference
content = content.replace('mix-blend-mode: difference;', '/* mix-blend-mode removed for visibility */')

# 2. Lower opacity of the gallery to make text pop, or add a dark overlay. 
# The gallery has opacity: 0.9. Let's change it to opacity: 0.45.
content = content.replace('opacity: 0.9; z-index: 1;', 'opacity: 0.35; z-index: 1;')

# 3. Add text-shadow to the massive text for extra pop
content = content.replace('color: #ffffff; margin: 0; text-transform: uppercase;', 'color: #ffffff; margin: 0; text-transform: uppercase; text-shadow: 0 10px 30px rgba(0,0,0,0.8);')
content = content.replace('color: #ffffff; margin: 0; text-align: right; margin-top: -2vw;', 'color: #ffffff; margin: 0; text-align: right; margin-top: -2vw; text-shadow: 0 10px 30px rgba(0,0,0,0.8);')

# 4. Remove grayscale filter and hover effect from CSS
css_to_remove = '''filter: grayscale(100%) contrast(1.1) brightness(0.8);
                transition: filter 0.8s cubic-bezier(0.165, 0.84, 0.44, 1);'''
content = content.replace(css_to_remove, '/* filters removed, always in color */')

hover_css = '''/* Hover Interaction: Reveal true colors */
            #awwwards-hero:hover .marquee-content img {
                filter: grayscale(0%) contrast(1) brightness(1);
            }'''
content = content.replace(hover_css, '')

with open('index.html', 'w', encoding='windows-1252') as f:
    f.write(content)

print("Hero colors and visibility fixed.")
