# -*- coding: utf-8 -*-
import re

with open('index.html', 'r', encoding='windows-1252', errors='ignore') as f:
    content = f.read()

new_footer = '''        <!-- Premium 10/10 Footer -->
        <footer id="bringer-footer" style="background: #06020A; padding-top: 15vh; position: relative; overflow: hidden; border-top: 1px solid rgba(140,45,246,0.1); margin-left: calc(50% - 50vw); width: 100vw;">
            <div class="stg-container" style="position: relative; z-index: 2; display: flex; flex-direction: column; min-height: 50vh; justify-content: space-between;">
                
                <!-- Top row: CTA -->
                <div style="display: flex; flex-direction: column; align-items: center; text-align: center; margin-bottom: 10vh;">
                    <p style="font-family: 'Inter', sans-serif; font-size: 0.75rem; font-weight: 500; letter-spacing: 0.3em; color: #8C2DF6; text-transform: uppercase; margin-bottom: 3vh;">Got a vision?</p>
                    <h2 style="font-family: 'Playfair Display', serif; font-size: clamp(3rem, 7vw, 6rem); font-weight: 400; letter-spacing: -0.03em; line-height: 1.1; margin-bottom: 6vh; max-width: 900px; color: #fff;">Let's build something <span style="font-style: italic; color: rgba(255,255,255,0.4);">extraordinary.</span></h2>
                    
                    <a href="contacts.html" class="glass-pill" style="display: inline-flex; align-items: center; gap: 15px; text-decoration: none; font-size: 0.85rem; padding: 20px 40px; background: rgba(140,45,246,0.1); border: 1px solid rgba(140,45,246,0.3); border-radius: 100px; color: #fff; font-family: 'Inter', sans-serif; font-weight: 500; text-transform: uppercase; letter-spacing: 0.15em; transition: all 0.3s ease; box-shadow: 0 10px 30px rgba(140,45,246,0.15);">
                        Start a Project
                        <i class="ph-fill ph-arrow-right" style="font-size: 1.2rem; color: #8C2DF6;"></i>
                    </a>
                </div>
                
                <!-- Bottom Row: Socials & Info -->
                <div style="display: flex; justify-content: space-between; align-items: center; border-top: 1px solid rgba(255,255,255,0.05); padding-top: 4vh; padding-bottom: 4vh; flex-wrap: wrap; gap: 20px;">
                    <div style="font-family: 'Inter', sans-serif; font-size: 0.8rem; color: rgba(255,255,255,0.4);">
                        &copy; 2026 Mulham Ibrahim. All rights reserved.
                    </div>
                    
                    <!-- Social Links -->
                    <ul class="bringer-socials-list" style="margin: 0; padding: 0; display: flex; gap: 20px; list-style: none;">
                        <li><a href="https://www.pinterest.com/normal_person_as_trippy/" target="_blank" style="text-decoration: none;"><i class="ph-fill ph-pinterest-logo"></i></a></li>
                        <li><a href="https://www.instagram.com/creative_mulham/" target="_blank" style="text-decoration: none;"><i class="ph-fill ph-instagram-logo"></i></a></li>
                        <li><a href="https://www.linkedin.com/in/mulham-ibrahim-2021643ab" target="_blank" style="text-decoration: none;"><i class="ph-fill ph-linkedin-logo"></i></a></li>
                    </ul>
                </div>
            </div>
            
            <!-- Massive Background Typography -->
            <div style="text-align: center; overflow: hidden; line-height: 0.75; margin-bottom: -5vw; pointer-events: none; opacity: 0.02; user-select: none;">
                <span style="font-family: 'Inter', sans-serif; font-weight: 900; font-size: 24vw; letter-spacing: -0.05em; color: #fff; white-space: nowrap;">MULHAM</span>
            </div>
        </footer>'''

# Find the footer bounds and replace it
content = re.sub(r'<!-- Footer -->\s*<footer id="bringer-footer".*?</footer>', new_footer, content, flags=re.DOTALL)

with open('index.html', 'w', encoding='windows-1252') as f:
    f.write(content)

print("Massive footer deployed!")
