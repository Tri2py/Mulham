with open('contact.html', 'r', encoding='cp1252', errors='replace') as fp:
    content = fp.read()

# 1. Update the Contact Grid cards classes and markup for responsive elegance
old_grid = """                <!-- Contacts Grid -->
                <div class="stg-row">
                    <div class="stg-col-4 stg-tp-col-6 stg-tp-bottom-gap">
                        <!-- Direct Line / Availability Card -->
                        <div class="bringer-block stg-aspect-square stg-vertical-space-between direct-line-card"
                            style="position: relative; overflow: hidden; border: 1px solid rgba(140, 45, 246, 0.22); box-shadow: 0 20px 50px rgba(0,0,0,0.6), inset 0 0 35px rgba(140, 45, 246, 0.06); transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);">
                            
                            <!-- Ambient Background Pulse Glow -->
                            <div style="position: absolute; -webkit-mask-image: radial-gradient(circle, rgba(0,0,0,1) 0%, rgba(0,0,0,0) 70%); mask-image: radial-gradient(circle, rgba(0,0,0,1) 0%, rgba(0,0,0,0) 70%); top: -40px; right: -40px; width: 180px; height: 180px; background: radial-gradient(circle, rgba(140,45,246,0.3) 0%, transparent 70%); filter: blur(25px); pointer-events: none;"></div>

                            <div>
                                <!-- Top Tag -->
                                <div style="display: flex; align-items: center; margin-bottom: 16px;">
                                    <span style="font-family: 'Inter', sans-serif; font-size: 0.65rem; font-weight: 600; letter-spacing: 0.22em; text-transform: uppercase; color: #8C2DF6;">Direct Line</span>
                                </div>
                                
                                <h5 style="margin-bottom: 8px;">Studio Status<span class="bringer-accent">.</span></h5>
                                <p style="color: rgba(255,255,255,0.6); font-size: 0.92rem; line-height: 1.6; margin: 0;">Accepting select commissions for digital experiences, brand architecture, and bespoke web design.</p>
                            </div>

                            <!-- Interactive Quick Action Buttons -->
                            <div style="display: flex; flex-direction: column; gap: 10px; margin-top: 18px; position: relative; z-index: 2;">
                                <!-- Primary Action: Send Inquiry via Email -->
                                <a href="mailto:mulhamlol790@gmail.com?subject=Project%20Inquiry%20-%20Mulham%20Studio"
                                   style="display: flex; align-items: center; justify-content: space-between; padding: 13px 18px; background: linear-gradient(135deg, rgba(140,45,246,0.3) 0%, rgba(140,45,246,0.12) 100%); border: 1px solid rgba(140,45,246,0.45); border-radius: 12px; color: #ffffff; text-decoration: none; font-family: 'Inter', sans-serif; font-size: 0.84rem; font-weight: 600; letter-spacing: 0.02em; transition: all 0.3s ease; box-shadow: 0 6px 20px rgba(140,45,246,0.18);"
                                   onmouseover="this.style.transform='translateY(-2px)'; this.style.borderColor='rgba(140,45,246,0.8)'; this.style.boxShadow='0 10px 25px rgba(140,45,246,0.35)';"
                                   onmouseout="this.style.transform='none'; this.style.borderColor='rgba(140,45,246,0.45)'; this.style.boxShadow='0 6px 20px rgba(140,45,246,0.18)';">
                                    <span style="display: flex; align-items: center; gap: 10px;">
                                        <i class="ph-fill ph-paper-plane-tilt" style="font-size: 1.1rem; color: #b066ff;"></i>
                                        Send Project Inquiry
                                    </span>
                                    <i class="ph-bold ph-arrow-up-right" style="font-size: 0.9rem; color: rgba(255,255,255,0.7);"></i>
                                </a>

                                <!-- Secondary Action: Instant Telegram / Chat link -->
                                <button onclick="copyEmailAddress(this)"
                                        style="display: flex; align-items: center; justify-content: space-between; padding: 11px 18px; background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.09); border-radius: 12px; color: rgba(255,255,255,0.75); font-family: 'Inter', sans-serif; font-size: 0.8rem; font-weight: 500; cursor: pointer; transition: all 0.25s ease;"
                                        onmouseover="this.style.background='rgba(255,255,255,0.08)'; this.style.borderColor='rgba(255,255,255,0.2)'; this.style.color='#fff';"
                                        onmouseout="this.style.background='rgba(255,255,255,0.04)'; this.style.borderColor='rgba(255,255,255,0.09)'; this.style.color='rgba(255,255,255,0.75)';">
                                    <span style="display: flex; align-items: center; gap: 9px;">
                                        <i class="ph-fill ph-copy" style="font-size: 1rem; color: #8C2DF6;"></i>
                                        <span class="copy-label">Copy Direct Email</span>
                                    </span>
                                    <span style="font-size: 0.72rem; color: rgba(255,255,255,0.35); font-family: monospace;">1-CLICK</span>
                                </button>
                            </div>
                        </div>
                    </div>
                    <div class="stg-col-4 stg-tp-col-6 stg-tp-bottom-gap">
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
                            
                            <!-- Custom Social Phosphor Cards / Chips -->
                            <div style="display: flex; gap: 10px; flex-wrap: wrap; margin-top: 16px;">
                                <!-- Instagram -->
                                <a href="https://www.instagram.com/creative_mulham/" target="_blank" class="social-chip" style="display: inline-flex; align-items: center; gap: 9px; padding: 10px 16px; background: rgba(225, 48, 108, 0.08); border: 1px solid rgba(225, 48, 108, 0.25); border-radius: 12px; color: #ffffff; text-decoration: none; font-family: 'Inter', sans-serif; font-size: 0.82rem; font-weight: 500; transition: all 0.3s ease;">
                                    <i class="ph-fill ph-instagram-logo" style="font-size: 1.2rem; color: #f04276; display: inline-block; vertical-align: middle;"></i>
                                    <span>Instagram</span>
                                    <i class="ph-bold ph-arrow-up-right" style="font-size: 0.75rem; color: rgba(255,255,255,0.4); margin-left: 2px;"></i>
                                </a>
                                
                                <!-- LinkedIn -->
                                <a href="https://www.linkedin.com/in/mulham-ibrahim-2021643ab?utm_source=share_via&utm_content=profile&utm_medium=member_android" target="_blank" class="social-chip" style="display: inline-flex; align-items: center; gap: 9px; padding: 10px 16px; background: rgba(10, 102, 194, 0.08); border: 1px solid rgba(10, 102, 194, 0.25); border-radius: 12px; color: #ffffff; text-decoration: none; font-family: 'Inter', sans-serif; font-size: 0.82rem; font-weight: 500; transition: all 0.3s ease;">
                                    <i class="ph-fill ph-linkedin-logo" style="font-size: 1.2rem; color: #2884e0; display: inline-block; vertical-align: middle;"></i>
                                    <span>LinkedIn</span>
                                    <i class="ph-bold ph-arrow-up-right" style="font-size: 0.75rem; color: rgba(255,255,255,0.4); margin-left: 2px;"></i>
                                </a>
                                
                                <!-- Pinterest -->
                                <a href="https://www.pinterest.com/normal_person_as_trippy/" target="_blank" class="social-chip" style="display: inline-flex; align-items: center; gap: 9px; padding: 10px 16px; background: rgba(230, 0, 35, 0.08); border: 1px solid rgba(230, 0, 35, 0.25); border-radius: 12px; color: #ffffff; text-decoration: none; font-family: 'Inter', sans-serif; font-size: 0.82rem; font-weight: 500; transition: all 0.3s ease;">
                                    <i class="ph-fill ph-pinterest-logo" style="font-size: 1.2rem; color: #ff334b; display: inline-block; vertical-align: middle;"></i>
                                    <span>Pinterest</span>
                                    <i class="ph-bold ph-arrow-up-right" style="font-size: 0.75rem; color: rgba(255,255,255,0.4); margin-left: 2px;"></i>
                                </a>
                            </div>
                        </div>
                    </div>
                </div>"""

