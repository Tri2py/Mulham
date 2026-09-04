import os

with open('home.html', 'r', encoding='cp1252', errors='replace') as f:
    content = f.read()

# ═══════════════════════════════════════════
# ENHANCEMENT 1: Upgrade the CV section HTML
# ═══════════════════════════════════════════

OLD_CV_HTML = """<!-- Section: CV Preview -->
            <section id="cv-preview" class="cv-preview-section" style="margin-top: 20vh; margin-bottom: 15vh;">
                <div class="stg-row bringer-section-title">
                    <div class="stg-col-8">
                        <div class="align-left">
                            <h2  style="font-family: 'Playfair Display', serif; font-size: clamp(2.5rem, 6vw, 4.5rem); font-weight: 400; letter-spacing: -0.02em; line-height: 1.1; margin-bottom: 24px;">
                                Curriculum <span style="font-style: italic; color: var(--bringer-s-text);">Vitae</span>
                            </h2>
                            <!-- Gradient arrow -->
                            <div   style="margin-top: 16px;">
                                <svg width="48" height="48" viewBox="0 0 24 24" fill="none"
                                    xmlns="http://www.w3.org/2000/svg"
                                    style="animation: cvArrowBounce 2s ease-in-out infinite;">
                                    <defs>
                                        <linearGradient id="cvArrowGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                                            <stop offset="0%" style="stop-color:#8C2DF6" />
                                            <stop offset="100%" style="stop-color:#8C2DF6" />
                                        </linearGradient>
                                    </defs>
                                    <path d="M7 10l5 5 5-5" stroke="url(#cvArrowGrad)" stroke-width="3"
                                        stroke-linecap="round" stroke-linejoin="round" />
                                </svg>
                            </div>
                            <style>
                                @keyframes cvArrowBounce {

                                    0%,
                                    100% {
                                        transform: translateY(0);
                                    }

                                    50% {
                                        transform: translateY(6px);
                                    }
                                }
                            </style>
                        </div>
                    </div>
                </div>
                <div class="cv-preview-container">
                    <div class="code-editor">
                        <div class="editor-header">
                            <div class="window-buttons">
                                <div class="window-btn btn-close"></div>
                                <div class="window-btn btn-minimize"></div>
                                <div class="window-btn btn-maximize"></div>
                            </div>
                            <div class="file-tabs"
                                style="flex: 1; display: flex; align-items: center; justify-content: space-between;">
                                <div class="file-tab">
                                    <span class="file-tab-icon">JS</span>
                                    mulham_ibrahim_cv.js
                                </div>
                            </div>
                        </div>
                        <div class="editor-body" id="codeView" style="display: flex;">
                            <div class="line-numbers" id="lineNumbers"></div>
                            <div class="code-content" id="codeContent">
                                <div class="loading">Loading CV...</div>
                            </div>
                        </div>
                    </div>


                </div>
            </section>"""

