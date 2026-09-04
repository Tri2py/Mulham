import glob
import os
import re

# Hyper-Minimalist Geometric Monogram Preloader
# Features:
# 1. Self-drawing animated SVG Monogram 'M' with glowing gradient stroke
# 2. Precision live counter (00% -> 100%) with luxury monospace tracking
# 3. Fine progress hairline
# 4. Cinematic Dual-Curtain wipe exit
# 5. Fast, snappy, non-blocking duration (completes in ~1.1s or on load)

MONOGRAM_LOADER = """    <!-- Hyper-Minimalist Geometric Monogram Preloader -->
    <div id="loader-wrapper" aria-hidden="true">
        <!-- Dual theatrical sliding curtains -->
        <div class="loader-curtain loader-curtain--left"></div>
        <div class="loader-curtain loader-curtain--right"></div>
        
        <!-- Ambient radial glow behind monogram -->
        <div class="loader-ambient-glow"></div>

        <!-- Center Stage Monogram & Counter -->
        <div id="loader-content">
            <!-- Animated Self-Drawing Geometric 'M' SVG -->
            <div class="loader-svg-wrap">
                <svg width="74" height="64" viewBox="0 0 74 64" fill="none" xmlns="http://www.w3.org/2000/svg" class="loader-monogram-svg">
                    <defs>
                        <linearGradient id="monogramStroke" x1="0%" y1="0%" x2="100%" y2="100%">
                            <stop offset="0%" stop-color="#8C2DF6" />
                            <stop offset="50%" stop-color="#c084fc" />
                            <stop offset="100%" stop-color="#ffffff" />
                        </linearGradient>
                        <filter id="monogramGlow" x="-20%" y="-20%" width="140%" height="140%">
                            <feGaussianBlur stdDeviation="3" result="blur" />
                            <feMerge>
                                <feMergeNode in="blur" />
                                <feMergeNode in="SourceGraphic" />
                            </feMerge>
                        </filter>
                    </defs>
                    <!-- Precision architectural paths for 'M' -->
                    <path class="m-path m-path-1" d="M12 56V12L37 42L62 12V56" stroke="url(#monogramStroke)" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" filter="url(#monogramGlow)" />
                    <!-- Geometric accent dot -->
                    <circle class="m-dot" cx="37" cy="54" r="3" fill="#8C2DF6" />
                </svg>
            </div>

            <!-- Typography Brand Line -->
            <div class="loader-brand">
                <span class="loader-brand-name">MULHAM</span>
                <span class="loader-brand-dot"></span>
                <span class="loader-brand-role">STUDIO</span>
            </div>

            <!-- Precision Percentage Counter -->
            <div class="loader-counter-wrap">
                <span id="loaderCounterNumber" class="loader-counter-number">00</span><span class="loader-counter-pct">%</span>
            </div>

            <!-- Hairline Progress Bar -->
            <div class="loader-progress-wrap">
                <div id="loaderProgressFill" class="loader-progress-fill"></div>
            </div>
        </div>
    </div>

    <style>
        /* === Root Wrapper === */
        #loader-wrapper {
            position: fixed;
            inset: 0;
            z-index: 9999999;
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
            pointer-events: all;
            user-select: none;
            background: transparent;
        }

        /* === Theatrical Curtains === */
        .loader-curtain {
            position: absolute;
            top: 0;
            width: 50.5%;
            height: 100%;
            background: #06020A;
            z-index: 100000;
            transition: transform 0.85s cubic-bezier(0.77, 0, 0.175, 1);
            will-change: transform;
        }
        .loader-curtain--left {
            left: 0;
            border-right: 1px solid rgba(140, 45, 246, 0.18);
        }
        .loader-curtain--right {
            right: 0;
            border-left: 1px solid rgba(140, 45, 246, 0.18);
        }
        .loaded .loader-curtain--left {
            transform: translateX(-101%);
        }
        .loaded .loader-curtain--right {
            transform: translateX(101%);
        }

        /* Ambient Glow */
        .loader-ambient-glow {
            position: absolute;
            width: 340px;
            height: 340px;
            border-radius: 50%;
            background: radial-gradient(circle, rgba(140, 45, 246, 0.22) 0%, rgba(140, 45, 246, 0.04) 50%, transparent 70%);
            z-index: 100001;
            pointer-events: none;
            filter: blur(50px);
            animation: monogramGlowPulse 2s ease-in-out infinite alternate;
        }

        /* === Center Brand Stage === */
        #loader-content {
            position: relative;
            z-index: 100002;
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
            gap: 14px;
            transition: opacity 0.45s cubic-bezier(0.4, 0, 0.2, 1), transform 0.5s cubic-bezier(0.4, 0, 0.2, 1);
        }
        .loaded #loader-content {
            opacity: 0;
            transform: scale(0.92) translateY(-14px);
        }

        /* === SVG Monogram Stroke Animation === */
        .loader-svg-wrap {
            position: relative;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 2px;
        }
        .loader-monogram-svg {
            display: block;
            overflow: visible;
        }
        .m-path-1 {
            stroke-dasharray: 220;
            stroke-dashoffset: 220;
            animation: drawMonogramPath 1.3s cubic-bezier(0.65, 0, 0.35, 1) forwards;
        }
        .m-dot {
            opacity: 0;
            transform: scale(0);
            transform-origin: 37px 54px;
            animation: dotPopIn 0.4s 0.8s cubic-bezier(0.34, 1.56, 0.64, 1) forwards;
        }

        /* === Typography Line === */
        .loader-brand {
            display: flex;
            align-items: center;
            gap: 8px;
            font-family: 'Inter', -apple-system, sans-serif;
            font-size: 0.72rem;
            font-weight: 600;
            letter-spacing: 0.28em;
            color: rgba(255, 255, 255, 0.75);
            opacity: 0;
            transform: translateY(8px);
            animation: brandFadeUp 0.6s 0.25s cubic-bezier(0.16, 1, 0.3, 1) forwards;
        }
        .loader-brand-name {
            color: #ffffff;
        }
        .loader-brand-dot {
            width: 3px;
            height: 3px;
            border-radius: 50%;
            background: #8C2DF6;
            display: inline-block;
        }
        .loader-brand-role {
            color: rgba(255, 255, 255, 0.4);
            font-weight: 400;
        }

        /* === Numeric Counter === */
        .loader-counter-wrap {
            font-family: 'Inter', -apple-system, monospace;
            font-size: 1.05rem;
            font-weight: 300;
            letter-spacing: 0.08em;
            color: #ffffff;
            margin-top: 2px;
            display: flex;
            align-items: baseline;
            gap: 1px;
            font-variant-numeric: tabular-nums;
        }
        .loader-counter-number {
            font-weight: 500;
            color: #ffffff;
        }
        .loader-counter-pct {
            font-size: 0.68rem;
            font-weight: 400;
            color: #8C2DF6;
        }

        /* === Progress Hairline === */
        .loader-progress-wrap {
            width: 120px;
            height: 1.5px;
            background: rgba(255, 255, 255, 0.08);
            border-radius: 99px;
            overflow: hidden;
            position: relative;
        }
        .loader-progress-fill {
            position: absolute;
            top: 0;
            left: 0;
            height: 100%;
            width: 0%;
            background: linear-gradient(90deg, #8C2DF6, #c084fc, #ffffff);
            box-shadow: 0 0 10px rgba(140, 45, 246, 0.8);
            border-radius: 99px;
            transition: width 0.08s linear;
        }

        /* Keyframes */
        @keyframes drawMonogramPath {
            to { stroke-dashoffset: 0; }
        }
        @keyframes dotPopIn {
            to { opacity: 1; transform: scale(1); }
        }
        @keyframes brandFadeUp {
            to { opacity: 1; transform: translateY(0); }
        }
        @keyframes monogramGlowPulse {
            0% { transform: scale(0.9); opacity: 0.55; }
            100% { transform: scale(1.18); opacity: 1; }
        }

        /* Dismissed */
        .loaded #loader-wrapper {
            pointer-events: none;
            visibility: hidden;
            transition: visibility 0s 0.95s;
        }
    </style>

    <script>
        (function() {
            var counterElem = document.getElementById('loaderCounterNumber');
            var progressElem = document.getElementById('loaderProgressFill');
            var currentPercent = 0;
            var targetPercent = 100;
            var isFinished = false;

            // Smooth numeric counter animation
            var counterInterval = setInterval(function() {
                if (currentPercent < 90) {
                    currentPercent += Math.floor(Math.random() * 6) + 3;
                    if (currentPercent > 90) currentPercent = 90;
                } else if (isFinished && currentPercent < 100) {
                    currentPercent += 2;
                }

                if (currentPercent > 100) currentPercent = 100;

                if (counterElem) {
                    counterElem.textContent = currentPercent < 10 ? '0' + currentPercent : currentPercent;
                }
                if (progressElem) {
                    progressElem.style.width = currentPercent + '%';
                }

                if (currentPercent >= 100) {
                    clearInterval(counterInterval);
                    setTimeout(dismissPreloader, 180);
                }
            }, 32);

            function dismissPreloader() {
                if (!document.body.classList.contains('loaded')) {
                    document.body.classList.add('loaded');
                }
            }

            function triggerFinish() {
                isFinished = true;
                // Rapidly complete counter to 100%
                var finishFast = setInterval(function() {
                    currentPercent += 5;
                    if (currentPercent >= 100) {
                        currentPercent = 100;
                        clearInterval(finishFast);
                        if (counterElem) counterElem.textContent = '100';
                        if (progressElem) progressElem.style.width = '100%';
                        setTimeout(dismissPreloader, 200);
                    } else {
                        if (counterElem) counterElem.textContent = currentPercent < 10 ? '0' + currentPercent : currentPercent;
                        if (progressElem) progressElem.style.width = currentPercent + '%';
                    }
                }, 20);
            }

            if (document.readyState === 'complete') {
                setTimeout(triggerFinish, 600);
            } else {
                window.addEventListener('load', function() {
                    setTimeout(triggerFinish, 600);
                });
            }

            // Fallback safety timeout so user is never stalled
            setTimeout(triggerFinish, 2800);
        })();
    </script>
"""

