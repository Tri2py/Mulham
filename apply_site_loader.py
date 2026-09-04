import glob
import os
import re

# Premium Master Loader Component (HTML + CSS + JS)
# Designed to be inserted right after <body> or replacing previous preloader instances.
MASTER_LOADER = """    <!-- Premium Monolithic Split-Curtain Preloader -->
    <div id="loader-wrapper" aria-hidden="true">
        <!-- Dual theatrical sliding curtains -->
        <div class="loader-curtain loader-curtain--left"></div>
        <div class="loader-curtain loader-curtain--right"></div>
        
        <!-- Ambient radial glow behind brandmark -->
        <div class="loader-ambient-glow"></div>

        <!-- Center Stage Branding -->
        <div id="loader-content">
            <!-- Sleek orbit ring with counter-spinning pulse ring -->
            <div class="loader-ring-wrapper">
                <div class="loader-ring loader-ring--outer"></div>
                <div class="loader-ring loader-ring--inner"></div>
                <div class="loader-ring loader-ring--core"></div>
            </div>

            <!-- Staggered 3D typographic reveal -->
            <h2 class="loader-logo" aria-label="Mulham">
                <span class="loader-letter" style="animation-delay: 0.00s;">M</span><span class="loader-letter" style="animation-delay: 0.05s;">u</span><span class="loader-letter" style="animation-delay: 0.10s;">l</span><span class="loader-letter" style="animation-delay: 0.15s;">h</span><span class="loader-letter" style="animation-delay: 0.20s;">a</span><span class="loader-letter" style="animation-delay: 0.25s;">m</span><span class="loader-dot" style="animation-delay: 0.35s;">.</span>
            </h2>

            <!-- Editorial Subtitle with letter-spacing tracking -->
            <p class="loader-tagline">Design <span class="loader-amp">&amp;</span> Development</p>

            <!-- Ultra-fine luminous progress line -->
            <div class="loader-progress-wrap">
                <div class="loader-progress-bar"></div>
            </div>
        </div>
    </div>
    <style>
        /* === Loader Core Wrapper === */
        #loader-wrapper {
            position: fixed;
            inset: 0;
            z-index: 999999;
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
            pointer-events: all;
            user-select: none;
            background: transparent;
        }

        /* === Dual Theatrical Curtains (True Luxury Obsidian) === */
        .loader-curtain {
            position: absolute;
            top: 0;
            width: 50.5%;
            height: 100%;
            background: #06020A; /* Match site backdrop */
            z-index: 100000;
            transition: transform 0.95s cubic-bezier(0.77, 0, 0.175, 1);
            will-change: transform;
        }
        .loader-curtain--left {
            left: 0;
            transform-origin: left center;
            border-right: 1px solid rgba(140, 45, 246, 0.12);
        }
        .loader-curtain--right {
            right: 0;
            transform-origin: right center;
            border-left: 1px solid rgba(140, 45, 246, 0.12);
        }
        .loaded .loader-curtain--left {
            transform: translateX(-101%);
        }
        .loaded .loader-curtain--right {
            transform: translateX(101%);
        }

        /* Ambient glow backdrop */
        .loader-ambient-glow {
            position: absolute;
            width: 380px;
            height: 380px;
            border-radius: 50%;
            background: radial-gradient(circle, rgba(140, 45, 246, 0.2) 0%, rgba(140, 45, 246, 0.05) 45%, transparent 70%);
            z-index: 100001;
            pointer-events: none;
            filter: blur(40px);
            animation: loaderGlowPulse 2.4s ease-in-out infinite alternate;
        }

        /* === Center Brand Stage === */
        #loader-content {
            position: relative;
            z-index: 100002;
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
            gap: 16px;
            transition: opacity 0.5s cubic-bezier(0.4, 0, 0.2, 1), transform 0.6s cubic-bezier(0.4, 0, 0.2, 1);
        }
        .loaded #loader-content {
            opacity: 0;
            transform: scale(0.94) translateY(-12px);
        }

        /* === Concentric Orbit Rings === */
        .loader-ring-wrapper {
            position: relative;
            width: 76px;
            height: 76px;
            margin-bottom: 6px;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .loader-ring {
            position: absolute;
            border-radius: 50%;
        }
        .loader-ring--outer {
            inset: 0;
            border: 1.5px solid rgba(140, 45, 246, 0.15);
            border-top-color: #8C2DF6;
            border-right-color: rgba(140, 45, 246, 0.5);
            box-shadow: 0 0 25px rgba(140, 45, 246, 0.25);
            animation: loaderSpinClockwise 1.2s cubic-bezier(0.45, 0.05, 0.55, 0.95) infinite;
        }
        .loader-ring--inner {
            inset: 12px;
            border: 1.5px dashed rgba(255, 255, 255, 0.18);
            border-bottom-color: #b066ff;
            animation: loaderSpinCounter 1.8s linear infinite;
        }
        .loader-ring--core {
            width: 6px;
            height: 6px;
            background: #8C2DF6;
            box-shadow: 0 0 14px 2px #8C2DF6;
            animation: loaderCorePulse 1.2s ease-in-out infinite alternate;
        }

        /* === Typography: Serif Monogram Logo === */
        .loader-logo {
            font-family: 'Playfair Display', serif, Georgia;
            font-size: clamp(2.4rem, 5.5vw, 3.6rem);
            font-weight: 500;
            font-style: italic;
            color: #ffffff;
            margin: 0;
            letter-spacing: 0.02em;
            display: flex;
            align-items: baseline;
            justify-content: center;
            overflow: hidden;
            line-height: 1.1;
        }
        .loader-letter {
            display: inline-block;
            opacity: 0;
            transform: translateY(110%) rotateX(-75deg);
            animation: loaderLetterReveal 0.6s cubic-bezier(0.22, 1, 0.36, 1) forwards;
        }
        .loader-dot {
            display: inline-block;
            color: #8C2DF6;
            opacity: 0;
            transform: scale(0);
            animation: loaderDotPop 0.45s cubic-bezier(0.34, 1.56, 0.64, 1) forwards;
            text-shadow: 0 0 20px rgba(140, 45, 246, 0.9);
            margin-left: 2px;
        }

        /* === Tagline === */
        .loader-tagline {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            font-size: 0.72rem;
            font-weight: 400;
            letter-spacing: 0.32em;
            text-transform: uppercase;
            color: rgba(255, 255, 255, 0.4);
            margin: 0;
            opacity: 0;
            animation: loaderTagFade 0.7s 0.35s cubic-bezier(0.16, 1, 0.3, 1) forwards;
        }
        .loader-amp {
            color: #8C2DF6;
            font-style: italic;
            font-family: 'Playfair Display', serif;
            font-size: 0.85rem;
            margin: 0 4px;
        }

        /* === Glowing Progress Bar === */
        .loader-progress-wrap {
            width: 130px;
            height: 2px;
            background: rgba(255, 255, 255, 0.06);
            border-radius: 99px;
            overflow: hidden;
            margin-top: 6px;
            opacity: 0;
            animation: loaderTagFade 0.5s 0.2s ease forwards;
        }
        .loader-progress-bar {
            width: 0%;
            height: 100%;
            background: linear-gradient(90deg, #8C2DF6, #b066ff, #ffffff);
            box-shadow: 0 0 12px rgba(140, 45, 246, 0.7);
            border-radius: 99px;
            animation: loaderProgressBar 1.5s cubic-bezier(0.65, 0, 0.35, 1) forwards;
        }

        /* === Animation Keyframes === */
        @keyframes loaderSpinClockwise {
            to { transform: rotate(360deg); }
        }
        @keyframes loaderSpinCounter {
            to { transform: rotate(-360deg); }
        }
        @keyframes loaderGlowPulse {
            0% { transform: scale(0.85); opacity: 0.6; }
            100% { transform: scale(1.15); opacity: 1; }
        }
        @keyframes loaderCorePulse {
            0% { transform: scale(0.8); opacity: 0.7; }
            100% { transform: scale(1.3); opacity: 1; }
        }
        @keyframes loaderLetterReveal {
            to {
                opacity: 1;
                transform: translateY(0) rotateX(0deg);
            }
        }
        @keyframes loaderDotPop {
            to {
                opacity: 1;
                transform: scale(1);
            }
        }
        @keyframes loaderTagFade {
            from {
                opacity: 0;
                letter-spacing: 0.5em;
            }
            to {
                opacity: 1;
                letter-spacing: 0.32em;
            }
        }
        @keyframes loaderProgressBar {
            0% { width: 0%; }
            45% { width: 55%; }
            85% { width: 90%; }
            100% { width: 100%; }
        }

        /* === Loaded / Dismissed State === */
        .loaded #loader-wrapper {
            pointer-events: none;
            visibility: hidden;
            transition: visibility 0s 1.05s;
        }
    </style>
    <script>
        (function() {
            function dismissPreloader() {
                if (!document.body.classList.contains('loaded')) {
                    document.body.classList.add('loaded');
                }
            }
            if (document.readyState === 'complete') {
                setTimeout(dismissPreloader, 1200);
            } else {
                window.addEventListener('load', function() {
                    setTimeout(dismissPreloader, 1200);
                });
            }
            // Fallback safety timer so user is never stuck
            setTimeout(dismissPreloader, 3500);
        })();
    </script>
"""

