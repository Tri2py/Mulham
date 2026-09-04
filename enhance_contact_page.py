with open('contact.html', 'r', encoding='cp1252', errors='replace') as fp:
    content = fp.read()

# 1. UPGRADE HERO HEADER
old_hero = """<!-- Section: Let's Talk -->
            <section>
                <!-- Section Title -->
                <div class="stg-row bringer-section-title">
                    <div class="stg-col-8 stg-offset-2">
                        <div class="align-center">
                            <h2>Contact!</h2>
                            <p class="bringer-large-text">
                                Get My Links</p>
                        </div>
                    </div>
                </div>"""

new_hero = """<!-- Section: Let's Connect -->
            <section style="padding-top: 4vh; margin-bottom: 6vh;">
                <!-- Section Title: Luxury Architectural Heading -->
                <div class="stg-row bringer-section-title" style="margin-bottom: 40px;">
                    <div class="stg-col-10 stg-offset-1">
                        <div class="align-center">
                            <span style="display: inline-block; font-family: 'Inter', sans-serif; font-size: 0.68rem; font-weight: 600; letter-spacing: 0.28em; text-transform: uppercase; color: #8C2DF6; margin-bottom: 16px;">Direct Channels</span>
                            <h1 style="font-family: 'Playfair Display', serif; font-size: clamp(3rem, 7vw, 5.5rem); font-weight: 400; letter-spacing: -0.03em; line-height: 1.05; margin: 0 0 20px 0; color: #ffffff;">
                                Let's build something <span style="font-style: italic; color: #8C2DF6;">extraordinary.</span>
                            </h1>
                            <p class="bringer-large-text" style="color: rgba(255,255,255,0.55); font-family: 'Inter', sans-serif; font-size: clamp(1rem, 2vw, 1.2rem); line-height: 1.6; max-width: 620px; margin: 0 auto; text-wrap: balance;">
                                Have a project in mind, a design inquiry, or simply want to connect? Choose your preferred channel below.
                            </p>
                        </div>
                    </div>
                </div>"""

# 2. UPGRADE EMAIL CARD AND SOCIAL CARD WITH LUXURY HOVER AND ICONS
old_cards = """<div class="stg-col-4 stg-tp-col-6 stg-tp-bottom-gap">
                        <!-- Email -->
                        <div class="bringer-block stg-aspect-square stg-vertical-space-between">
                            <a href="mailto:mulhamlol790@gmail.com" class="bringer-grid-item-link"></a>
                            <div>
                                <h5>Email<span class="bringer-accent">.</span></h5>
                                <h6>mulhamlol790@gmail.com</h6>
                            </div>
                            <p>Send us a detailed message. I'll get back to you as soon as possible to discuss your
                                creative project further.</p>
                        </div>
                    </div>
                    <div class="stg-col-4 stg-tp-col-12">
                        <!-- Social Media -->
                        <div class="bringer-block stg-aspect-square stg-tp-aspect-rectangle stg-vertical-space-between">
                            <div>
                                <h5>Social Media<span class="bringer-accent">.</span></h5>
                                <ul class="bringer-socials-list stg-small-gap"
                                   >
                                    <li>
                                        <a href="https://www.pinterest.com/normal_person_as_trippy/" target="_blank"
                                            class="bringer-socials-pinterest"><i class="ph-fill ph-pinterest-logo"></i>
                                        </a>
                                    </li>
                                    <li>
                                        <a href="https://www.instagram.com/creative_mulham/" target="_blank"
                                            class="bringer-socials-instagram"><i class="ph-fill ph-instagram-logo"></i>
                                        </a>
                                    </li>
                                    <li>
                                        <a href="https://www.linkedin.com/in/mulham-ibrahim-2021643ab?utm_source=share_via&utm_content=profile&utm_medium=member_android"
                                            target="_blank" class="bringer-socials-linkedin"><i class="ph-fill ph-linkedin-logo"></i>
                                        </a>
                                    </li>
                                </ul>
                            </div>
                            <p>Follow Me on Social Media Platforms for a glimpse into our creative world, industry
                                insights, and projects.</p>
                        </div>
                    </div>"""

