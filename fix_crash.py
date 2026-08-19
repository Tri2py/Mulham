# -*- coding: utf-8 -*-
import re

with open('index.html', 'r', encoding='windows-1252', errors='ignore') as f:
    content = f.read()

# 1. Remove the entire updateScroll skew logic
# We can just replace the contents of the DOMContentLoaded block that adds the skewing

bad_script_start = "              // Calculate Scroll Velocity"
bad_script_end = "          // Apply Parallax to background images"

content = re.sub(r'// Calculate Scroll Velocity.*?// Apply Parallax to background images', '// Apply Parallax to background images', content, flags=re.DOTALL)
content = re.sub(r'// Apply Velocity Skew to text and cards.*?ticking = false;', 'ticking = false;', content, flags=re.DOTALL)
content = re.sub(r'// Reset skew when scrolling stops.*?};', '};', content, flags=re.DOTALL)

# 2. Fix the noise filter completely.
old_gradient_1 = "<div style=\"position: absolute; inset: 0; background-image: url('data:image/svg+xml,%3Csvg viewBox=%220 0 200 200%22 xmlns=%22http://www.w3.org/2000/svg%22%3E%3Cfilter id=%22noiseFilter%22%3E%3CfeTurbulence type=%22fractalNoise%22 baseFrequency=%220.85%22 numOctaves=%223%22 stitchTiles=%22stitch%22/%3E%3C/filter%3E%3Crect width=%22100%25%22 height=%22100%25%22 filter=%22url(%23noiseFilter)%22 opacity=%220.08%22/%3E%3C/svg%3E'); z-index: 0; mix-blend-mode: overlay;\"></div>"
content = content.replace(old_gradient_1, "")

# Ensure it's done for both contacts and portfolio if they have the script
def fix_js_in_file(filename):
    try:
        with open(filename, 'r', encoding='windows-1252', errors='ignore') as f:
            c = f.read()
        
        c = re.sub(r'// Calculate Scroll Velocity.*?// Apply Parallax to background images', '// Apply Parallax to background images', c, flags=re.DOTALL)
        c = re.sub(r'// Apply Velocity Skew to text and cards.*?ticking = false;', 'ticking = false;', c, flags=re.DOTALL)
        c = re.sub(r'// Reset skew when scrolling stops.*?};', '};', c, flags=re.DOTALL)
        
        with open(filename, 'w', encoding='windows-1252') as f:
            f.write(c)
    except:
        pass

fix_js_in_file('contacts.html')
fix_js_in_file('portfolio.html')

with open('index.html', 'w', encoding='windows-1252') as f:
    f.write(content)

print("Removed skewing and heavy SVG filters!")
