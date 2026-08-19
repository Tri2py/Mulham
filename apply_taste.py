# -*- coding: utf-8 -*-
import re

with open('index.html', 'r', encoding='windows-1252', errors='ignore') as f:
    content = f.read()

# 1. Tint the pure black curtain to deep obsidian
# Currently: background: #000000;
content = content.replace('background: #000000; margin-left: calc(50% - 50vw);', 'background: #06020A; margin-left: calc(50% - 50vw);')

# 2. Fix Orphaned words & Typography in Section Titles
content = content.replace('<p class="bringer-large-text"   style="color: var(--bringer-s-text); font-weight: 300;">', '<p class="bringer-large-text"   style="color: rgba(255,255,255,0.7); font-weight: 400; text-wrap: balance; line-height: 1.6;">')
content = content.replace('<h2  style="font-family: \'Playfair Display\', serif; font-size: clamp(2rem, 5vw, 4rem); font-weight: 500;">', '<h2  style="font-family: \'Playfair Display\', serif; font-size: clamp(2.5rem, 6vw, 4.5rem); font-weight: 400; letter-spacing: -0.02em; line-height: 1.1; margin-bottom: 24px;">')

# 3. Enhance the Services Grid (Break Symmetry)
# Left card currently uses stg-aspect-square
content = content.replace('stg-aspect-square stg-vertical-space-between bringer-masked-media', 'stg-vertical-space-between bringer-masked-media premium-card', 2)

# We will inject specific inline styles to break symmetry and add premium glass/noise textures
old_card_1_style = 'style="position: relative; border: 1px solid rgba(255,255,255,0.05);"'
new_card_1_style = 'style="position: relative; border: 1px solid rgba(140,45,246,0.15); border-radius: 24px; overflow: hidden; aspect-ratio: 4/5; box-shadow: inset 0 0 50px rgba(140,45,246,0.05);"'

old_card_2_style = 'style="position: relative; border: 1px solid rgba(255,255,255,0.05);"'
new_card_2_style = 'style="position: relative; border: 1px solid rgba(255,255,255,0.08); border-radius: 24px; overflow: hidden; aspect-ratio: 1/1; transform: translateY(10%); box-shadow: inset 0 0 40px rgba(255,255,255,0.02);"'

# Since both cards have the same old style, we replace them sequentially.
content = content.replace(old_card_1_style, new_card_1_style, 1)
content = content.replace(old_card_1_style, new_card_2_style, 1) # second occurrence

# 4. Add subtle noise overlay inside the cards
old_gradient = '<div style="position: absolute; inset: 0; background: linear-gradient(to top, rgba(0,0,0,0.95), rgba(0,0,0,0.2)); z-index: 0;"></div>'
new_gradient = '<div style="position: absolute; inset: 0; background: linear-gradient(to top, rgba(6,2,10,0.95) 0%, rgba(6,2,10,0.2) 100%); z-index: 0;"></div><div style="position: absolute; inset: 0; background-image: url(\'data:image/svg+xml,%3Csvg viewBox=%220 0 200 200%22 xmlns=%22http://www.w3.org/2000/svg%22%3E%3Cfilter id=%22noiseFilter%22%3E%3CfeTurbulence type=%22fractalNoise%22 baseFrequency=%220.85%22 numOctaves=%223%22 stitchTiles=%22stitch%22/%3E%3C/filter%3E%3Crect width=%22100%25%22 height=%22100%25%22 filter=%22url(%23noiseFilter)%22 opacity=%220.08%22/%3E%3C/svg%3E\'); z-index: 0; mix-blend-mode: overlay;"></div>'
content = content.replace(old_gradient, new_gradient)

# 5. Fix card typography (tracking, weight)
content = content.replace('<h5 style="position: relative; z-index: 1;">', '<h5 style="position: relative; z-index: 1; font-family: \'Inter\', sans-serif; font-weight: 600; letter-spacing: -0.03em; font-size: 1.5rem; margin-bottom: 12px;">')
content = content.replace('<p style="position: relative; z-index: 1;">', '<p style="position: relative; z-index: 1; color: rgba(255,255,255,0.6); text-wrap: balance; font-size: 0.95rem; line-height: 1.6;">')

with open('index.html', 'w', encoding='windows-1252') as f:
    f.write(content)

print("Taste-skill enhancements applied!")
