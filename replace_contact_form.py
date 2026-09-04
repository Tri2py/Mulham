with open('contact.html', 'r', encoding='cp1252', errors='replace') as fp:
    content = fp.read()

# 1. Replace the card container
card_start = content.find('<!-- Initiate Contact -->')
col_start = content.rfind('<div class=', 0, card_start)
card_end = content.find('<!-- Email -->')
col_email = content.rfind('<div class=', 0, card_end)

NEW_CARD = """<div class="stg-col-4 stg-tp-col-6 stg-tp-bottom-gap">
                        <!-- Direct Line / Availability Card -->
                        <div class="bringer-block stg-aspect-square stg-vertical-space-between direct-line-card"
                            style="position: relative; overflow: hidden; border: 1px solid rgba(140, 45, 246, 0.22); box-shadow: 0 20px 50px rgba(0,0,0,0.6), inset 0 0 35px rgba(140, 45, 246, 0.06); transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);">
                            
                            <!-- Ambient Background Pulse Glow -->
                            <div style="position: absolute; -webkit-mask-image: radial-gradient(circle, rgba(0,0,0,1) 0%, rgba(0,0,0,0) 70%); mask-image: radial-gradient(circle, rgba(0,0,0,1) 0%, rgba(0,0,0,0) 70%); top: -40px; right: -40px; width: 180px; height: 180px; background: radial-gradient(circle, rgba(140,45,246,0.3) 0%, transparent 70%); filter: blur(25px); pointer-events: none;"></div>

                            <div>
                                <!-- Top status badge: Live availability -->
                                <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 18px;">
                                    <span style="font-family: 'Inter', sans-serif; font-size: 0.65rem; font-weight: 600; letter-spacing: 0.22em; text-transform: uppercase; color: rgba(255,255,255,0.4);">Direct Line</span>
                                    <div style="display: inline-flex; align-items: center; gap: 7px; background: rgba(35, 134, 54, 0.15); border: 1px solid rgba(46, 160, 67, 0.35); padding: 4px 10px; border-radius: 99px;">
                                        <span style="width: 7px; height: 7px; border-radius: 50%; background: #3fb950; box-shadow: 0 0 8px #3fb950; display: inline-block; animation: statusPulse 2s infinite ease-in-out;"></span>
                                        <span style="font-family: 'Inter', sans-serif; font-size: 0.65rem; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; color: #7ee787;">Available</span>
                                    </div>
                                </div>
                                
                                <h5 style="margin-bottom: 8px;">Studio Status<span class="bringer-accent">.</span></h5>
                                <p style="color: rgba(255,255,255,0.6); font-size: 0.92rem; line-height: 1.6; margin: 0;">Accepting select commissions for digital experiences, brand architecture, and bespoke web design.</p>
                            </div>

                            <!-- Interactive Quick Action Buttons -->
                            <div style="display: flex; flex-direction: column; gap: 10px; margin-top: 18px; position: relative; z-index: 2;">
                                <!-- Primary Action: Send Inquiry via Email -->
                                <a href="mailto:mulhamlol790@gmail.com?subject=Project%20Inquiry%20-%20Mulham%20Studio"
                                   style="display: flex; align-items: center; justify-content: space-between; padding: 13px 18px; background: linear-gradient(135deg, rgba(140,45,246,0.3) 0%, rgba(140,45,246,0.12) 100%); border: 1px solid rgba(140,45,246,0.45); border-radius: 12px; color: #ffffff; text-decoration: none; font-family: 'Inter', sans-serif; font-size: 0.84rem; font-weight: 600; letter-spacing: 0.02em; transition: all 0.3s ease; box-shadow: 0 6px 20px rgba(140,45,246,0.18);"
                                   onmouseover="this.style.transform='translateY(-2px)'; this.style.borderColor='rgba(140,45,246,0.8)'; this.style.boxShadow='0 10px 25px rgba(140,45,246,0.35)';"
                                   onmouseout="this.style.transform='none'; this.style.borderColor='rgba(140,45,246,0.45)'; this.style.boxShadow='0 6px 20px rgba(140,45,246,0.18)';">
                                    <span style="display: flex; align-items: center; gap: 10px;">
                                        <i class="ph-fill ph-paper-plane-tilt" style="font-size: 1.1rem; color: #b066ff;"></i>
                                        Send Project Inquiry
                                    </span>
                                    <i class="ph-bold ph-arrow-up-right" style="font-size: 0.9rem; color: rgba(255,255,255,0.7);"></i>
                                </a>

                                <!-- Secondary Action: Instant Telegram / Chat link -->
                                <button onclick="copyEmailAddress(this)"
                                        style="display: flex; align-items: center; justify-content: space-between; padding: 11px 18px; background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.09); border-radius: 12px; color: rgba(255,255,255,0.75); font-family: 'Inter', sans-serif; font-size: 0.8rem; font-weight: 500; cursor: pointer; transition: all 0.25s ease;"
                                        onmouseover="this.style.background='rgba(255,255,255,0.08)'; this.style.borderColor='rgba(255,255,255,0.2)'; this.style.color='#fff';"
                                        onmouseout="this.style.background='rgba(255,255,255,0.04)'; this.style.borderColor='rgba(255,255,255,0.09)'; this.style.color='rgba(255,255,255,0.75)';">
                                    <span style="display: flex; align-items: center; gap: 9px;">
                                        <i class="ph-fill ph-copy" style="font-size: 1rem; color: #8C2DF6;"></i>
                                        <span class="copy-label">Copy Direct Email</span>
                                    </span>
                                    <span style="font-size: 0.72rem; color: rgba(255,255,255,0.35); font-family: monospace;">1-CLICK</span>
                                </button>
                            </div>
                        </div>
                    </div>
                    """

content = content[:col_start] + NEW_CARD + content[col_email:]

# 2. Remove the old discord script and replace with quick copy script + pulse animation
idx_script = content.find('let msgCooldownActive = false;')
if idx_script != -1:
    script_start = content.rfind('<script', 0, idx_script)
    end_script = content.find('<!-- High-Performance Reveal', idx_script)
    
    NEW_SCRIPT = """<style>
        @keyframes statusPulse {
            0%, 100% { transform: scale(1); opacity: 1; }
            50% { transform: scale(1.4); opacity: 0.55; }
        }
        .direct-line-card:hover {
            transform: translateY(-4px);
            border-color: rgba(140, 45, 246, 0.45) !important;
            box-shadow: 0 25px 60px rgba(140, 45, 246, 0.15), inset 0 0 45px rgba(140, 45, 246, 0.09) !important;
        }
    </style>
    <script>
        function copyEmailAddress(btn) {
            const email = 'mulhamlol790@gmail.com';
            navigator.clipboard.writeText(email).then(() => {
                const label = btn.querySelector('.copy-label');
                const prevText = label.textContent;
                label.textContent = 'Copied to Clipboard!';
                btn.style.borderColor = 'rgba(63, 185, 80, 0.6)';
                btn.style.color = '#7ee787';
                setTimeout(() => {
                    label.textContent = prevText;
                    btn.style.borderColor = '';
                    btn.style.color = '';
                }, 2200);
            });
        }
    </script>
    """
    content = content[:script_start] + NEW_SCRIPT + content[end_script:]

with open('contact.html', 'w', encoding='cp1252', errors='xmlcharrefreplace') as fp:
    fp.write(content)

print("SUCCESS: Upgraded contact card to high-end Direct Line / Studio Status card")
