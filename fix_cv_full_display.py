with open('home.html', 'r', encoding='cp1252', errors='replace') as fp:
    content = fp.read()

# 1. Clean up the Editor Header: remove copy and download buttons, keep sleek title tab & window controls
old_header = """                        <!-- Editor Header -->
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
                        </div>"""

new_header = """                        <!-- Editor Header -->
                        <div class="editor-header">
                            <div class="window-buttons">
                                <div class="window-btn btn-close"></div>
                                <div class="window-btn btn-minimize"></div>
                                <div class="window-btn btn-maximize"></div>
                            </div>
                            <div class="file-tabs" style="flex: 1; display: flex; align-items: center;">
                                <div class="file-tab">
                                    <span class="file-tab-icon">JS</span>
                                    mulham_ibrahim_cv.js
                                </div>
                            </div>
                        </div>"""

# 2. Update subtitle to remove "hover over the editor to explore" if desired or keep clean
old_sub = '<p style="color: rgba(255,255,255,0.4); font-family: \'Inter\', sans-serif; font-size: 0.88rem; line-height: 1.7; max-width: 480px; margin-bottom: 32px;">My journey rendered as code &mdash; hover over the editor to explore.</p>'
new_sub = '<p style="color: rgba(255,255,255,0.45); font-family: \'Inter\', sans-serif; font-size: 0.88rem; line-height: 1.7; max-width: 480px; margin-bottom: 32px;">Professional background, capabilities, and track record rendered as code.</p>'

content_norm = content.replace('\r\n', '\n')
old_header_norm = old_header.replace('\r\n', '\n')
new_header_norm = new_header.replace('\r\n', '\n')

if old_header_norm in content_norm:
    content_norm = content_norm.replace(old_header_norm, new_header_norm, 1)
    print("OK: Removed copy and download buttons from editor header")
else:
    print("WARN: Header block not matched directly")

if old_sub in content_norm:
    content_norm = content_norm.replace(old_sub, new_sub, 1)
    print("OK: Updated CV subtitle")

# 3. Fix the full-height visibility of the CV:
# Update the CSS rules so .code-editor, .editor-body, and .code-content are fully expanded on mobile with line-height sync
old_css_mq = """            /* Body: Completely eliminate inner box scrollbar on mobile */
            .editor-body {
                overflow: hidden !important;
            }
            .line-numbers {
                min-width: 32px !important;
                padding: 14px 0 !important;
                font-size: 11px !important;
                line-height: 1.55 !important;
            }
            .line-number {
                padding: 0 5px !important;
            }
            .code-content {
                padding: 14px 10px !important;
                font-size: 11.5px !important;
                line-height: 1.55 !important;
                word-break: break-word !important;
                white-space: pre-wrap !important;
                overflow: hidden !important;
                scrollbar-width: none !important;
                -ms-overflow-style: none !important;
            }"""

new_css_mq = """            /* Body: Full Height Unclipped Flow on Mobile */
            .code-editor {
                height: auto !important;
                max-height: none !important;
                overflow: visible !important;
            }
            .editor-body {
                height: auto !important;
                max-height: none !important;
                overflow: visible !important;
                display: flex !important;
            }
            .line-numbers {
                min-width: 32px !important;
                padding: 16px 0 !important;
                font-size: 11px !important;
                line-height: 1.6 !important;
                height: auto !important;
            }
            .line-number {
                padding: 0 5px !important;
                line-height: 1.6 !important;
            }
            .code-content {
                padding: 16px 12px !important;
                font-size: 11.5px !important;
                line-height: 1.6 !important;
                word-break: break-word !important;
                white-space: pre-wrap !important;
                height: auto !important;
                max-height: none !important;
                overflow: visible !important;
                scrollbar-width: none !important;
                -ms-overflow-style: none !important;
            }"""

old_css_mq_n = old_css_mq.replace('\r\n', '\n')
new_css_mq_n = new_css_mq.replace('\r\n', '\n')

if old_css_mq_n in content_norm:
    content_norm = content_norm.replace(old_css_mq_n, new_css_mq_n, 1)
    print("OK: Replaced mobile CSS to ensure full height unclipped display")
else:
    print("WARN: old_css_mq not matched directly")

# 4. Remove copyCVToClipboard and downloadCVAsPDF functions from JS since buttons are removed
old_js_funcs = """        // Copy CV text to clipboard
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
        }"""

old_js_funcs_n = old_js_funcs.replace('\r\n', '\n')
if old_js_funcs_n in content_norm:
    content_norm = content_norm.replace(old_js_funcs_n, '', 1)
    print("OK: Removed unused copy/download JS functions")

with open('home.html', 'w', encoding='cp1252', errors='xmlcharrefreplace') as fp:
    fp.write(content_norm)

print("SUCCESS: Completed CV update in home.html!")
