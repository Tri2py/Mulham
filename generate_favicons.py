import os
from PIL import Image, ImageDraw, ImageFilter

os.makedirs('img', exist_ok=True)

# 1. Create SVG Favicon
svg_content = \"\"\"<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0E051B"/>
      <stop offset="100%" stop-color="#06020A"/>
    </linearGradient>
    <linearGradient id="mGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#C084FC"/>
      <stop offset="50%" stop-color="#8C2DF6"/>
      <stop offset="100%" stop-color="#6B14D1"/>
    </linearGradient>
    <linearGradient id="mGrad2" x1="100%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#E9D5FF"/>
      <stop offset="100%" stop-color="#8C2DF6"/>
    </linearGradient>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="16" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
    <linearGradient id="borderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#8C2DF6" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#C084FC" stop-opacity="0.2"/>
    </linearGradient>
  </defs>

  <rect x="16" y="16" width="480" height="480" rx="120" fill="url(#bgGrad)" stroke="url(#borderGrad)" stroke-width="6"/>
  <circle cx="256" cy="256" r="160" fill="#8C2DF6" opacity="0.15" filter="url(#glow)"/>

  <path d="M120 380 L120 150 L175 150 L200 380 Z" fill="url(#mGrad1)" filter="url(#glow)"/>
  <path d="M392 380 L392 150 L337 150 L312 380 Z" fill="url(#mGrad1)" filter="url(#glow)"/>
  <path d="M165 150 L256 315 L220 315 L145 150 Z" fill="url(#mGrad2)"/>
  <path d="M347 150 L256 315 L292 315 L367 150 Z" fill="url(#mGrad2)"/>

  <polygon points="256,220 280,270 256,310 232,270" fill="#FFFFFF" opacity="0.95"/>
  <circle cx="256" cy="115" r="14" fill="#C084FC" filter="url(#glow)"/>
</svg>
\"\"\"

with open('favicon.svg', 'w', encoding='utf-8') as f:
    f.write(svg_content)
with open('img/favicon.svg', 'w', encoding='utf-8') as f:
    f.write(svg_content)

print("Created favicon.svg")

def create_master_icon(size=512):
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    corner_radius = int(size * 0.24)
    
    for y in range(size):
        r = int(14 - (8 * (y / size)))
        g = int(5 - (3 * (y / size)))
        b = int(27 - (17 * (y / size)))
        draw.rounded_rectangle([16, 16, size-16, size-16], radius=corner_radius, fill=(r, g, b, 255))
    
    draw.rounded_rectangle([16, 16, size-16, size-16], radius=corner_radius, outline=(140, 45, 246, 180), width=int(size * 0.015))
    
    glow = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    glow_draw = ImageDraw.Draw(glow)
    glow_draw.ellipse([size*0.25, size*0.25, size*0.75, size*0.75], fill=(140, 45, 246, 90))
    glow = glow.filter(ImageFilter.GaussianBlur(int(size * 0.12)))
    img = Image.alpha_composite(img, glow)
    
    draw = ImageDraw.Draw(img)
    scale = size / 512.0
    
    def pt(x, y):
        return (int(x * scale), int(y * scale))
    
    draw.polygon([pt(120, 380), pt(120, 150), pt(175, 150), pt(200, 380)], fill=(140, 45, 246, 255))
    draw.polygon([pt(392, 380), pt(392, 150), pt(337, 150), pt(312, 380)], fill=(140, 45, 246, 255))
    draw.polygon([pt(165, 150), pt(256, 315), pt(220, 315), pt(145, 150)], fill=(192, 132, 252, 255))
    draw.polygon([pt(347, 150), pt(256, 315), pt(292, 315), pt(367, 150)], fill=(233, 213, 255, 255))
    draw.polygon([pt(256, 220), pt(280, 270), pt(256, 310), pt(232, 270)], fill=(255, 255, 255, 245))
    dot_r = int(14 * scale)
    draw.ellipse([pt(256, 115)[0]-dot_r, pt(256, 115)[1]-dot_r, pt(256, 115)[0]+dot_r, pt(256, 115)[1]+dot_r], fill=(192, 132, 252, 255))

    return img

master_icon = create_master_icon(512)

sizes = {
    'favicon.png': 32,
    'img/favicon.png': 32,
    'img/favicon-16x16.png': 16,
    'img/favicon-32x32.png': 32,
    'img/favicon-48x48.png': 48,
    'img/apple-touch-icon.png': 180,
    'img/android-chrome-192x192.png': 192,
    'img/android-chrome-512x512.png': 512,
    'img/mulham_icon.png': 512
}