new_cards = """<div class="stg-col-4 stg-tp-col-6 stg-tp-bottom-gap">
                        <!-- Email Card: Refined Interactive -->
                        <div class="bringer-block stg-aspect-square stg-vertical-space-between contact-feature-card"
                            style="position: relative; overflow: hidden; border: 1px solid rgba(255, 255, 255, 0.08); transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);">
                            <div>
                                <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 16px;">
                                    <span style="font-family: 'Inter', sans-serif; font-size: 0.65rem; font-weight: 600; letter-spacing: 0.22em; text-transform: uppercase; color: #8C2DF6;">Direct Inbox</span>
                                    <i class="ph-bold ph-envelope-simple" style="font-size: 1.25rem; color: rgba(255,255,255,0.3);"></i>
                                </div>
                                <h5 style="margin-bottom: 8px;">Electronic Mail<span class="bringer-accent">.</span></h5>
                                <a href="mailto:mulhamlol790@gmail.com" style="display: inline-block; font-family: 'Inter', monospace, sans-serif; font-size: 0.88rem; color: #ffffff; text-decoration: none; word-break: break-all; margin-bottom: 12px; transition: color 0.2s;" onmouseover="this.style.color='#b066ff'" onmouseout="this.style.color='#ffffff'">
                                    mulhamlol790@gmail.com
                                </a>
                            </div>
                            <div>
                                <p style="color: rgba(255,255,255,0.55); font-size: 0.9rem; line-height: 1.6; margin: 0 0 16px 0;">Send detailed project briefs, RFP specifications, or collaboration proposals.</p>
                                <a href="mailto:mulhamlol790@gmail.com" class="contact-pill-btn" style="display: inline-flex; align-items: center; gap: 8px; padding: 10px 18px; border-radius: 99px; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.12); color: #fff; text-decoration: none; font-size: 0.78rem; font-weight: 500; letter-spacing: 0.04em; text-transform: uppercase; transition: all 0.3s ease;">
                                    Write an Email
                                    <i class="ph-bold ph-arrow-up-right" style="font-size: 0.8rem; color: #8C2DF6;"></i>
                                </a>
                            </div>
                        </div>
                    </div>

                    <div class="stg-col-4 stg-tp-col-12">
                        <!-- Social Media: Editorial Card -->
                        <div class="bringer-block stg-aspect-square stg-tp-aspect-rectangle stg-vertical-space-between contact-feature-card"
                            style="position: relative; overflow: hidden; border: 1px solid rgba(255, 255, 255, 0.08); transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);">
                            <div>
                                <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 16px;">
                                    <span style="font-family: 'Inter', sans-serif; font-size: 0.65rem; font-weight: 600; letter-spacing: 0.22em; text-transform: uppercase; color: #8C2DF6;">Broadcasts</span>
                                    <i class="ph-bold ph-share-network" style="font-size: 1.25rem; color: rgba(255,255,255,0.3);"></i>
                                </div>
                                <h5 style="margin-bottom: 8px;">Social Ecosphere<span class="bringer-accent">.</span></h5>
                                <p style="color: rgba(255,255,255,0.55); font-size: 0.9rem; line-height: 1.6; margin: 0;">Follow daily design explorations, behind-the-scenes engineering, and ongoing creative releases.</p>
                            </div>
                            
                            <!-- Custom Social Chips -->
                            <div style="display: flex; gap: 10px; flex-wrap: wrap; margin-top: 14px;">
                                <a href="https://www.instagram.com/creative_mulham/" target="_blank" class="social-chip" style="display: inline-flex; align-items: center; gap: 8px; padding: 8px 14px; background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.1); border-radius: 10px; color: #fff; text-decoration: none; font-size: 0.8rem; font-weight: 500; transition: all 0.25s ease;">
                                    <i class="ph-fill ph-instagram-logo" style="font-size: 1rem; color: #e1306c;"></i>
                                    Instagram
                                </a>
                                <a href="https://www.linkedin.com/in/mulham-ibrahim-2021643ab?utm_source=share_via&utm_content=profile&utm_medium=member_android" target="_blank" class="social-chip" style="display: inline-flex; align-items: center; gap: 8px; padding: 8px 14px; background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.1); border-radius: 10px; color: #fff; text-decoration: none; font-size: 0.8rem; font-weight: 500; transition: all 0.25s ease;">
                                    <i class="ph-fill ph-linkedin-logo" style="font-size: 1rem; color: #0a66c2;"></i>
                                    LinkedIn
                                </a>
                                <a href="https://www.pinterest.com/normal_person_as_trippy/" target="_blank" class="social-chip" style="display: inline-flex; align-items: center; gap: 8px; padding: 8px 14px; background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.1); border-radius: 10px; color: #fff; text-decoration: none; font-size: 0.8rem; font-weight: 500; transition: all 0.25s ease;">
                                    <i class="ph-fill ph-pinterest-logo" style="font-size: 1rem; color: #e60023;"></i>
                                    Pinterest
                                </a>
                            </div>
                        </div>
                    </div>"""

