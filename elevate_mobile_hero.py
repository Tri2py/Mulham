with open('home.html', 'r', encoding='cp1252', errors='replace') as fp:
    content = fp.read()

old_hero_mq = """                        /* Responsive Overrides for Hero */
                        @media (max-width: 900px) {
                .hero-badge,
                .vertical-text,
                .glass-pill,
                .pill-1,
                .pill-2,
                .pill-3,
                #hero-particles,
                .hero-particle { 
                    display: none !important; 
                    opacity: 0 !important;
                    visibility: hidden !important;
                    animation: none !important;
                }
                .pill-3 { display: none !important; }

                .glass-pill {
                    font-size: 0.55rem !important;
                    padding: 6px 14px !important;
                }
                .pill-1 { top: 95px !important; left: 16px !important; }
                .pill-2 { top: 135px !important; right: 16px !important; }

                .hero-main-title { transform: translateY(-4vh) !important; }
                .hero-main-title h1 span { font-size: clamp(2.8rem, 14vw, 4.5rem) !important; }
                .hero-main-title h1 span:last-child { margin-top: -2vw !important; }
                .hero-main-title > div:first-child { font-size: 0.6rem !important; margin-bottom: 2vh !important; }
                .hero-main-title > div:last-child { font-size: 0.65rem !important; margin-top: 2vh !important; }

                .hero-desc {
                    display: block !important;
                    position: absolute !important;
                    bottom: 16vh !important;
                    left: 20px !important;
                    right: 20px !important;
                    max-width: 320px !important;
                    margin: 0 auto !important;
                    text-align: center !important;
                    border-left: none !important;
                    border-top: 1px solid rgba(140, 45, 246, 0.4) !important;
                    padding: 12px 10px 0 !important;
                }
                .hero-desc p { font-size: 0.75rem !important; line-height: 1.5 !important; }

                .hero-scroll-btn {
                    position: absolute !important;
                    width: 64px !important;
                    height: 64px !important;
                    bottom: 4vh !important;
                    left: 50% !important;
                    right: auto !important;
                    transform: translateX(-50%) !important;
                    font-size: 0.52rem !important;
                    backdrop-filter: none !important;
                    -webkit-backdrop-filter: none !important;
                    background: rgba(140, 45, 246, 0.9) !important;
                    border: 1px solid rgba(140, 45, 246, 0.4) !important;
                }

                .bringer-grid-2cols {
                    display: flex !important;
                    flex-direction: column !important;
                    gap: 20px !important;
                }

                .editor-window pre {
                    font-size: 11px !important;
                    padding: 10px !important;
                }
            }"""

new_hero_mq = """                        /* Responsive Overrides for Hero: Elevated & High Positioning on Mobile */
                        @media (max-width: 900px) {
                .bringer-hero-section {
                    margin-top: -100px !important;
                    padding-top: 0 !important;
                }

                .hero-badge,
                .vertical-text,
                .glass-pill,
                .pill-1,
                .pill-2,
                .pill-3,
                #hero-particles,
                .hero-particle { 
                    display: none !important; 
                    opacity: 0 !important;
                    visibility: hidden !important;
                    animation: none !important;
                }

                /* Elevate Hero Typography Higher on the Screen */
                .hero-main-title { 
                    transform: translateY(-14vh) !important; 
                }
                .hero-main-title h1 span { 
                    font-size: clamp(2.6rem, 13vw, 4.2rem) !important; 
                    line-height: 1.05 !important;
                }
                .hero-main-title h1 span:last-child { 
                    margin-top: -1.5vw !important; 
                }
                .hero-main-title > div:first-child { 
                    font-size: 0.6rem !important; 
                    margin-bottom: 1.5vh !important; 
                    letter-spacing: 0.4em !important;
                }
                .hero-main-title > div:last-child { 
                    font-size: 0.65rem !important; 
                    margin-top: 1.8vh !important; 
                    letter-spacing: 0.22em !important;
                }

                /* Elevate Description in proportion */
                .hero-desc {
                    display: block !important;
                    position: absolute !important;
                    bottom: 22vh !important;
                    left: 20px !important;
                    right: 20px !important;
                    max-width: 320px !important;
                    margin: 0 auto !important;
                    text-align: center !important;
                    border-left: none !important;
                    border-top: 1px solid rgba(140, 45, 246, 0.4) !important;
                    padding: 12px 10px 0 !important;
                }
                .hero-desc p { 
                    font-size: 0.75rem !important; 
                    line-height: 1.5 !important; 
                }

                /* Elevate Explore Button comfortably */
                .hero-scroll-btn {
                    position: absolute !important;
                    width: 60px !important;
                    height: 60px !important;
                    bottom: 9vh !important;
                    left: 50% !important;
                    right: auto !important;
                    transform: translateX(-50%) !important;
                    font-size: 0.52rem !important;
                    backdrop-filter: none !important;
                    -webkit-backdrop-filter: none !important;
                    background: rgba(140, 45, 246, 0.9) !important;
                    border: 1px solid rgba(140, 45, 246, 0.4) !important;
                }

                .bringer-grid-2cols {
                    display: flex !important;
                    flex-direction: column !important;
                    gap: 20px !important;
                }

                .editor-window pre {
                    font-size: 11px !important;
                    padding: 10px !important;
                }
            }"""

content_norm = content.replace('\r\n', '\n')
old_mq_norm = old_hero_mq.replace('\r\n', '\n')
new_mq_norm = new_hero_mq.replace('\r\n', '\n')

if old_mq_norm in content_norm:
    content_norm = content_norm.replace(old_mq_norm, new_mq_norm, 1)
    with open('home.html', 'w', encoding='cp1252', errors='xmlcharrefreplace') as fp:
        fp.write(content_norm)
    print("SUCCESS: Elevated hero content on mobile in home.html!")
else:
    print("ERROR: old_hero_mq not matched directly")
