with open('home.html', 'r', encoding='cp1252', errors='replace') as fp:
    content = fp.read()

# 1. Update .code-content default rules to hide scrollbars cleanly on modern browsers
old_code_content = """.code-content {
            flex: 1;
            padding: 20px;
            overflow-x: auto;
            overflow-y: visible;
            max-height: none;
            height: auto;
            font-size: 14px;
            line-height: 1.6;
            white-space: pre-wrap;
            word-wrap: break-word;
            color: #c9d1d9;
            font-family: 'Consolas', 'Monaco', 'Courier New', monospace;
        }"""

new_code_content = """.code-content {
            flex: 1;
            padding: 20px;
            overflow-x: auto;
            overflow-y: visible;
            max-height: none;
            height: auto;
            font-size: 14px;
            line-height: 1.6;
            white-space: pre-wrap;
            word-wrap: break-word;
            color: #c9d1d9;
            font-family: 'Consolas', 'Monaco', 'Courier New', monospace;
            scrollbar-width: none; /* Firefox */
            -ms-overflow-style: none; /* IE and Edge */
        }"""

if old_code_content in content:
    content = content.replace(old_code_content, new_code_content, 1)
    print("OK: Added scrollbar-width: none to .code-content")

# 2. Update media query block to eliminate any box scrollbar, hide webkit scrollbars completely on mobile
old_mq = """            /* Body: Line numbers & code content sizing */
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
            }"""

new_mq = """            /* Body: Completely eliminate inner box scrollbar on mobile */
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
            }
            .code-content::-webkit-scrollbar,
            .editor-body::-webkit-scrollbar,
            .code-editor::-webkit-scrollbar {
                display: none !important;
                width: 0 !important;
                height: 0 !important;
                background: transparent !important;
            }"""

if old_mq in content:
    content = content.replace(old_mq, new_mq, 1)
    print("OK: Replaced mobile editor-body styling to remove inner scrollbars")

with open('home.html', 'w', encoding='cp1252', errors='xmlcharrefreplace') as fp:
    fp.write(content)

print("SUCCESS: Inner CV box scrollbar removed on mobile view!")