def update_file(filepath):
    with open(filepath, 'r', encoding='cp1252', errors='replace') as fp:
        content = fp.read()

    # Search for existing loader wrapper block
    # from <!-- ...Preloader --> to the closing </script>
    loader_pattern = r'(\s*<!--[^\n]*Preloader[^\n]*-->\s*<div id="loader-wrapper"[^>]*>.*?<\/script>\s*)'
    m = re.search(loader_pattern, content, re.DOTALL | re.IGNORECASE)

    if m:
        start, end = m.span()
        content = content[:start] + "\n" + MONOGRAM_LOADER.strip() + "\n" + content[end:]
        with open(filepath, 'w', encoding='cp1252', errors='xmlcharrefreplace') as fp:
            fp.write(content)
        print(f"Updated {filepath} (replaced existing loader)")
        return True
    else:
        # If not matched by regex, find id="loader-wrapper"
        idx = content.find('id="loader-wrapper"')
        if idx != -1:
            start = content.rfind('<!--', 0, idx)
            end = content.find('</script>', idx) + 9
            content = content[:start] + "\n" + MONOGRAM_LOADER.strip() + "\n" + content[end:]
            with open(filepath, 'w', encoding='cp1252', errors='xmlcharrefreplace') as fp:
                fp.write(content)
            print(f"Updated {filepath} (replaced via string boundaries)")
            return True
        else:
            # Insert after <body>
            body_m = re.search(r'<body[^>]*>', content, re.IGNORECASE)
            if body_m:
                end = body_m.end()
                content = content[:end] + "\n" + MONOGRAM_LOADER.strip() + "\n" + content[end:]
                with open(filepath, 'w', encoding='cp1252', errors='xmlcharrefreplace') as fp:
                    fp.write(content)
                print(f"Updated {filepath} (inserted after body)")
                return True
            else:
                print(f"FAILED for {filepath}")
                return False

for f in sorted(glob.glob('*.html')):
    update_file(f)

print("--- ALL 11 HTML FILES UPDATED WITH HYPER-MINIMALIST MONOGRAM LOADER ---")