new_grid = """                <!-- Contacts Grid: Adaptive Mobile & Tablet Flow -->
                <div class="stg-row contact-main-grid">
                    <div class="stg-col-4 stg-tp-col-6 stg-m-col-12 stg-tp-bottom-gap">
                        <!-- Direct Line Card -->
                        <div class="bringer-block stg-aspect-square stg-vertical-space-between direct-line-card contact-card-inner"
                            style="position: relative; overflow: hidden; border: 1px solid rgba(140, 45, 246, 0.22); box-shadow: 0 20px 50px rgba(0,0,0,0.6), inset 0 0 35px rgba(140, 45, 246, 0.06); transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);">
                            
                            <!-- Ambient Background Pulse Glow -->
                            <div style="position: absolute; -webkit-mask-image: radial-gradient(circle, rgba(0,0,0,1) 0%, rgba(0,0,0,0) 70%); mask-image: radial-gradient(circle, rgba(0,0,0,1) 0%, rgba(0,0,0,0) 70%); top: -40px; right: -40px; width: 180px; height: 180px; background: radial-gradient(circle, rgba(140,45,246,0.3) 0%, transparent 70%); filter: blur(25px); pointer-events: none;"></div>

                            <div>
                                <!-- Top Tag -->
                                <div style="display: flex; align-items: center; margin-bottom: 16px;">
                                    <span style="font-family: 'Inter', sans-serif; font-size: 0.65rem; font-weight: 600; letter-spacing: 0.22em; text-transform: uppercase; color: #8C2DF6;">Direct Line</span>
                                </div>
                                
                                <h5 style="margin-bottom: 8px;">Studio Status<span class="bringer-accent">.</span></h5>
                                <p style="color: rgba(255,255,255,0.6); font-size: 0.92rem; line-height: 1.6; margin: 0;">Accepting select commissions for digital experiences, brand architecture, and bespoke web design.</p>
                            </div>

                            <!-- Interactive Quick Action Buttons -->
                            <div style="display: flex; flex-direction: column; gap: 10px; margin-top: 18px; position: relative; z-index: 2;">
                                <!-- Primary Action: Send Inquiry via Email -->
                                <a href="mailto:mulhamlol790@gmail.com?subject=Project%20Inquiry%20-%20Mulham%20Studio"
                                   class="inquiry-btn"
                                   style="display: flex; align-items: center; justify-content: space-between; padding: 13px 18px; background: linear-gradient(135deg, rgba(140,45,246,0.3) 0%, rgba(140,45,246,0.12) 100%); border: 1px solid rgba(140,45,246,0.45); border-radius: 12px; color: #ffffff; text-decoration: none; font-family: 'Inter', sans-serif; font-size: 0.84rem; font-weight: 600; letter-spacing: 0.02em; transition: all 0.3s ease; box-shadow: 0 6px 20px rgba(140,45,246,0.18);">
                                    <span style="display: flex; align-items: center; gap: 10px;">
                                        <i class="ph-fill ph-paper-plane-tilt" style="font-size: 1.1rem; color: #b066ff;"></i>
                                        Send Project Inquiry
                                    </span>
                                    <i class="ph-bold ph-arrow-up-right" style="font-size: 0.9rem; color: rgba(255,255,255,0.7);"></i>
                                </a>

                                <!-- Secondary Action: Instant Email Copy button -->
                                <button onclick="copyEmailAddress(this)"
                                        class="copy-btn"
                                        style="display: flex; align-items: center; justify-content: space-between; padding: 11px 18px; background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.09); border-radius: 12px; color: rgba(255,255,255,0.75); font-family: 'Inter', sans-serif; font-size: 0.8rem; font-weight: 500; cursor: pointer; transition: all 0.25s ease;">
                                    <span style="display: flex; align-items: center; gap: 9px;">
                                        <i class="ph-fill ph-copy" style="font-size: 1rem; color: #8C2DF6;"></i>
                                        <span class="copy-label">Copy Direct Email</span>
                                    </span>
                                    <span style="font-size: 0.72rem; color: rgba(255,255,255,0.35); font-family: monospace;">1-CLICK</span>
                                </button>
                            </div>
                        </div>
                    </div>
                    
                    <div class="stg-col-4 stg-tp-col-6 stg-m-col-12 stg-tp-bottom-gap">
                        <!-- Email Card -->
                        <div class="bringer-block stg-aspect-square stg-vertical-space-between contact-feature-card contact-card-inner"
                            style="position: relative; overflow: hidden; border: 1px solid rgba(255, 255, 255, 0.08); transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);">
                            <div>
                                <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 16px;">
                                    <span style="font-family: 'Inter', sans-serif; font-size: 0.65rem; font-weight: 600; letter-spacing: 0.22em; text-transform: uppercase; color: #8C2DF6;">Direct Inbox</span>
                                    <i class="ph-bold ph-envelope-simple" style="font-size: 1.25rem; color: rgba(255,255,255,0.3);"></i>
                                </div>
                                <h5 style="margin-bottom: 8px;">Electronic Mail<span class="bringer-accent">.</span></h5>
                                <a href="mailto:mulhamlol790@gmail.com" class="email-address-link" style="display: inline-block; font-family: 'Inter', monospace, sans-serif; font-size: 0.88rem; color: #ffffff; text-decoration: none; word-break: break-all; margin-bottom: 12px; transition: color 0.2s;">
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

                    <div class="stg-col-4 stg-tp-col-12 stg-m-col-12">
                        <!-- Social Media Card -->
                        <div class="bringer-block stg-aspect-square stg-tp-aspect-rectangle stg-vertical-space-between contact-feature-card contact-card-inner"
                            style="position: relative; overflow: hidden; border: 1px solid rgba(255, 255, 255, 0.08); transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);">
                            <div>
                                <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 16px;">
                                    <span style="font-family: 'Inter', sans-serif; font-size: 0.65rem; font-weight: 600; letter-spacing: 0.22em; text-transform: uppercase; color: #8C2DF6;">Broadcasts</span>
                                    <i class="ph-bold ph-share-network" style="font-size: 1.25rem; color: rgba(255,255,255,0.3);"></i>
                                </div>
                                <h5 style="margin-bottom: 8px;">Social Ecosphere<span class="bringer-accent">.</span></h5>
                                <p style="color: rgba(255,255,255,0.55); font-size: 0.9rem; line-height: 1.6; margin: 0;">Follow daily design explorations, behind-the-scenes engineering, and ongoing creative releases.</p>
                            </div>
                            
                            <!-- Custom Social Phosphor Chips -->
                            <div class="social-chips-wrap" style="display: flex; gap: 10px; flex-wrap: wrap; margin-top: 16px;">
                                <!-- Instagram -->
                                <a href="https://www.instagram.com/creative_mulham/" target="_blank" class="social-chip" style="display: inline-flex; align-items: center; gap: 9px; padding: 10px 16px; background: rgba(225, 48, 108, 0.08); border: 1px solid rgba(225, 48, 108, 0.25); border-radius: 12px; color: #ffffff; text-decoration: none; font-family: 'Inter', sans-serif; font-size: 0.82rem; font-weight: 500; transition: all 0.3s ease;">
                                    <i class="ph-fill ph-instagram-logo" style="font-size: 1.2rem; color: #f04276; display: inline-block; vertical-align: middle;"></i>
                                    <span>Instagram</span>
                                    <i class="ph-bold ph-arrow-up-right" style="font-size: 0.75rem; color: rgba(255,255,255,0.4); margin-left: 2px;"></i>
                                </a>
                                
                                <!-- LinkedIn -->
                                <a href="https://www.linkedin.com/in/mulham-ibrahim-2021643ab?utm_source=share_via&utm_content=profile&utm_medium=member_android" target="_blank" class="social-chip" style="display: inline-flex; align-items: center; gap: 9px; padding: 10px 16px; background: rgba(10, 102, 194, 0.08); border: 1px solid rgba(10, 102, 194, 0.25); border-radius: 12px; color: #ffffff; text-decoration: none; font-family: 'Inter', sans-serif; font-size: 0.82rem; font-weight: 500; transition: all 0.3s ease;">
                                    <i class="ph-fill ph-linkedin-logo" style="font-size: 1.2rem; color: #2884e0; display: inline-block; vertical-align: middle;"></i>
                                    <span>LinkedIn</span>
                                    <i class="ph-bold ph-arrow-up-right" style="font-size: 0.75rem; color: rgba(255,255,255,0.4); margin-left: 2px;"></i>
                                </a>
                                
                                <!-- Pinterest -->
                                <a href="https://www.pinterest.com/normal_person_as_trippy/" target="_blank" class="social-chip" style="display: inline-flex; align-items: center; gap: 9px; padding: 10px 16px; background: rgba(230, 0, 35, 0.08); border: 1px solid rgba(230, 0, 35, 0.25); border-radius: 12px; color: #ffffff; text-decoration: none; font-family: 'Inter', sans-serif; font-size: 0.82rem; font-weight: 500; transition: all 0.3s ease;">
                                    <i class="ph-fill ph-pinterest-logo" style="font-size: 1.2rem; color: #ff334b; display: inline-block; vertical-align: middle;"></i>
                                    <span>Pinterest</span>
                                    <i class="ph-bold ph-arrow-up-right" style="font-size: 0.75rem; color: rgba(255,255,255,0.4); margin-left: 2px;"></i>
                                </a>
                            </div>
                        </div>
                    </div>
                </div>"""

