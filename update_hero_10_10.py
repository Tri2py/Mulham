# -*- coding: utf-8 -*-
import re

with open('index.html', 'r', encoding='windows-1252', errors='replace') as f:
    content = f.read()

new_hero = '''    <!-- 10/10 Creative Portfolio Hero Section -->
    <section class="bringer-hero-section" id="awwwards-hero" style="position: relative; width: 100vw; height: 100vh; overflow: hidden; background: #080808; margin-left: calc(50% - 50vw); margin-top: -120px; margin-bottom: 0;">

        <!-- Diagonal Infinite Gallery Background -->
        <div class="diagonal-gallery" style="position: absolute; top: -50%; left: -20%; width: 150vw; height: 200vh; transform: rotate(-12deg); display: flex; flex-direction: column; justify-content: center; gap: 2vw; opacity: 0.8; z-index: 1;">
            
            <!-- Track 1 (Left) -->
            <div class="marquee marquee-left">
                <!-- Group 1 -->
                <div class="marquee-content">
                    <img src="img/home/services_branding.jpg" alt="Work">
                    <img src="img/home/services_digital_fluid.jpg" alt="Work">
                    <img src="img/home/services_abstract_violet.jpg" alt="Work">
                    <img src="img/home/services_marketing.jpg" alt="Work">
                </div>
                <!-- Group 2 (Clone for infinite scroll) -->
                <div class="marquee-content">
                    <img src="img/home/services_branding.jpg" alt="Work">
                    <img src="img/home/services_digital_fluid.jpg" alt="Work">
                    <img src="img/home/services_abstract_violet.jpg" alt="Work">
                    <img src="img/home/services_marketing.jpg" alt="Work">
                </div>
            </div>

            <!-- Track 2 (Right) -->
            <div class="marquee marquee-right">
                <div class="marquee-content">
                    <img src="img/home/home01-hero.jpg" alt="Work">
                    <img src="img/home/home02-hero02.jpg" alt="Work">
                    <img src="img/home/home03-hero2.jpg" alt="Work">
                    <img src="img/home/services_web.jpg" alt="Work">
                </div>
                <div class="marquee-content">
                    <img src="img/home/home01-hero.jpg" alt="Work">
                    <img src="img/home/home02-hero02.jpg" alt="Work">
                    <img src="img/home/home03-hero2.jpg" alt="Work">
                    <img src="img/home/services_web.jpg" alt="Work">
                </div>
            </div>

            <!-- Track 3 (Left) -->
            <div class="marquee marquee-left" style="animation-duration: 45s;">
                <div class="marquee-content">
                    <img src="img/home/social-proof01.jpg" alt="Work">
                    <img src="img/home/social-proof02.jpg" alt="Work">
                    <img src="img/home/social-proof03.jpg" alt="Work">
                    <img src="img/home/social-proof04.jpg" alt="Work">
                </div>
                <div class="marquee-content">
                    <img src="img/home/social-proof01.jpg" alt="Work">
                    <img src="img/home/social-proof02.jpg" alt="Work">
                    <img src="img/home/social-proof03.jpg" alt="Work">
                    <img src="img/home/social-proof04.jpg" alt="Work">
                </div>
            </div>
        </div>

        <!-- Foreground Difference Text Overlay -->
        <div class="hero-blend-text" style="position: absolute; inset: 0; display: flex; flex-direction: column; justify-content: center; padding: 0 5vw; pointer-events: none; mix-blend-mode: difference; z-index: 10;">
            
            <!-- Editorial Header -->
            <div style="display: flex; justify-content: space-between; align-items: flex-end; border-bottom: 1px solid rgba(255,255,255,0.5); padding-bottom: 2vh; margin-bottom: 2vh;">
                <span style="font-family: 'Inter', sans-serif; color: #fff; font-size: clamp(0.7rem, 1vw, 1.2rem); font-weight: 500; text-transform: uppercase; letter-spacing: 0.15em; max-width: 250px; line-height: 1.4;">
                    Portfolio 2026<br>Digital Craft &mdash; UI/UX
                </span>
                <span style="font-family: 'Inter', sans-serif; color: #fff; font-size: clamp(0.7rem, 1vw, 1.2rem); font-weight: 500; text-transform: uppercase; letter-spacing: 0.15em; text-align: right; line-height: 1.4;">
                    Damascus, Syria<br>Available Worldwide
                </span>
            </div>
            
            <!-- Brutalist Typography -->
            <h1 style="font-family: 'Inter', sans-serif; font-size: 16vw; font-weight: 900; line-height: 0.8; letter-spacing: -0.05em; color: #ffffff; margin: 0; text-transform: uppercase;">
                MULHAM
            </h1>
            <h1 style="font-family: 'Playfair Display', serif; font-size: 15.5vw; font-weight: 400; font-style: italic; line-height: 0.8; letter-spacing: -0.03em; color: #ffffff; margin: 0; text-align: right; margin-top: -2vw;">
                IBRAHIM
            </h1>
            
        </div>

        <!-- Interactive Scroll Button (Non-blend, clickable) -->
        <a href="#cv-preview" onclick="document.getElementById('cv-preview').scrollIntoView({behavior: 'smooth'}); return false;" class="hero-scroll-btn" style="position: absolute; bottom: 5vh; right: 5vw; z-index: 20; width: 120px; height: 120px; border-radius: 50%; border: 1px solid rgba(255,255,255,0.2); display: flex; align-items: center; justify-content: center; color: #fff; text-decoration: none; backdrop-filter: blur(10px); -webkit-backdrop-filter: blur(10px); transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1); font-family: 'Inter', sans-serif; font-size: 0.75rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.1em; background: rgba(255,255,255,0.03);">
            Explore
        </a>

        <!-- CSS Styles -->
        <style>
            /* The image track styles */
            .marquee {
                display: flex;
                gap: 2vw;
                width: max-content;
            }
            .marquee-content {
                display: flex;
                gap: 2vw;
            }
            .marquee-content img {
                width: 25vw;
                height: 38vh;
                object-fit: cover;
                border-radius: 4px;
                filter: grayscale(100%) contrast(1.1) brightness(0.8);
                transition: filter 0.8s cubic-bezier(0.165, 0.84, 0.44, 1);
            }
            
            /* Hover Interaction: Reveal true colors */
            #awwwards-hero:hover .marquee-content img {
                filter: grayscale(0%) contrast(1) brightness(1);
            }

            .marquee-left {
                animation: scrollL 35s linear infinite;
            }
            .marquee-right {
                animation: scrollR 40s linear infinite;
            }

            @keyframes scrollL {
                0% { transform: translateX(0); }
                100% { transform: translateX(calc(-50% - 1vw)); }
            }
            @keyframes scrollR {
                0% { transform: translateX(calc(-50% - 1vw)); }
                100% { transform: translateX(0); }
            }

            /* Scroll Button Hover */
            .hero-scroll-btn:hover {
                transform: scale(1.05);
                background: #8C2DF6 !important;
                border-color: #8C2DF6 !important;
                box-shadow: 0 10px 30px rgba(140, 45, 246, 0.5);
            }

            /* Mobile Responsiveness */
            @media (max-width: 768px) {
                .hero-blend-text h1:first-of-type { font-size: 20vw; }
                .hero-blend-text h1:last-of-type { font-size: 20vw; margin-top: 0; }
                .marquee-content img { width: 45vw; height: 25vh; }
                .diagonal-gallery { width: 250vw; height: 150vh; left: -50%; }
                .hero-scroll-btn { width: 80px; height: 80px; font-size: 0.6rem; bottom: 2vh; right: 5vw; }
            }
        </style>
    </section>'''

# Regex to replace the hero
pattern = re.compile(r'<!-- Another Universe UI-UX-PRO-MAX Hero -->.*?</section>', re.DOTALL)
new_content = pattern.sub(new_hero, content, count=1)

with open('index.html', 'w', encoding='windows-1252') as f:
    f.write(new_content)

print("10/10 Hero Updated!")
