# -*- coding: utf-8 -*-
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_hero = '''    <!-- Professional Premium Hero Section -->
    <section class="bringer-hero-section" style="position: relative; width: 100%; min-height: 100vh; display: flex; flex-direction: column; align-items: center; justify-content: center; overflow: hidden; padding-top: 80px; padding-bottom: 10vh; margin: 0;">

        <!-- Ambient Background Sub-layers -->
        <div style="position: absolute; inset: 0; background: #050505; z-index: 1;">
            <!-- Subtle Radial Purple Core -->
            <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 800px; height: 800px; background: radial-gradient(circle, rgba(140,45,246,0.12) 0%, rgba(140,45,246,0) 60%); filter: blur(50px); pointer-events: none;"></div>
            
            <!-- Premium Tech Grid Overlay -->
            <div style="position: absolute; inset: 0; background-image: linear-gradient(rgba(255,255,255,0.03) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.03) 1px, transparent 1px); background-size: 50px 50px; pointer-events: none; mask-image: radial-gradient(ellipse at center, black 30%, transparent 70%); -webkit-mask-image: radial-gradient(ellipse at center, black 30%, transparent 70%); opacity: 0.7;"></div>
        </div>

        <!-- Foreground Content Container -->
        <div style="position: relative; z-index: 3; text-align: center; width: 100%; max-width: 1200px; padding: 0 20px; display: flex; flex-direction: column; align-items: center;">
            
            <!-- Status Pill -->
            <div data-appear="fade-down" data-delay="100" style="display: inline-flex; align-items: center; gap: 10px; padding: 8px 18px; background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.06); border-radius: 100px; margin-bottom: 4vh; backdrop-filter: blur(10px); box-shadow: 0 4px 20px rgba(0,0,0,0.5);">
                <div style="width: 8px; height: 8px; background: #8C2DF6; border-radius: 50%; box-shadow: 0 0 12px #8C2DF6; animation: pulseStatus 2s infinite;"></div>
                <span style="font-family: 'Inter', sans-serif; text-transform: uppercase; letter-spacing: 0.15em; font-size: 0.7rem; color: #aaa; font-weight: 500;">Mulham Ibrahim &mdash; Available for work</span>
            </div>
            
            <!-- Massive Clean Headline -->
            <h1 style="font-family: 'Playfair Display', serif; font-size: clamp(3.5rem, 8vw, 7.5rem); font-weight: 500; line-height: 1.05; letter-spacing: -0.02em; color: #ffffff; margin-bottom: 2.5rem;" data-appear="fade-up" data-delay="200">
                Crafting digital <br>
                <span style="font-style: italic; color: #8C2DF6; padding-right: 10px;">experiences</span> that inspire.
            </h1>
            
            <!-- Professional Subheadline -->
            <p style="font-family: 'Inter', sans-serif; font-size: clamp(1rem, 1.8vw, 1.25rem); color: #888888; max-width: 600px; margin: 0 auto 4rem; line-height: 1.6; font-weight: 400;" data-appear="fade-up" data-delay="300">
                Specializing in full-stack web design, UI/UX optimization, and data-driven digital marketing strategies to elevate your brand.
            </p>
            
            <!-- Premium CTA Buttons -->
            <div data-appear="fade-up" data-delay="400" style="display: flex; gap: 20px; align-items: center; justify-content: center; flex-wrap: wrap;">
                <!-- Primary Solid Button -->
                <a href="#cv-preview" onclick="document.getElementById('cv-preview').scrollIntoView({behavior: 'smooth'}); return false;" style="background: #ffffff; color: #050505; padding: 18px 40px; border-radius: 100px; font-family: 'Inter', sans-serif; font-size: 0.95rem; font-weight: 600; text-decoration: none; display: inline-flex; align-items: center; gap: 8px; transition: all 0.3s ease; box-shadow: 0 4px 15px rgba(255,255,255,0.1);" onmouseover="this.style.transform='translateY(-3px)'; this.style.boxShadow='0 12px 24px rgba(255,255,255,0.2)';" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 4px 15px rgba(255,255,255,0.1)';">
                    Read My CV <i class="ph-bold ph-arrow-down" style="font-size: 18px;"></i>
                </a>
                
                <!-- Secondary Ghost Button -->
                <a href="contacts.html" style="background: rgba(255,255,255,0.03); color: #ffffff; border: 1px solid rgba(255,255,255,0.1); padding: 18px 40px; border-radius: 100px; font-family: 'Inter', sans-serif; font-size: 0.95rem; font-weight: 600; text-decoration: none; display: inline-flex; align-items: center; gap: 8px; transition: all 0.3s ease; backdrop-filter: blur(5px);" onmouseover="this.style.background='rgba(255,255,255,0.08)'; this.style.borderColor='rgba(255,255,255,0.2)';" onmouseout="this.style.background='rgba(255,255,255,0.03)'; this.style.borderColor='rgba(255,255,255,0.1)';">
                    Get in touch <i class="ph-bold ph-arrow-right" style="font-size: 18px;"></i>
                </a>
            </div>
            
        </div>

        <style>
            @keyframes pulseStatus {
                0% { box-shadow: 0 0 0 0 rgba(140, 45, 246, 0.4); }
                70% { box-shadow: 0 0 0 10px rgba(140, 45, 246, 0); }
                100% { box-shadow: 0 0 0 0 rgba(140, 45, 246, 0); }
            }
        </style>
    </section>'''

# Regex to replace everything from <!-- Avant-Garde Asymmetrical Hero Section --> down to </section> before Services
pattern = re.compile(r'<!-- Avant-Garde Asymmetrical Hero Section -->.*?</section>', re.DOTALL)
new_content = pattern.sub(new_hero, content, count=1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Pro Hero Updated!")