content_norm = content.replace('\r\n', '\n')
old_grid_norm = old_grid.replace('\r\n', '\n')
new_grid_norm = new_grid.replace('\r\n', '\n')

if old_grid_norm in content_norm:
    content_norm = content_norm.replace(old_grid_norm, new_grid_norm, 1)
    print("OK: Replaced contacts grid with responsive mobile classes")
else:
    print("WARN: Old grid not matched directly")

# 2. Comprehensive Mobile Styling to fix padding, aspect ratios, wrapping, fonts, and footer on phones
COMPREHENSIVE_MOBILE_CSS = """
    <!-- Mobile & Responsive Refinements -->
    <style>
        /* Base touch & layout stability */
        html, body {
            overflow-x: hidden !important;
            max-width: 100vw;
        }

        /* Hover states for desktop */
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
        .protocol-card {
            background: rgba(14, 8, 20, 0.6) !important;
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.5), inset 0 0 25px rgba(140, 45, 246, 0.03);
        }
        .protocol-card:hover {
            transform: translateY(-5px);
            border-color: rgba(140, 45, 246, 0.45) !important;
            box-shadow: 0 25px 60px rgba(140, 45, 246, 0.12), inset 0 0 35px rgba(140, 45, 246, 0.08) !important;
        }

        /* Tablet Responsive (<= 1024px) */
        @media (max-width: 1024px) {
            .protocol-cards-grid {
                grid-template-columns: repeat(2, 1fr) !important;
                gap: 16px !important;
            }
        }

        /* Mobile View (<= 768px) */
        @media (max-width: 768px) {
            /* Fix container side padding so nothing clips */
            .stg-container {
                padding-left: 20px !important;
                padding-right: 20px !important;
            }

            /* Remove rigid square aspect ratios so text never overflows */
            .contact-card-inner,
            .stg-aspect-square,
            .stg-tp-aspect-rectangle {
                aspect-ratio: auto !important;
                min-height: auto !important;
                padding: 28px 22px !important;
            }

            /* Spacing between vertical cards */
            .contact-main-grid > div {
                margin-bottom: 20px !important;
            }

            /* Buttons inside direct line card stretch comfortably */
            .inquiry-btn,
            .copy-btn {
                padding: 14px 18px !important;
                font-size: 0.86rem !important;
            }

            /* Social chips wrap cleanly in full rows or even blocks */
            .social-chips-wrap {
                gap: 8px !important;
            }
            .social-chip {
                flex: 1 1 calc(50% - 8px);
                justify-content: center;
                padding: 10px 12px !important;
            }

            /* Protocol grid stacked */
            .protocol-cards-grid {
                grid-template-columns: 1fr !important;
                gap: 14px !important;
            }
            .protocol-card {
                padding: 24px 20px !important;
            }

            /* Footer CTA sizing on mobile */
            #bringer-footer {
                padding-top: 8vh !important;
                padding-bottom: 4vh !important;
            }
            #bringer-footer h2 {
                font-size: 2.2rem !important;
                line-height: 1.15 !important;
            }
            #bringer-footer .glass-pill {
                padding: 14px 24px !important;
                font-size: 0.78rem !important;
                max-width: 90vw;
                justify-content: center;
            }

            /* Giant watermark typography hidden on narrow mobile to prevent scroll hitch */
            #bringer-footer > div:last-child {
                display: none !important;
            }
        }

        /* Small Phones (<= 480px) */
        @media (max-width: 480px) {
            .bringer-section-title h1 {
                font-size: 2.3rem !important;
            }
            .social-chip {
                flex: 1 1 100% !important;
            }
        }
    </style>
"""

# Replace previous extra CSS block with COMPREHENSIVE_MOBILE_CSS
idx_css = content_norm.find('<!-- Mobile & Responsive Refinements -->')
if idx_css == -1:
    idx_css = content_norm.find('<style>\n        .contact-feature-card:hover')
if idx_css == -1:
    idx_css = content_norm.find('</head>')
    content_norm = content_norm[:idx_css] + COMPREHENSIVE_MOBILE_CSS + content_norm[idx_css:]
else:
    end_css = content_norm.find('</head>', idx_css)
    content_norm = content_norm[:idx_css] + COMPREHENSIVE_MOBILE_CSS + content_norm[end_css:]

with open('contact.html', 'w', encoding='cp1252', errors='xmlcharrefreplace') as fp:
    fp.write(content_norm)

print("SUCCESS: Enhanced mobile responsive view for contact.html!")
