with open('home.html', 'r', encoding='cp1252', errors='replace') as fp:
    content = fp.read()

# Replace the media query block at the end of the CV style section with a complete, robust mobile suite
old_cv_mq = """        /* Responsive status bar */
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
        }"""

new_cv_mq = """        /* === Comprehensive CV Mobile & Tablet Optimization === */
        @media (max-width: 768px) {
            /* Section padding & spacing */
            .cv-preview-section {
                margin-top: 10vh !important;
                margin-bottom: 8vh !important;
                padding: 0 !important;
            }
            .cv-preview-container {
                padding: 0 4px;
            }

            /* Code Editor frame on mobile */
            .code-editor {
                border-radius: 12px !important;
                box-shadow: 0 15px 40px rgba(0, 0, 0, 0.9), inset 0 0 25px rgba(140, 45, 246, 0.05) !important;
            }

            /* Header: simplify tab and buttons for small touch screens */
            .editor-header {
                padding: 10px 14px !important;
            }
            .window-buttons {
                gap: 5px !important;
            }
            .window-btn {
                width: 9px !important;
                height: 9px !important;
            }
            .file-tabs {
                margin-left: 8px !important;
            }
            .file-tab {
                padding: 4px 10px !important;
                font-size: 11px !important;
                border-radius: 5px 5px 0 0 !important;
            }
            .cv-action-btn {
                padding: 5px 8px !important;
                font-size: 11px !important;
            }

            /* Body: Line numbers & code content sizing */
            .editor-body {
                overflow-x: auto;
                -webkit-overflow-scrolling: touch;
            }
            .line-numbers {
                min-width: 34px !important;
                padding: 14px 0 !important;
                font-size: 11px !important;
                line-height: 1.55 !important;
            }
            .line-number {
                padding: 0 6px !important;
            }
            .code-content {
                padding: 14px 12px !important;
                font-size: 11.5px !important;
                line-height: 1.55 !important;
                word-break: break-word !important;
                white-space: pre-wrap !important;
            }

            /* Status Bar compact on mobile */
            .cv-status-bar {
                height: 24px !important;
                padding: 0 6px !important;
                font-size: 9.5px !important;
            }
            .cv-status-item {
                height: 24px !important;
                padding: 0 4px !important;
            }
            .cv-status-right .cv-status-item:not(:last-child) {
                display: none !important;
            }
        }

        @media (max-width: 480px) {
            .file-tab {
                max-width: 130px;
                overflow: hidden;
                text-overflow: ellipsis;
                white-space: nowrap;
            }
            .line-numbers {
                min-width: 28px !important;
            }
            .line-number {
                padding: 0 4px !important;
            }
            .code-content {
                padding: 12px 8px !important;
                font-size: 11px !important;
            }
        }"""

content_norm = content.replace('\r\n', '\n')
old_mq_norm = old_cv_mq.replace('\r\n', '\n')
new_mq_norm = new_cv_mq.replace('\r\n', '\n')

if old_mq_norm in content_norm:
    content_norm = content_norm.replace(old_mq_norm, new_mq_norm, 1)
    with open('home.html', 'w', encoding='cp1252', errors='xmlcharrefreplace') as fp:
        fp.write(content_norm)
    print("SUCCESS: Enhanced CV preview mobile view in home.html")
else:
    print("ERROR: old_cv_mq target block not found")
