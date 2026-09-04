import re

# Read current web-projects.html
with open('web-projects.html', 'r', encoding='cp1252', errors='replace') as f:
    orig = f.read()

# Unified styles for web-projects.html
NEW_CSS = """
        /* === Deep Luxury Studio Canvas === */
        :root {
            --bringer-s-accent: #8C2DF6;
            --bringer-s-accent-glow: rgba(140, 45, 246, 0.35);
            --bringer-s-heading: #FFFFFF;
            --bringer-s-text: rgba(255, 255, 255, 0.65);
            --bringer-s-card-bg: rgba(14, 8, 20, 0.72);
            --bringer-s-card-border: rgba(255, 255, 255, 0.08);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        html {
            scroll-behavior: smooth;
        }

        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            background-color: #06020A !important;
            color: #e0e0e0;
            min-height: 100vh;
            overflow-x: hidden !important;
            position: relative;
        }

        /* Ambient Studio Light Blooms */
        .ambient-glow {
            position: fixed;
            pointer-events: none;
            z-index: 0;
            border-radius: 50%;
            filter: blur(120px);
            opacity: 0.35;
        }
        .ambient-glow--top {
            width: 550px;
            height: 550px;
            top: -150px;
            left: 50%;
            transform: translateX(-50%);
            background: radial-gradient(circle, rgba(140, 45, 246, 0.45) 0%, rgba(140, 45, 246, 0.05) 70%, transparent 100%);
        }
        .ambient-glow--bottom {
            width: 450px;
            height: 450px;
            bottom: 5%;
            right: -100px;
            background: radial-gradient(circle, rgba(140, 45, 246, 0.25) 0%, transparent 70%);
        }

        /* Ambient Subtle Grid Texture */
        .ambient-grid {
            position: fixed;
            inset: 0;
            pointer-events: none;
            z-index: 0;
            background-image: linear-gradient(rgba(255, 255, 255, 0.02) 1px, transparent 1px),
                              linear-gradient(90deg, rgba(255, 255, 255, 0.02) 1px, transparent 1px);
            background-size: 64px 64px;
            mask-image: radial-gradient(circle at 50% 30%, black 40%, transparent 80%);
            -webkit-mask-image: radial-gradient(circle at 50% 30%, black 40%, transparent 80%);
        }

        /* === Elegant Floating Glass Navbar === */
        #bringer-header {
            position: fixed !important;
            background: rgba(255, 255, 255, 0.02) !important;
            border: 1px solid rgba(255, 255, 255, 0.08) !important;
            backdrop-filter: blur(16px) !important;
            -webkit-backdrop-filter: blur(16px) !important;
            border-radius: 100px !important;
            padding: 0 30px !important;
            width: auto !important;
            min-width: 540px;
            max-width: 90vw !important;
            left: 50% !important;
            transform: translateX(-50%) !important;
            top: 26px !important;
            z-index: 1000 !important;
            transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1) !important;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5) !important;
            display: flex;
            justify-content: center;
        }

        #bringer-header.is-sticky {
            top: 18px !important;
            background: rgba(10, 6, 16, 0.78) !important;
            border: 1px solid rgba(140, 45, 246, 0.22) !important;
            box-shadow: 0 14px 45px rgba(0, 0, 0, 0.85) !important;
        }

        .bringer-header-inner {
            display: flex !important;
            justify-content: space-between !important;
            align-items: center !important;
            width: 100% !important;
            padding: 12px 0 !important;
            min-height: 40px;
        }

        .bringer-header-lp {
            display: flex !important;
            align-items: center !important;
        }

        .bringer-header-mp {
            display: flex !important;
            justify-content: flex-end !important;
            flex-grow: 1 !important;
        }

        ul.main-menu {
            display: flex;
            align-items: center;
            gap: 28px !important;
            margin: 0 !important;
            padding: 0 !important;
            list-style: none;
        }

        ul.main-menu li a {
            font-family: 'Inter', sans-serif !important;
            font-size: 0.82rem !important;
            text-transform: uppercase !important;
            letter-spacing: 0.15em !important;
            font-weight: 500 !important;
            color: #fff !important;
            opacity: 0.7;
            text-decoration: none;
            transition: opacity 0.3s ease, color 0.3s ease;
            position: relative;
            padding: 6px 0;
        }

        ul.main-menu li a:hover,
        ul.main-menu li.current-menu-item a {
            opacity: 1;
            color: #c084fc !important;
        }

        .bringer-active-menu-ind {
            display: none !important;
        }

        .bringer-mobile-header-inner {
            display: none;
            justify-content: space-between;
            align-items: center;
            width: 100%;
            padding: 12px 0;
        }

        /* === Main Content Architecture === */
        .main-content {
            position: relative;
            z-index: 2;
            max-width: 1140px;
            margin: 0 auto;
            padding: 140px 32px 60px;
        }

        /* === Editorial Hero Header === */
        .web-projects-hero {
            margin-bottom: 56px;
            text-align: left;
            position: relative;
        }

        .hero-pill-badge {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 6px 14px;
            background: rgba(140, 45, 246, 0.12);
            border: 1px solid rgba(140, 45, 246, 0.28);
            border-radius: 100px;
            font-size: 0.72rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.16em;
            color: #c084fc;
            margin-bottom: 22px;
        }

        .hero-pill-badge .status-dot {
            width: 6px;
            height: 6px;
            border-radius: 50%;
            background: #8C2DF6;
            box-shadow: 0 0 10px #8C2DF6;
            animation: statusPulse 2s infinite ease-in-out;
        }

        @keyframes statusPulse {
            0%, 100% { opacity: 1; transform: scale(1); }
            50% { opacity: 0.45; transform: scale(1.3); }
        }

        .hero-layout-split {
            display: flex;
            align-items: flex-end;
            justify-content: space-between;
            gap: 40px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
            padding-bottom: 36px;
        }

        .hero-headline {
            font-family: 'Playfair Display', Georgia, serif;
            font-size: clamp(2.4rem, 4.8vw, 3.8rem);
            font-weight: 400;
            letter-spacing: -0.025em;
            line-height: 1.1;
            color: #ffffff;
            margin: 0;
        }

        .hero-headline em {
            font-style: italic;
            background: linear-gradient(135deg, #ffffff 30%, rgba(255, 255, 255, 0.5) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .hero-lead-text {
            font-family: 'Inter', sans-serif;
            font-size: 0.95rem;
            line-height: 1.65;
            color: rgba(255, 255, 255, 0.6);
            max-width: 420px;
            margin: 0;
        }

        /* === Filter / Quick Stats Rail === */
        .projects-filter-bar {
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 16px;
            margin-bottom: 36px;
            padding: 8px 0;
        }

        .filter-counter {
            font-size: 0.8rem;
            color: rgba(255, 255, 255, 0.45);
            font-weight: 500;
            letter-spacing: 0.06em;
            text-transform: uppercase;
        }
        .filter-counter strong {
            color: #ffffff;
            font-weight: 700;
        }

        .filter-pills {
            display: flex;
            gap: 8px;
            flex-wrap: wrap;
        }

        .filter-pill {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.08);
            color: rgba(255, 255, 255, 0.65);
            padding: 7px 16px;
            border-radius: 100px;
            font-size: 0.76rem;
            font-weight: 500;
            cursor: pointer;
            transition: all 0.25s ease;
            user-select: none;
        }

        .filter-pill:hover,
        .filter-pill.active {
            background: rgba(140, 45, 246, 0.16);
            border-color: rgba(140, 45, 246, 0.4);
            color: #ffffff;
        }

        /* === Architectural Project Cards Grid === */
        .projects-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 28px;
            margin-bottom: 56px;
        }

        .project-card {
            position: relative;
            display: flex;
            flex-direction: column;
            background: rgba(16, 9, 24, 0.55);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 20px;
            overflow: hidden;
            text-decoration: none;
            color: inherit;
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1),
                        border-color 0.4s cubic-bezier(0.16, 1, 0.3, 1),
                        box-shadow 0.4s cubic-bezier(0.16, 1, 0.3, 1);
            isolation: isolate;
        }

        .project-card::before {
            content: '';
            position: absolute;
            inset: 0;
            background: radial-gradient(600px circle at var(--mouse-x, 50%) var(--mouse-y, 50%), rgba(140, 45, 246, 0.12), transparent 40%);
            opacity: 0;
            transition: opacity 0.4s ease;
            pointer-events: none;
            z-index: 1;
        }

        .project-card:hover {
            transform: translateY(-6px);
            border-color: rgba(140, 45, 246, 0.45);
            box-shadow: 0 24px 60px rgba(0, 0, 0, 0.6), 0 0 35px rgba(140, 45, 246, 0.14);
        }

        .project-card:hover::before {
            opacity: 1;
        }

        /* Card Header Graphic with Abstract Visual Identity */
        .project-card-header {
            position: relative;
            width: 100%;
            height: 190px;
            background: linear-gradient(135deg, rgba(22, 12, 34, 0.95) 0%, rgba(12, 6, 20, 0.95) 100%);
            border-bottom: 1px solid rgba(255, 255, 255, 0.06);
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
            z-index: 2;
        }

        .project-card-pattern {
            position: absolute;
            inset: 0;
            background-size: 24px 24px;
            opacity: 0.18;
            transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.4s ease;
        }

        .project-card:hover .project-card-pattern {
            transform: scale(1.08);
            opacity: 0.3;
        }

        .pattern-grid {
            background-image: radial-gradient(rgba(140, 45, 246, 0.85) 1px, transparent 1px);
        }
        .pattern-lines {
            background-image: repeating-linear-gradient(45deg, rgba(140, 45, 246, 0.3) 0, rgba(140, 45, 246, 0.3) 1px, transparent 0, transparent 50%);
            background-size: 16px 16px;
        }
        .pattern-dots {
            background-image: radial-gradient(rgba(255, 255, 255, 0.6) 1px, transparent 1px);
        }
        .pattern-waves {
            background-image: radial-gradient(circle at 100% 150%, rgba(140, 45, 246, 0.4) 24px, transparent 25px);
            background-size: 28px 28px;
        }

        /* Animated Icon Badge */
        .card-icon-badge {
            position: relative;
            z-index: 3;
            width: 72px;
            height: 72px;
            border-radius: 18px;
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid rgba(255, 255, 255, 0.12);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            display: flex;
            align-items: center;
            justify-content: center;
            color: #c084fc;
            box-shadow: 0 8px 30px rgba(0, 0, 0, 0.35);
            transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
        }

        .card-icon-badge svg,
        .card-icon-badge i {
            font-size: 32px;
            transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
        }

        .project-card:hover .card-icon-badge {
            background: rgba(140, 45, 246, 0.22);
            border-color: rgba(140, 45, 246, 0.6);
            color: #ffffff;
            box-shadow: 0 12px 35px rgba(140, 45, 246, 0.35);
            transform: scale(1.08);
        }

        .project-card:hover .card-icon-badge svg,
        .project-card:hover .card-icon-badge i {
            transform: scale(1.1);
        }

        /* Index badge in top right of graphic */
        .card-index-indicator {
            position: absolute;
            top: 16px;
            right: 18px;
            font-family: 'Inter', monospace, sans-serif;
            font-size: 0.72rem;
            font-weight: 700;
            letter-spacing: 0.12em;
            color: rgba(255, 255, 255, 0.25);
            z-index: 3;
        }

        /* Card Body */
        .project-card-body {
            position: relative;
            z-index: 2;
            padding: 26px 28px 24px;
            display: flex;
            flex-direction: column;
            flex: 1;
        }

        .card-meta-row {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 14px;
            gap: 12px;
        }

        .tag-row {
            display: flex;
            align-items: center;
            gap: 8px;
            flex-wrap: wrap;
        }

        .tag {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 4px 12px;
            border-radius: 100px;
            font-size: 0.68rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            background: rgba(140, 45, 246, 0.12);
            color: #c084fc;
            border: 1px solid rgba(140, 45, 246, 0.25);
        }

        .project-type-label {
            font-size: 0.72rem;
            color: rgba(255, 255, 255, 0.35);
            font-weight: 500;
            letter-spacing: 0.05em;
        }

        .project-card-body h3 {
            font-family: 'Playfair Display', Georgia, serif;
            font-size: 1.42rem;
            font-weight: 600;
            color: #ffffff;
            margin-bottom: 10px;
            letter-spacing: -0.015em;
            line-height: 1.25;
            transition: color 0.3s ease;
        }

        .project-card:hover .project-card-body h3 {
            color: #e5ccff;
        }

        .project-card-body p {
            font-size: 0.88rem;
            line-height: 1.65;
            color: rgba(255, 255, 255, 0.58);
            margin-bottom: 22px;
            flex: 1;
        }

        /* Tech stack pills inside card body */
        .tech-stack-row {
            display: flex;
            gap: 6px;
            flex-wrap: wrap;
            margin-bottom: 20px;
            padding-top: 14px;
            border-top: 1px solid rgba(255, 255, 255, 0.06);
        }

        .tech-tag {
            font-family: 'Inter', monospace, sans-serif;
            font-size: 0.68rem;
            color: rgba(255, 255, 255, 0.45);
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.06);
            padding: 3px 8px;
            border-radius: 6px;
        }

        /* Card Action Row */
        .card-action-row {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-top: auto;
            padding-top: 14px;
            border-top: 1px solid rgba(255, 255, 255, 0.06);
        }

        .visit-link {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            font-size: 0.82rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.12em;
            color: #c084fc;
            transition: all 0.25s ease;
        }

        .project-card:hover .visit-link {
            color: #ffffff;
        }

        .action-arrow-wrap {
            width: 34px;
            height: 34px;
            border-radius: 50%;
            background: rgba(140, 45, 246, 0.12);
            border: 1px solid rgba(140, 45, 246, 0.25);
            display: flex;
            align-items: center;
            justify-content: center;
            color: #c084fc;
            transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
        }

        .project-card:hover .action-arrow-wrap {
            background: #8C2DF6;
            border-color: #8C2DF6;
            color: #ffffff;
            transform: translate(3px, -3px) rotate(-45deg);
            box-shadow: 0 0 16px rgba(140, 45, 246, 0.5);
        }

        /* === Navigation / Back Action Section === */
        .back-section {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 16px;
            padding: 44px 0 20px;
            flex-wrap: wrap;
        }

        .back-btn {
            display: inline-flex;
            align-items: center;
            gap: 10px;
            padding: 14px 30px;
            border-radius: 100px;
            font-size: 0.85rem;
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: 0.12em;
            color: rgba(255, 255, 255, 0.75);
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.1);
            text-decoration: none;
            transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
        }

        .back-btn:hover {
            background: rgba(140, 45, 246, 0.18);
            border-color: rgba(140, 45, 246, 0.4);
            color: #ffffff;
            transform: translateY(-2px);
            box-shadow: 0 10px 30px rgba(140, 45, 246, 0.15);
        }

        .back-btn-primary {
            background: rgba(140, 45, 246, 0.15);
            border-color: rgba(140, 45, 246, 0.35);
            color: #ffffff;
        }

        /* === Sleek Low-Profile Studio Footer === */
        .contact-page-footer {
            background: #06020A;
            border-top: 1px solid rgba(255, 255, 255, 0.06);
            padding: 36px 0 44px;
            margin-top: 6vh;
            position: relative;
            z-index: 5;
        }

        .contact-footer-inner {
            max-width: 1140px;
            margin: 0 auto;
            padding: 0 32px;
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

        /* === Responsive Viewport Adjustments === */
        @media (max-width: 900px) {
            .projects-grid {
                grid-template-columns: 1fr;
                gap: 24px;
            }
            .hero-layout-split {
                flex-direction: column;
                align-items: flex-start;
                gap: 16px;
            }
            .hero-lead-text {
                max-width: 100%;
            }
        }

        @media (max-width: 768px) {
            #bringer-header {
                min-width: 0;
                width: calc(100% - 40px) !important;
                padding: 0 20px !important;
                backdrop-filter: none !important;
                -webkit-backdrop-filter: none !important;
                background: rgba(14, 8, 20, 0.95) !important;
                top: 16px !important;
            }

            .bringer-header-inner {
                display: none !important;
            }

            .bringer-mobile-header-inner {
                display: flex !important;
            }

            .main-content {
                padding: 105px 20px 40px;
            }

            .hero-headline {
                font-size: 2.2rem;
            }

            .project-card-header {
                height: 160px;
            }

            .card-icon-badge {
                width: 60px;
                height: 60px;
                border-radius: 14px;
            }

            .card-icon-badge svg,
            .card-icon-badge i {
                font-size: 26px;
            }

            .project-card-body {
                padding: 20px;
            }

            .project-card-body h3 {
                font-size: 1.25rem;
            }

            .contact-page-footer {
                padding: 28px 0 36px;
                margin-top: 4vh;
            }

            .contact-footer-inner {
                flex-direction: column;
                text-align: center;
                gap: 14px;
                padding: 0 20px;
            }

            .contact-footer-socials {
                justify-content: center;
            }
        }

        @media (max-width: 480px) {
            #bringer-header {
                width: calc(100% - 24px) !important;
                padding: 0 16px !important;
            }
            .hero-headline {
                font-size: 1.9rem;
            }
            .main-content {
                padding: 95px 14px 32px;
            }
            .projects-filter-bar {
                flex-direction: column;
                align-items: flex-start;
            }
            .back-btn {
                width: 100%;
                justify-content: center;
            }
        }
"""

print("Writing replacement script...")