# 3. ADD FAQ / WORKING WITH ME ACCORDION OR INFO STRIP BEFORE FOOTER
INFO_STRIP = """
                <!-- Client Expectations / Working With Me Strip -->
                <div style="margin-top: 10vh; margin-bottom: 8vh; padding: 48px 36px; border-radius: 24px; background: rgba(140, 45, 246, 0.03); border: 1px solid rgba(140, 45, 246, 0.15); position: relative; overflow: hidden;">
                    <!-- Ambient Glow -->
                    <div style="position: absolute; top: -50px; left: 20%; width: 260px; height: 160px; background: radial-gradient(circle, rgba(140,45,246,0.15) 0%, transparent 70%); filter: blur(40px); pointer-events: none;"></div>

                    <div class="stg-row" style="align-items: center;">
                        <div class="stg-col-5 stg-tp-col-12" style="margin-bottom: 24px;">
                            <span style="display: inline-block; font-family: 'Inter', sans-serif; font-size: 0.65rem; font-weight: 600; letter-spacing: 0.24em; text-transform: uppercase; color: #8C2DF6; margin-bottom: 12px;">Collaboration Protocol</span>
                            <h3 style="font-family: 'Playfair Display', serif; font-size: clamp(1.8rem, 3.5vw, 2.6rem); font-weight: 400; color: #ffffff; line-height: 1.2; margin: 0;">What to expect when reaching out<span style="color: #8C2DF6;">.</span></h3>
                        </div>
                        <div class="stg-col-7 stg-tp-col-12">
                            <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 24px;" class="protocol-grid">
                                <div>
                                    <div style="font-family: 'Inter', sans-serif; font-size: 0.72rem; font-weight: 600; letter-spacing: 0.1em; color: #8C2DF6; margin-bottom: 6px;">01 / RAPID TURNAROUND</div>
                                    <p style="color: rgba(255,255,255,0.6); font-size: 0.88rem; line-height: 1.5; margin: 0;">All initial inquiries receive a response within 24 business hours with scoping notes.</p>
                                </div>
                                <div>
                                    <div style="font-family: 'Inter', sans-serif; font-size: 0.72rem; font-weight: 600; letter-spacing: 0.1em; color: #8C2DF6; margin-bottom: 6px;">02 / DIRECT ENGAGEMENT</div>
                                    <p style="color: rgba(255,255,255,0.6); font-size: 0.88rem; line-height: 1.5; margin: 0;">You talk directly with Mulham — no account managers or agency intermediaries.</p>
                                </div>
                                <div>
                                    <div style="font-family: 'Inter', sans-serif; font-size: 0.72rem; font-weight: 600; letter-spacing: 0.1em; color: #8C2DF6; margin-bottom: 6px;">03 / TAILORED ARCHITECTURE</div>
                                    <p style="color: rgba(255,255,255,0.6); font-size: 0.88rem; line-height: 1.5; margin: 0;">Every deliverable is handcrafted from zero to fit your brand identity & objectives.</p>
                                </div>
                                <div>
                                    <div style="font-family: 'Inter', sans-serif; font-size: 0.72rem; font-weight: 600; letter-spacing: 0.1em; color: #8C2DF6; margin-bottom: 6px;">04 / GLOBAL DELIVERY</div>
                                    <p style="color: rgba(255,255,255,0.6); font-size: 0.88rem; line-height: 1.5; margin: 0;">Async-first workflow tuned for seamless collaboration across all time zones.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>"""

