import re

# Read file with cp1252 encoding (same as original)
with open('home.html', 'r', encoding='cp1252', errors='replace') as f:
    content = f.read()

OLD_LOADER = """        <!-- Ultra-Premium Monolithic Preloader -->
    <div id="loader-wrapper">
        <div id="loader-content">
            <h2 class="loader-logo">Mulham<span class="loader-dot">.</span></h2>
            <div class="loader-progress-wrap">
                <div class="loader-progress-bar"></div>
            </div>
        </div>
        <div class="loader-bg"></div>
    </div>
    <style>
        #loader-wrapper {
            position: fixed;
            inset: 0;
            z-index: 99999;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .loader-bg {
            position: absolute;
            inset: 0;
            background: #050505; /* Deep luxury monolithic black */
            z-index: 100000;
            transition: transform 0.8s cubic-bezier(0.7, 0, 0.3, 1);
            transform-origin: top;
        }

        #loader-content {
            position: relative;
            z-index: 100001;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 20px;
            transition: opacity 0.4s ease-out, transform 0.4s ease-out;
        }

        .loader-logo {
            font-family: 'Playfair Display', serif;
            font-size: clamp(2rem, 4vw, 3rem);
            font-weight: 500;
            font-style: italic;
            color: #ffffff;
            margin: 0;
            letter-spacing: -0.02em;
            opacity: 0;
            animation: loaderFadeIn 0.5s ease forwards;
        }

        .loader-dot {
            color: #8C2DF6;
            display: inline-block;
            animation: pulseDot 1.5s infinite ease-in-out;
        }

        .loader-progress-wrap {
            width: 140px;
            height: 2px;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 2px;
            overflow: hidden;
            opacity: 0;
            animation: loaderFadeIn 0.5s 0.2s ease forwards;
        }

        .loader-progress-bar {
            width: 0%;
            height: 100%;
            background: linear-gradient(90deg, #8C2DF6, #b066ff);
            box-shadow: 0 0 10px rgba(140, 45, 246, 0.5);
            animation: loaderProgress 1.6s cubic-bezier(0.7, 0, 0.3, 1) forwards;
        }

        @keyframes loaderFadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        @keyframes pulseDot {
            0%, 100% { opacity: 1; text-shadow: 0 0 15px rgba(140, 45, 246, 0.8); }
            50% { opacity: 0.8; text-shadow: 0 0 5px rgba(140, 45, 246, 0.3); }
        }

        @keyframes loaderProgress {
            0% { width: 0%; }
            40% { width: 60%; }
            100% { width: 100%; }
        }

        .loaded #loader-content {
            opacity: 0;
            transform: translateY(-20px);
        }

        .loaded .loader-bg {
            transform: scaleY(0);
        }

        .loaded #loader-wrapper {
            pointer-events: none;
            visibility: hidden;
            transition: visibility 0s 0.8s; 
        }
    </style>
    <script>
        function hidePreloader() { 
            if (!document.body.classList.contains('loaded')) {
                document.body.classList.add('loaded'); 
            }
        }
        document.addEventListener('DOMContentLoaded', function () { 
            setTimeout(hidePreloader, 1600); 
        });
        window.addEventListener('load', function() {
            setTimeout(hidePreloader, 1600);
        });
        setTimeout(hidePreloader, 4000);
    </script>"""

