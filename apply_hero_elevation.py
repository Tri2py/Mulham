with open('home.html', 'r', encoding='cp1252', errors='replace') as fp:
    content = fp.read()

idx_start = content.find('/* Responsive Overrides for Hero */')
idx_end = content.find('.editor-window pre', idx_start)
idx_end = content.find('}', idx_end) + 1  # end of the @media block

NEW_HERO_MEDIA = """/* Responsive Overrides for Hero: Elevated Higher on Mobile */
        @media (max-width: 900px) {
            .bringer-hero-section {
                margin-top: -120px !important;
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

            /* Shift hero title significantly higher */
            .hero-main-title { 
                transform: translateY(-16vh) !important; 
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

            /* Shift editorial description higher */
            .hero-desc {
                display: block !important;
                position: absolute !important;
                bottom: 24vh !important;
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

            /* Explore button positioned nicely below description */
            .hero-scroll-btn {
                position: absolute !important;
                width: 60px !important;
                height: 60px !important;
                bottom: 11vh !important;
                left: 50% !important;
                right: auto !important;
                transform: translateX(-50%) !important;
                font-size: 0.52rem !important;
                backdrop-filter: none !important;
                -webkit-backdrop-filter: none !important;
                background: rgba(14, 8, 20, 0.9) !important;
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

content = content[:idx_start] + NEW_HERO_MEDIA + content[idx_end:]

with open('home.html', 'w', encoding='cp1252', errors='xmlcharrefreplace') as fp:
    fp.write(content)

print("SUCCESS: Hero section elevated higher on mobile view in home.html!")
