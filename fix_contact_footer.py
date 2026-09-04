with open('contact.html', 'r', encoding='cp1252', errors='replace') as fp:
    content = fp.read()

# 1. Replace the duplicated oversized footer with a clean, low-profile, unobtrusive studio footer
old_footer = """        <!-- Premium 10/10 Footer -->
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

new_footer = """        <!-- Minimalist Studio Footer -->
        <footer id="bringer-footer" class="contact-page-footer">
            <div class="stg-container">
                <div class="contact-footer-inner">
                    <div class="contact-footer-copy">
                        <span class="contact-footer-brand">MULHAM IBRAHIM</span> &copy; 2026. All rights reserved.
                    </div>
                    
                    <!-- Social Links -->
                    <ul class="contact-footer-socials">
                        <li><a href="https://www.instagram.com/creative_mulham/" target="_blank" aria-label="Instagram"><i class="ph-fill ph-instagram-logo"></i></a></li>
                        <li><a href="https://www.linkedin.com/in/mulham-ibrahim-2021643ab" target="_blank" aria-label="LinkedIn"><i class="ph-fill ph-linkedin-logo"></i></a></li>
                        <li><a href="https://www.pinterest.com/normal_person_as_trippy/" target="_blank" aria-label="Pinterest"><i class="ph-fill ph-pinterest-logo"></i></a></li>
                    </ul>
                </div>
            </div>
        </footer>"""

# 2. Add clean CSS for the contact footer
FOOTER_CSS = """
        /* Sleek & Low-Profile Contact Footer */
        .contact-page-footer {
            background: #06020A;
            border-top: 1px solid rgba(255, 255, 255, 0.06);
            padding: 36px 0 44px;
            margin-top: 6vh;
            position: relative;
            z-index: 5;
        }
        .contact-footer-inner {
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 16px;
        }
        .contact-footer-copy {
            font-family: 'Inter', sans-serif;
            font-size: 0.8rem;
            color: rgba(255, 255, 255, 0.4);
            letter-spacing: 0.03em;
        }
        .contact-footer-brand {
            color: #ffffff;
            font-weight: 600;
            letter-spacing: 0.1em;
        }
        .contact-footer-socials {
            margin: 0;
            padding: 0;
            display: flex;
            gap: 18px;
            list-style: none;
            align-items: center;
        }
        .contact-footer-socials a {
            color: rgba(255, 255, 255, 0.5);
            font-size: 1.15rem;
            text-decoration: none;
            transition: color 0.25s ease, transform 0.25s ease;
            display: inline-flex;
        }
        .contact-footer-socials a:hover {
            color: #8C2DF6;
            transform: translateY(-2px);
        }
        @media (max-width: 640px) {
            .contact-page-footer {
                padding: 28px 0 36px;
                margin-top: 4vh;
            }
            .contact-footer-inner {
                flex-direction: column;
                text-align: center;
                gap: 14px;
            }
            .contact-footer-socials {
                justify-content: center;
            }
        }
"""

content_norm = content.replace('\r\n', '\n')
old_footer_norm = old_footer.replace('\r\n', '\n')
new_footer_norm = new_footer.replace('\r\n', '\n')

if old_footer_norm in content_norm:
    content_norm = content_norm.replace(old_footer_norm, new_footer_norm, 1)
    print("OK: Replaced aggressive CTA footer with sleek studio footer")
else:
    print("WARN: Old footer not matched by exact block, trying tag replacement")
    start_f = content_norm.find('<footer id="bringer-footer"')
    end_f = content_norm.find('</footer>', start_f) + 9
    content_norm = content_norm[:start_f] + new_footer_norm + content_norm[end_f:]
    print("OK: Replaced footer via tags")

# Insert FOOTER_CSS before </style>\n</head>
idx_style = content_norm.find('</style>\n</head>')
if idx_style != -1:
    content_norm = content_norm[:idx_style] + FOOTER_CSS + content_norm[idx_style:]
    print("OK: Added footer CSS styles")

with open('contact.html', 'w', encoding='cp1252', errors='xmlcharrefreplace') as fp:
    fp.write(content_norm)

print("SUCCESS: Fixed contact page footer layout!")