def update_file(filepath):
    print(f"Processing: {filepath}")
    with open(filepath, 'r', encoding='cp1252', errors='replace') as fp:
        content = fp.read()

    filename = os.path.basename(filepath)

    if filename == 'home.html':
        # Replace Cinematic Split-Reveal Preloader block
        idx = content.find('Cinematic Split-Reveal Preloader')
        start = content.rfind('<!--', 0, idx)
        end = content.find('</script>', idx) + 9
        content = content[:start] + MASTER_LOADER.strip() + content[end:]

    elif filename in ['contact.html', 'portfolio.html']:
        # Replace Ultra-Premium Monolithic Preloader block
        idx = content.find('Ultra-Premium Monolithic Preloader')
        start = content.rfind('<!--', 0, idx)
        end = content.find('</script>', idx) + 9
        content = content[:start] + MASTER_LOADER.strip() + content[end:]

    elif filename == 'web-projects.html':
        # Remove old CSS in <head>
        idx_css = content.find('/* Preloader */')
        if idx_css != -1:
            end_css = content.find('/* Header/Navbar Overrides', idx_css)
            content = content[:idx_css] + content[end_css:]
        # Replace old HTML + script in <body>
        idx_html = content.find('<!-- Preloader -->')
        if idx_html != -1:
            end_html = content.find('</script>', idx_html) + 9
            content = content[:idx_html] + MASTER_LOADER.strip() + content[end_html:]

    else:
        # File currently has NO loader: insert right after <body>
        body_match = re.search(r'<body[^>]*>', content, re.IGNORECASE)
        if not body_match:
            print(f"  ERROR: No <body> found in {filepath}!")
            return False
        body_end = body_match.end()
        # Insert newline and MASTER_LOADER
        content = content[:body_end] + "\n" + MASTER_LOADER.strip() + content[body_end:]

    with open(filepath, 'w', encoding='cp1252', errors='xmlcharrefreplace') as fp:
        fp.write(content)
    print(f"  Successfully updated {filepath}")
    return True

html_files = sorted(glob.glob('*.html'))
for f in html_files:
    update_file(f)

print("\n--- ALL HTML FILES UPDATED ---")