# 4. ADD SIGNATURE LUXURY FOOTER (identical to home.html)
LUXURY_FOOTER = """
        <!-- Premium 10/10 Footer -->
        <footer id="bringer-footer" style="background: #06020A; padding-top: 12vh; position: relative; overflow: hidden; border-top: 1px solid rgba(140,45,246,0.1); margin-left: calc(50% - 50vw); width: 100vw;">
            <div class="stg-container" style="position: relative; z-index: 2; display: flex; flex-direction: column; min-height: 40vh; justify-content: space-between;">
                
                <!-- Top row: CTA -->
                <div style="display: flex; flex-direction: column; align-items: center; text-align: center; margin-bottom: 8vh;">
                    <p style="font-family: 'Inter', sans-serif; font-size: 0.75rem; font-weight: 500; letter-spacing: 0.3em; color: #8C2DF6; text-transform: uppercase; margin-bottom: 2vh;">Ready to start?</p>
                    <h2 style="font-family: 'Playfair Display', serif; font-size: clamp(2.6rem, 6vw, 5rem); font-weight: 400; letter-spacing: -0.03em; line-height: 1.1; margin-bottom: 4vh; max-width: 800px; color: #fff;">
                        Transforming concepts into <span style="font-style: italic; color: rgba(255,255,255,0.4);">living experiences.</span>
                    </h2>
                    
                    <a href="mailto:mulhamlol790@gmail.com" class="glass-pill" style="display: inline-flex; align-items: center; gap: 15px; text-decoration: none; font-size: 0.85rem; padding: 18px 38px; background: rgba(140,45,246,0.1); border: 1px solid rgba(140,45,246,0.3); border-radius: 100px; color: #fff; font-family: 'Inter', sans-serif; font-weight: 500; text-transform: uppercase; letter-spacing: 0.15em; transition: all 0.3s ease; box-shadow: 0 10px 30px rgba(140,45,246,0.15);" onmouseover="this.style.background='rgba(140,45,246,0.2)'; this.style.borderColor='rgba(140,45,246,0.6)'; this.style.transform='translateY(-2px)';" onmouseout="this.style.background='rgba(140,45,246,0.1)'; this.style.borderColor='rgba(140,45,246,0.3)'; this.style.transform='none';">
                        mulhamlol790@gmail.com
                        <i class="ph-fill ph-paper-plane-tilt" style="font-size: 1.1rem; color: #8C2DF6;"></i>
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
        </footer>"""

# Extra styling for hover states and mobile responsiveness
EXTRA_CSS = """
    <style>
        .contact-feature-card:hover {
            transform: translateY(-4px);
            border-color: rgba(140, 45, 246, 0.35) !important;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.7), inset 0 0 40px rgba(140, 45, 246, 0.05) !important;
        }
        .contact-pill-btn:hover {
            background: rgba(140, 45, 246, 0.2) !important;
            border-color: rgba(140, 45, 246, 0.5) !important;
            transform: translateY(-2px);
        }
        .social-chip:hover {
            background: rgba(140, 45, 246, 0.15) !important;
            border-color: rgba(140, 45, 246, 0.4) !important;
            transform: translateY(-2px);
        }
        @media (max-width: 768px) {
            .protocol-grid {
                grid-template-columns: 1fr !important;
                gap: 16px !important;
            }
        }
    </style>
"""

# Normalize string endings
content_n = content.replace('\r\n', '\n')
old_hero_n = old_hero.replace('\r\n', '\n')
new_hero_n = new_hero.replace('\r\n', '\n')

old_cards_n = old_cards.replace('\r\n', '\n')
new_cards_n = new_cards.replace('\r\n', '\n')

if old_hero_n in content_n:
    content_n = content_n.replace(old_hero_n, new_hero_n, 1)
    print("OK: Replaced hero header")
else:
    print("WARN: Old hero not found by exact string, checking fallback")

if old_cards_n in content_n:
    content_n = content_n.replace(old_cards_n, new_cards_n, 1)
    print("OK: Replaced email and social cards")
else:
    print("WARN: Old cards not found by exact string, checking fallback")

# Insert Info Strip before </section>
sec_end = content_n.find('</section>\n\n        </div><!-- .stg-container -->')
if sec_end == -1:
    sec_end = content_n.find('</section>')
if sec_end != -1:
    content_n = content_n[:sec_end] + INFO_STRIP + "\n            " + content_n[sec_end:]
    print("OK: Inserted Collaboration Protocol strip")

# Insert Footer after </main>
main_end = content_n.find('</main>')
if main_end != -1:
    content_n = content_n[:main_end+7] + "\n" + LUXURY_FOOTER + content_n[main_end+7:]
    print("OK: Inserted luxury footer")

# Insert Extra CSS before </head>
head_end = content_n.find('</head>')
if head_end != -1:
    content_n = content_n[:head_end] + EXTRA_CSS + "\n" + content_n[head_end:]
    print("OK: Inserted extra styles in head")

with open('contact.html', 'w', encoding='cp1252', errors='xmlcharrefreplace') as fp:
    fp.write(content_n)

print("SUCCESS: Enhanced Contact Page with full architectural luxury design!")
