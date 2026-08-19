import shutil
import os
import glob
import re

brain_dir = r"C:\Users\MSI\.gemini\antigravity-cli\brain\ddabcc97-5173-4b75-bc1c-79e20ea9383d"
target_dir = r"C:\Users\MSI\Desktop\Mulham-main\img\home"

# Find generated images
for i in range(1, 5):
    pattern = os.path.join(brain_dir, f"hero_creative_{i}_*.jpg")
    found = glob.glob(pattern)
    if found:
        shutil.copy(found[0], os.path.join(target_dir, f"hero_creative_{i}.jpg"))
        print(f"Copied hero_creative_{i}.jpg")

with open('index.html', 'r', encoding='windows-1252', errors='ignore') as f:
    content = f.read()

# Make sure the hero section uses the absolute black #000000 background to match the site perfectly.
content = content.replace('background: #080808;', 'background: #000000;')

# Replace the images in the track. 
gallery_regex = re.compile(r'<div class="diagonal-gallery".*?</div>\s*<!-- Foreground Difference Text Overlay -->', re.DOTALL)

new_gallery = '''<div class="diagonal-gallery" style="position: absolute; top: -50%; left: -20%; width: 150vw; height: 200vh; transform: rotate(-12deg); display: flex; flex-direction: column; justify-content: center; gap: 2vw; opacity: 0.9; z-index: 1;">
            
            <!-- Track 1 (Left) -->
            <div class="marquee marquee-left">
                <div class="marquee-content">
                    <img src="img/home/hero_creative_1.jpg" alt="Creative Art">
                    <img src="img/home/hero_creative_2.jpg" alt="Creative Art">
                    <img src="img/home/hero_creative_3.jpg" alt="Creative Art">
                    <img src="img/home/hero_creative_4.jpg" alt="Creative Art">
                </div>
                <div class="marquee-content">
                    <img src="img/home/hero_creative_1.jpg" alt="Creative Art">
                    <img src="img/home/hero_creative_2.jpg" alt="Creative Art">
                    <img src="img/home/hero_creative_3.jpg" alt="Creative Art">
                    <img src="img/home/hero_creative_4.jpg" alt="Creative Art">
                </div>
            </div>

            <!-- Track 2 (Right) -->
            <div class="marquee marquee-right">
                <div class="marquee-content">
                    <img src="img/home/hero_creative_4.jpg" alt="Creative Art">
                    <img src="img/home/hero_creative_1.jpg" alt="Creative Art">
                    <img src="img/home/hero_creative_2.jpg" alt="Creative Art">
                    <img src="img/home/hero_creative_3.jpg" alt="Creative Art">
                </div>
                <div class="marquee-content">
                    <img src="img/home/hero_creative_4.jpg" alt="Creative Art">
                    <img src="img/home/hero_creative_1.jpg" alt="Creative Art">
                    <img src="img/home/hero_creative_2.jpg" alt="Creative Art">
                    <img src="img/home/hero_creative_3.jpg" alt="Creative Art">
                </div>
            </div>

            <!-- Track 3 (Left) -->
            <div class="marquee marquee-left" style="animation-duration: 45s;">
                <div class="marquee-content">
                    <img src="img/home/hero_creative_3.jpg" alt="Creative Art">
                    <img src="img/home/hero_creative_4.jpg" alt="Creative Art">
                    <img src="img/home/hero_creative_1.jpg" alt="Creative Art">
                    <img src="img/home/hero_creative_2.jpg" alt="Creative Art">
                </div>
                <div class="marquee-content">
                    <img src="img/home/hero_creative_3.jpg" alt="Creative Art">
                    <img src="img/home/hero_creative_4.jpg" alt="Creative Art">
                    <img src="img/home/hero_creative_1.jpg" alt="Creative Art">
                    <img src="img/home/hero_creative_2.jpg" alt="Creative Art">
                </div>
            </div>
        </div>

        <!-- Foreground Difference Text Overlay -->'''

content = gallery_regex.sub(new_gallery, content, count=1)

with open('index.html', 'w', encoding='windows-1252') as f:
    f.write(content)

print("Updated images and background color in index.html!")