NEW_CV_HTML = """<!-- Section: CV Preview (Enhanced) -->
            <section id="cv-preview" class="cv-preview-section" style="margin-top: 20vh; margin-bottom: 15vh;">
                <div class="stg-row bringer-section-title">
                    <div class="stg-col-8">
                        <div class="align-left">
                            <span style="display: inline-block; font-family: 'Inter', sans-serif; font-size: 0.65rem; font-weight: 600; letter-spacing: 0.25em; text-transform: uppercase; color: #8C2DF6; margin-bottom: 16px; opacity: 0.8;">About Me</span>
                            <h2 style="font-family: 'Playfair Display', serif; font-size: clamp(2.5rem, 6vw, 4.5rem); font-weight: 400; letter-spacing: -0.02em; line-height: 1.1; margin-bottom: 16px;">
                                Curriculum <span style="font-style: italic; color: var(--bringer-s-text);">Vitae</span>
                            </h2>
                            <p style="color: rgba(255,255,255,0.4); font-family: 'Inter', sans-serif; font-size: 0.88rem; line-height: 1.7; max-width: 480px; margin-bottom: 32px;">My journey rendered as code &mdash; hover over the editor to explore.</p>
                        </div>
                    </div>
                </div>
                <div class="cv-preview-container">
                    <div class="code-editor" id="cv-editor">

                        <!-- Editor Header -->
                        <div class="editor-header">
                            <div class="window-buttons">
                                <div class="window-btn btn-close"></div>
                                <div class="window-btn btn-minimize"></div>
                                <div class="window-btn btn-maximize"></div>
                            </div>
                            <div class="file-tabs" style="flex: 1; display: flex; align-items: center; justify-content: space-between;">
                                <div style="display: flex; align-items: center; gap: 8px;">
                                    <div class="file-tab">
                                        <span class="file-tab-icon">JS</span>
                                        mulham_ibrahim_cv.js
                                    </div>
                                </div>
                                <!-- Action Buttons -->
                                <div style="display: flex; gap: 8px; align-items: center;">
                                    <button onclick="copyCVToClipboard()" class="cv-action-btn" title="Copy to clipboard" style="background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08); border-radius: 6px; padding: 6px 10px; cursor: pointer; color: rgba(255,255,255,0.45); font-size: 12px; display: flex; align-items: center; gap: 6px; transition: all 0.2s ease; font-family: 'Inter', sans-serif;">
                                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
                                        Copy
                                    </button>
                                    <button onclick="downloadCVAsPDF()" class="cv-action-btn" title="Download as PDF" style="background: rgba(140,45,246,0.1); border: 1px solid rgba(140,45,246,0.2); border-radius: 6px; padding: 6px 10px; cursor: pointer; color: rgba(255,255,255,0.55); font-size: 12px; display: flex; align-items: center; gap: 6px; transition: all 0.2s ease; font-family: 'Inter', sans-serif;">
                                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
                                        PDF
                                    </button>
                                </div>
                            </div>
                        </div>

                        <!-- Editor Body -->
                        <div class="editor-body" id="codeView" style="display: flex;">
                            <div class="line-numbers" id="lineNumbers"></div>
                            <div class="code-content" id="codeContent">
                                <div class="loading">Loading CV...</div>
                            </div>
                        </div>

                        <!-- Status Bar (VS Code style) -->
                        <div class="cv-status-bar">
                            <div class="cv-status-left">
                                <span class="cv-status-item" style="background: rgba(140,45,246,0.25); padding: 0 8px; border-radius: 0 2px 2px 0;">
                                    <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M15 22v-4a4.8 4.8 0 0 0-1-3.5c3 0 6-2 6-5.5.08-1.25-.27-2.48-1-3.5.28-1.15.28-2.35 0-3.5 0 0-1 0-3 1.5-2.64-.5-5.36-.5-8 0C6 2 5 2 5 2c-.3 1.15-.3 2.35 0 3.5A5.403 5.403 0 0 0 4 9c0 3.5 3 5.5 6 5.5-.39.49-.68 1.05-.85 1.65-.17.6-.22 1.23-.15 1.85v4"></path><path d="M9 18c-4.51 2-5-2-7-2"></path></svg>
                                    main
                                </span>
                                <span class="cv-status-item">
                                    <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle></svg>
                                    0 problems
                                </span>
                            </div>
                            <div class="cv-status-right">
                                <span class="cv-status-item" id="cvLineInfo">Ln 1, Col 1</span>
                                <span class="cv-status-item">UTF-8</span>
                                <span class="cv-status-item">JavaScript</span>
                            </div>
                        </div>
                    </div>
                </div>
            </section>"""

if OLD_CV_HTML in content:
    content = content.replace(OLD_CV_HTML, NEW_CV_HTML)
    print("OK: CV HTML replaced")
else:
    old_n = OLD_CV_HTML.replace('\r\n', '\n').replace('\r', '')
    content_n = content.replace('\r\n', '\n').replace('\r', '')
    if old_n in content_n:
        content_n = content_n.replace(old_n, NEW_CV_HTML)
        content = content_n
        print("OK: CV HTML replaced (normalized)")
    else:
        print("ERROR: Could not find old CV HTML block")
        exit(1)


# ═══════════════════════════════════════════
# ENHANCEMENT 2: Add enhanced styles to the CSS
# ═══════════════════════════════════════════

