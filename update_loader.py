import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_loader = '''    <!-- Ultra-Premium Monolithic Preloader -->
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
    </script>'''

# Regex to replace everything from <!-- Preloader --> up to <!-- Premium Glassmorphism Navbar -->
pattern = re.compile(r'<!-- Preloader -->.*?<!-- Premium Glassmorphism Navbar -->', re.DOTALL)
new_content = pattern.sub(f'{new_loader}\n\n    <!-- Premium Glassmorphism Navbar -->', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Loader Updated!")
