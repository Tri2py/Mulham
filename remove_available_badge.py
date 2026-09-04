with open('contact.html', 'r', encoding='cp1252', errors='replace') as fp:
    content = fp.read()

old_badge_block = """<!-- Top status badge: Live availability -->
                                <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 18px;">
                                    <span style="font-family: 'Inter', sans-serif; font-size: 0.65rem; font-weight: 600; letter-spacing: 0.22em; text-transform: uppercase; color: rgba(255,255,255,0.4);">Direct Line</span>
                                    <div style="display: inline-flex; align-items: center; gap: 7px; background: rgba(35, 134, 54, 0.15); border: 1px solid rgba(46, 160, 67, 0.35); padding: 4px 10px; border-radius: 99px;">
                                        <span style="width: 7px; height: 7px; border-radius: 50%; background: #3fb950; box-shadow: 0 0 8px #3fb950; display: inline-block; animation: statusPulse 2s infinite ease-in-out;"></span>
                                        <span style="font-family: 'Inter', sans-serif; font-size: 0.65rem; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; color: #7ee787;">Available</span>
                                    </div>
                                </div>"""

new_badge_block = """<!-- Top Tag -->
                                <div style="display: flex; align-items: center; margin-bottom: 16px;">
                                    <span style="font-family: 'Inter', sans-serif; font-size: 0.65rem; font-weight: 600; letter-spacing: 0.22em; text-transform: uppercase; color: #8C2DF6;">Direct Line</span>
                                </div>"""

# Normalize line endings for replacement
content_norm = content.replace('\r\n', '\n')
old_norm = old_badge_block.replace('\r\n', '\n')
new_norm = new_badge_block.replace('\r\n', '\n')

if old_norm in content_norm:
    content_norm = content_norm.replace(old_norm, new_norm, 1)
    with open('contact.html', 'w', encoding='cp1252', errors='xmlcharrefreplace') as fp:
        fp.write(content_norm)
    print("SUCCESS: Removed 'Available' badge from the card in contact.html")
else:
    print("ERROR: Badge block not found")