# Insert new styles before the closing </style> of the CV style block (line ~507)
OLD_STYLE_END = """        /* Smooth scroll */
        html {
            scroll-behavior: smooth;
        }

    </style>"""

NEW_STYLE_END = """        /* Smooth scroll */
        html {
            scroll-behavior: smooth;
        }

        /* ── Enhanced CV Editor Styles ── */

        /* Editor hover glow */
        .code-editor {
            transition: border-color 0.5s ease, box-shadow 0.5s ease;
        }
        .code-editor:hover {
            border-color: rgba(140, 45, 246, 0.35);
            box-shadow: 0 30px 100px rgba(0, 0, 0, 0.8), 
                        inset 0 0 40px rgba(140, 45, 246, 0.05),
                        0 0 60px rgba(140, 45, 246, 0.08);
        }

        /* Active line highlight */
        .code-content .cv-line {
            display: block;
            padding: 0 4px;
            margin: 0 -4px;
            border-radius: 3px;
            transition: background 0.15s ease;
        }
        .code-content .cv-line:hover {
            background: rgba(140, 45, 246, 0.06);
        }

        /* Status bar */
        .cv-status-bar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0 8px;
            height: 26px;
            background: rgba(140, 45, 246, 0.08);
            border-top: 1px solid rgba(255, 255, 255, 0.04);
            font-family: 'Inter', -apple-system, sans-serif;
            font-size: 11px;
            color: rgba(255, 255, 255, 0.45);
        }
        .cv-status-left, .cv-status-right {
            display: flex;
            align-items: center;
            gap: 2px;
        }
        .cv-status-item {
            display: flex;
            align-items: center;
            gap: 5px;
            padding: 0 6px;
            height: 26px;
            transition: background 0.15s ease;
            cursor: default;
            white-space: nowrap;
        }
        .cv-status-item:hover {
            background: rgba(255, 255, 255, 0.06);
        }
        .cv-status-item svg {
            opacity: 0.7;
        }

        /* Action buttons */
        .cv-action-btn:hover {
            background: rgba(140, 45, 246, 0.2) !important;
            border-color: rgba(140, 45, 246, 0.35) !important;
            color: #fff !important;
        }

        /* Typewriter cursor blink */
        .cv-cursor {
            display: inline-block;
            width: 2px;
            height: 1em;
            background: #8C2DF6;
            margin-left: 2px;
            animation: cvBlink 1s step-end infinite;
            vertical-align: text-bottom;
        }
        @keyframes cvBlink {
            50% { opacity: 0; }
        }

        /* Scroll-triggered fade-in for editor */
        .cv-editor-reveal {
            opacity: 0;
            transform: translateY(40px);
            transition: opacity 0.8s cubic-bezier(0.16, 1, 0.3, 1), 
                        transform 0.8s cubic-bezier(0.16, 1, 0.3, 1);
        }
        .cv-editor-reveal.visible {
            opacity: 1;
            transform: translateY(0);
        }

        /* Responsive status bar */
        @media (max-width: 600px) {
            .cv-status-bar {
                font-size: 10px;
            }
            .cv-status-right .cv-status-item:not(:last-child) {
                display: none;
            }
            .cv-action-btn span {
                display: none;
            }
        }

    </style>"""

if OLD_STYLE_END in content:
    content = content.replace(OLD_STYLE_END, NEW_STYLE_END)
    print("OK: Enhanced styles added")
else:
    old_n = OLD_STYLE_END.replace('\r\n', '\n').replace('\r', '')
    content_n = content.replace('\r\n', '\n').replace('\r', '')
    if old_n in content_n:
        content_n = content_n.replace(old_n, NEW_STYLE_END)
        content = content_n
        print("OK: Enhanced styles added (normalized)")
    else:
        print("ERROR: Could not find style end block")
        exit(1)


# ═══════════════════════════════════════════
# ENHANCEMENT 3: Add enhanced JS functions
# ═══════════════════════════════════════════

# Add new JS functions right before the loadCV function
OLD_LOAD_CV = """        // Load CV content
        function loadCV() {"""