for filename, sz in sizes.items():
    resized = master_icon.resize((sz, sz), Image.Resampling.LANCZOS)
    resized.save(filename, 'PNG')
    print(f"Saved {filename} ({sz}x{sz})")

icon_16 = master_icon.resize((16, 16), Image.Resampling.LANCZOS)
icon_32 = master_icon.resize((32, 32), Image.Resampling.LANCZOS)
icon_48 = master_icon.resize((48, 48), Image.Resampling.LANCZOS)
icon_16.save('favicon.ico', format='ICO', sizes=[(16,16), (32,32), (48,48)], append_images=[icon_32, icon_48])
icon_16.save('img/favicon.ico', format='ICO', sizes=[(16,16), (32,32), (48,48)], append_images=[icon_32, icon_48])
print("Saved favicon.ico")

manifest_content = \"\"\"{
  "name": "Mulham Ibrahim - Portfolio",
  "short_name": "Mulham",
  "description": "Creative Developer and Digital Experience Architect. UI/UX, Web Engineering, and Brand Systems.",
  "start_url": "/home",
  "display": "standalone",
  "background_color": "#06020A",
  "theme_color": "#8C2DF6",
  "icons": [
    {
      "src": "/img/favicon-32x32.png",
      "sizes": "32x32",
      "type": "image/png"
    },
    {
      "src": "/img/android-chrome-192x192.png",
      "sizes": "192x192",
      "type": "image/png"
    },
    {
      "src": "/img/android-chrome-512x512.png",
      "sizes": "512x512",
      "type": "image/png",
      "purpose": "any maskable"
    }
  ]
}
\"\"\"
with open('site.webmanifest', 'w', encoding='utf-8') as f:
    f.write(manifest_content)
print("Created site.webmanifest")

og_img = Image.new('RGBA', (1200, 630), (6, 2, 10, 255))
og_draw = ImageDraw.Draw(og_img)

nebula = Image.new('RGBA', (1200, 630), (0, 0, 0, 0))
nebula_draw = ImageDraw.Draw(nebula)
nebula_draw.ellipse([750, -150, 1450, 550], fill=(140, 45, 246, 75))
nebula_draw.ellipse([-200, 250, 650, 950], fill=(107, 20, 209, 65))
nebula = nebula.filter(ImageFilter.GaussianBlur(130))
og_img = Image.alpha_composite(og_img, nebula)
og_draw = ImageDraw.Draw(og_img)

emblem = master_icon.resize((260, 260), Image.Resampling.LANCZOS)
og_img.paste(emblem, (850, 185), emblem)

for x in range(0, 1200, 100):
    og_draw.line([(x, 0), (x, 630)], fill=(140, 45, 246, 15), width=1)
for y in range(0, 630, 100):
    og_draw.line([(0, y), (1200, y)], fill=(140, 45, 246, 15), width=1)

og_draw.rectangle([20, 20, 1180, 610], outline=(140, 45, 246, 60), width=2)
og_draw.rounded_rectangle([90, 85, 420, 130], radius=22, fill=(20, 10, 35, 220), outline=(140, 45, 246, 150), width=1)
og_draw.text((115, 98), "PORTFOLIO & DIGITAL STUDIO", fill=(192, 132, 252, 255))
og_draw.text((90, 160), "MULHAM", fill=(255, 255, 255, 255))
og_draw.text((90, 250), "IBRAHIM", fill=(140, 45, 246, 255))
og_draw.text((90, 370), "Digital Experience Architect & Creative Developer", fill=(255, 255, 255, 230))
og_draw.text((90, 420), "Founder of Plasma Agency - UI/UX Design - Brand Identity - Web Engineering", fill=(180, 180, 190, 200))
og_draw.line([(90, 480), (750, 480)], fill=(140, 45, 246, 80), width=1)
og_draw.text((90, 515), "https://mulham.design", fill=(192, 132, 252, 255))
og_draw.text((500, 515), "EST. 2026", fill=(120, 120, 140, 200))

og_img_rgb = og_img.convert('RGB')
og_img_rgb.save('img/og-image.jpg', 'JPEG', quality=95)
og_img_rgb.save('img/og-image.png', 'PNG')
og_img_rgb.save('og-image.jpg', 'JPEG', quality=95)
print("Saved og-image.jpg and og-image.png")
