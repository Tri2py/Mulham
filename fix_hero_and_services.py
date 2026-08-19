# -*- coding: utf-8 -*-
import re

with open('index.html', 'r', encoding='windows-1252', errors='ignore') as f:
    content = f.read()

# 1. Replace Hero Images with Colorized Line
gallery_regex = re.compile(r'<div class="diagonal-gallery".*?</div>\s*<!-- Foreground Difference Text Overlay -->', re.DOTALL)

new_hero_bg = '''<!-- Colorized Line Background -->
        <div class="colorized-line-bg" style="position: absolute; inset: 0; overflow: hidden; display: flex; align-items: center; justify-content: center; z-index: 1;">
            <!-- Outer Glow -->
            <div style="position: absolute; width: 250vw; height: 6px; background: linear-gradient(90deg, transparent 0%, #8C2DF6 40%, #e0c8ff 50%, #8C2DF6 60%, transparent 100%); transform: rotate(-12deg); filter: blur(8px); animation: pulseNeon 3s ease-in-out infinite alternate; box-shadow: 0 0 60px rgba(140,45,246,0.8), 0 0 120px rgba(140,45,246,0.5);"></div>
            <!-- Core Line -->
            <div style="position: absolute; width: 250vw; height: 2px; background: linear-gradient(90deg, transparent 0%, #ffffff 40%, #ffffff 60%, transparent 100%); transform: rotate(-12deg); box-shadow: 0 0 20px #ffffff;"></div>
            
            <style>
                @keyframes pulseNeon {
                    0% { opacity: 0.6; transform: rotate(-12deg) scaleX(0.9); }
                    100% { opacity: 1; transform: rotate(-12deg) scaleX(1.1); }
                }
            </style>
        </div>

        <!-- Foreground Difference Text Overlay -->'''

content = gallery_regex.sub(new_hero_bg, content, count=1)

# 2. Replace Services Cards
services_regex = re.compile(r'<!-- Branding -->.*?(?=</section>)', re.DOTALL)

new_services = '''<!-- Service Web Development -->
                    <div class="bringer-masked-block">
                        <div class="bringer-block stg-aspect-square stg-vertical-space-between bringer-masked-media" style="position: relative; border: 1px solid rgba(255,255,255,0.05); background: #080808;">
                            <div style="position: absolute; inset: 0; background: linear-gradient(to top, rgba(140,45,246,0.1), transparent); z-index: 0;"></div>
                            <h5 style="position: relative; z-index: 1; display: flex; align-items: center; gap: 10px;">
                                <i class="ph-bold ph-code" style="color: #8C2DF6; font-size: 1.2em;"></i>
                                Service Web Development<span class="bringer-accent">.</span>
                            </h5>
                            <p style="position: relative; z-index: 1; color: var(--bringer-s-text);">Modern, responsive websites built with the latest technologies for optimal performance.</p>
                        </div>
                    </div>

                    <!-- Service Designs -->
                    <div class="bringer-masked-block">
                        <div class="bringer-block stg-aspect-square stg-vertical-space-between bringer-masked-media" style="position: relative; border: 1px solid rgba(255,255,255,0.05); background: #080808;">
                            <div style="position: absolute; inset: 0; background: linear-gradient(to top, rgba(140,45,246,0.1), transparent); z-index: 0;"></div>
                            <h5 style="position: relative; z-index: 1; display: flex; align-items: center; gap: 10px;">
                                <i class="ph-bold ph-bezier-curve" style="color: #8C2DF6; font-size: 1.2em;"></i>
                                Service Designs<span class="bringer-accent">.</span>
                            </h5>
                            <p style="position: relative; z-index: 1; color: var(--bringer-s-text);">Creative branding, UI/UX design, and visual identity systems that make your business stand out.</p>
                        </div>
                    </div>
                </div>
            '''

content = services_regex.sub(new_services, content, count=1)

with open('index.html', 'w', encoding='windows-1252') as f:
    f.write(content)

print("Updated Hero and Services!")