NEW_LOAD_CV = """        // Copy CV text to clipboard
        function copyCVToClipboard() {
            const btn = event.currentTarget;
            const text = cvMarkdownContent.replace(/[#*\\-]/g, '').replace(/\\n{3,}/g, '\\n\\n').trim();
            navigator.clipboard.writeText(text).then(() => {
                const origHTML = btn.innerHTML;
                btn.innerHTML = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#3fb950" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg> Copied!';
                btn.style.borderColor = 'rgba(63, 185, 80, 0.4)';
                btn.style.color = '#3fb950';
                setTimeout(() => {
                    btn.innerHTML = origHTML;
                    btn.style.borderColor = '';
                    btn.style.color = '';
                }, 2000);
            });
        }

        // Download CV as formatted PDF (opens print dialog)
        function downloadCVAsPDF() {
            const printWindow = window.open('', '_blank');
            const htmlContent = convertMarkdownToHTML(cvMarkdownContent);
            printWindow.document.write(`<!DOCTYPE html><html><head><title>Mulham Ibrahim - CV</title>
            <style>
                body { font-family: 'Segoe UI', Arial, sans-serif; max-width: 700px; margin: 40px auto; color: #1a1a1a; line-height: 1.7; padding: 0 20px; }
                h1 { font-size: 28px; margin: 0 0 4px 0; color: #111; }
                h2 { font-size: 16px; color: #8C2DF6; text-transform: uppercase; letter-spacing: 0.08em; margin: 28px 0 12px; border-bottom: 1px solid #eee; padding-bottom: 6px; }
                h3 { font-size: 14px; margin: 14px 0 6px; }
                p { margin: 0 0 6px; color: #333; font-size: 14px; }
                ul { margin: 6px 0 14px 18px; padding: 0; }
                li { margin-bottom: 4px; color: #333; font-size: 14px; }
                hr { border: none; border-top: 1px solid #ddd; margin: 16px 0; }
                strong { color: #111; }
                @media print { body { margin: 0; padding: 20px; } }
            </style></head><body>${htmlContent}</body></html>`);
            printWindow.document.close();
            setTimeout(() => printWindow.print(), 300);
        }

        // Scroll-reveal for editor
        function initCVReveal() {
            const editor = document.getElementById('cv-editor');
            if (!editor) return;
            editor.classList.add('cv-editor-reveal');

            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        editor.classList.add('visible');
                        observer.unobserve(entry.target);
                    }
                });
            }, { threshold: 0.15 });
            observer.observe(editor);
        }

        // Track line info in status bar
        function initLineTracking() {
            const codeContent = document.getElementById('codeContent');
            if (!codeContent) return;

            codeContent.addEventListener('mousemove', function(e) {
                const lineHeight = parseFloat(getComputedStyle(codeContent).lineHeight) || 22.4;
                const scrollTop = codeContent.scrollTop;
                const rect = codeContent.getBoundingClientRect();
                const y = e.clientY - rect.top + scrollTop;
                const lineNum = Math.max(1, Math.ceil(y / lineHeight));
                const info = document.getElementById('cvLineInfo');
                if (info) info.textContent = 'Ln ' + lineNum + ', Col 1';
            });
        }

        // Load CV content
        function loadCV() {"""

if OLD_LOAD_CV in content:
    content = content.replace(OLD_LOAD_CV, NEW_LOAD_CV)
    print("OK: Enhanced JS functions added")
else:
    print("ERROR: Could not find loadCV function")
    exit(1)


# ═══════════════════════════════════════════
# ENHANCEMENT 4: Call init functions after loadCV
# ═══════════════════════════════════════════

OLD_LOAD_CALL = "console.log('CV loaded successfully');"
NEW_LOAD_CALL = """console.log('CV loaded successfully');
                initCVReveal();
                initLineTracking();"""

if OLD_LOAD_CALL in content:
    content = content.replace(OLD_LOAD_CALL, NEW_LOAD_CALL, 1)
    print("OK: Init calls added")
else:
    print("WARN: Could not find console.log call for init")


# ═══════════════════════════════════════════
# Write the file
# ═══════════════════════════════════════════

with open('home.html', 'w', encoding='cp1252', errors='xmlcharrefreplace') as f:
    f.write(content)

print(f"\nFile size: {os.path.getsize('home.html')} bytes")
print("DONE: All CV enhancements applied")