NEW_LOADER = """        <!-- Cinematic Split-Reveal Preloader -->
    <div id="loader-wrapper">
        <!-- Two curtain halves -->
        <div class="loader-curtain loader-curtain--left"></div>
        <div class="loader-curtain loader-curtain--right"></div>
        <!-- Center content -->
        <div id="loader-content">
            <div class="loader-ring"></div>
            <h2 class="loader-logo">
                <span class="loader-letter" style="animation-delay:0s">M</span><span class="loader-letter" style="animation-delay:0.06s">u</span><span class="loader-letter" style="animation-delay:0.12s">l</span><span class="loader-letter" style="animation-delay:0.18s">h</span><span class="loader-letter" style="animation-delay:0.24s">a</span><span class="loader-letter" style="animation-delay:0.30s">m</span><span class="loader-dot" style="animation-delay:0.42s">.</span>
            </h2>
            <p class="loader-tagline">Design & Development</p>
        </div>
    </div>
    <style>
        #loader-wrapper {
            position: fixed;
            inset: 0;
            z-index: 99999;
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
        }

        /* === Curtain Halves === */
        .loader-curtain {
            position: absolute;
            top: 0;
            width: 50%;
            height: 100%;
            background: #050505;
            z-index: 100000;
            transition: transform 0.9s cubic-bezier(0.76, 0, 0.24, 1);
        }
        .loader-curtain--left  { left: 0;  transform-origin: left;  }
        .loader-curtain--right { right: 0; transform-origin: right; }
        .loaded .loader-curtain--left  { transform: translateX(-100%); }
        .loaded .loader-curtain--right { transform: translateX(100%);  }

        /* === Center Content === */
        #loader-content {
            position: relative;
            z-index: 100001;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 16px;
            transition: opacity 0.5s ease-out, transform 0.5s ease-out;
        }
        .loaded #loader-content {
            opacity: 0;
            transform: scale(0.92);
        }

        /* === Orbiting Ring === */
        .loader-ring {
            width: 90px;
            height: 90px;
            border-radius: 50%;
            border: 1.5px solid rgba(140, 45, 246, 0.12);
            border-top-color: #8C2DF6;
            animation: loaderSpin 1.1s cubic-bezier(0.45, 0.05, 0.55, 0.95) infinite;
            margin-bottom: 8px;
            box-shadow: 0 0 30px rgba(140, 45, 246, 0.15);
        }

        /* === Logo Letters === */
        .loader-logo {
            font-family: 'Playfair Display', serif;
            font-size: clamp(2.2rem, 5vw, 3.4rem);
            font-weight: 500;
            font-style: italic;
            color: #ffffff;
            margin: 0;
            letter-spacing: 0.04em;
            display: flex;
            overflow: hidden;
        }
        .loader-letter {
            display: inline-block;
            opacity: 0;
            transform: translateY(100%) rotateX(-80deg);
            animation: letterReveal 0.55s cubic-bezier(0.22, 1, 0.36, 1) forwards;
        }
        .loader-dot {
            display: inline-block;
            color: #8C2DF6;
            opacity: 0;
            transform: scale(0);
            animation: dotPop 0.4s cubic-bezier(0.34, 1.56, 0.64, 1) forwards;
            text-shadow: 0 0 18px rgba(140, 45, 246, 0.7);
        }

        /* === Tagline === */
        .loader-tagline {
            font-family: 'Inter', sans-serif;
            font-size: 0.72rem;
            font-weight: 400;
            letter-spacing: 0.28em;
            text-transform: uppercase;
            color: rgba(255, 255, 255, 0.35);
            margin: 0;
            opacity: 0;
            animation: tagFade 0.6s 0.5s ease forwards;
        }

        /* === Keyframes === */
        @keyframes loaderSpin {
            to { transform: rotate(360deg); }
        }
        @keyframes letterReveal {
            to { opacity: 1; transform: translateY(0) rotateX(0deg); }
        }
        @keyframes dotPop {
            to { opacity: 1; transform: scale(1); }
        }
        @keyframes tagFade {
            from { opacity: 0; letter-spacing: 0.5em; }
            to   { opacity: 1; letter-spacing: 0.28em; }
        }

        /* === Exit States === */
        .loaded .loader-ring {
            animation: none;
            opacity: 0;
            transform: scale(1.8);
            transition: opacity 0.3s, transform 0.5s cubic-bezier(0.7, 0, 0.3, 1);
        }
        .loaded #loader-wrapper {
            pointer-events: none;
            visibility: hidden;
            transition: visibility 0s 1s;
        }
    </style>
    <script>
        function hidePreloader() {
            if (!document.body.classList.contains('loaded')) {
                document.body.classList.add('loaded');
            }
        }
        document.addEventListener('DOMContentLoaded', function () {
            setTimeout(hidePreloader, 2000);
        });
        window.addEventListener('load', function() {
            setTimeout(hidePreloader, 2000);
        });
        setTimeout(hidePreloader, 4500);
    </script>"""

if OLD_LOADER in content:
    content = content.replace(OLD_LOADER, NEW_LOADER)
    with open('home.html', 'w', encoding='cp1252', errors='xmlcharrefreplace') as f:
        f.write(content)
    print("SUCCESS: Loader screen replaced with cinematic split-reveal preloader")
else:
    # Try to find it by stripping \r
    old_stripped = OLD_LOADER.replace('\r\n', '\n').replace('\r', '')
    content_stripped = content.replace('\r\n', '\n').replace('\r', '')
    if old_stripped in content_stripped:
        content_stripped = content_stripped.replace(old_stripped, NEW_LOADER)
        with open('home.html', 'w', encoding='cp1252', errors='xmlcharrefreplace', newline='') as f:
            f.write(content_stripped)
        print("SUCCESS: Loader screen replaced (normalized line endings)")
    else:
        print("ERROR: Could not find the old loader block.")
        # Debug: show what's around line 517
        lines = content.split('\n')
        for i in range(516, min(526, len(lines))):
            print(f"  Line {i+1}: {repr(lines[i][:100])}")
