# -*- coding: utf-8 -*-
import re

with open('contacts.html', 'r', encoding='windows-1252', errors='ignore') as f:
    content = f.read()

old_script = r'''    <!-- Discord Webhook Message Script -->
    <script>
        let msgCooldownActive = false;
        let msgCooldownTimer = null;
        let msgSentCount = 0;

        async function sendDiscordMessage\(e\) \{.*?function resetBtnText\(btn\) \{.*?\}
    </script>'''

# Note: We will replace the whole block by extracting from <!-- Discord Webhook Message Script --> to the closing </script>
old_script_pattern = re.compile(r'<!-- Discord Webhook Message Script -->\s*<script>.*?</script>', re.DOTALL)

new_script = '''    <!-- Discord Webhook Message Script -->
    <script>
        let msgCooldownActive = false;
        let msgCooldownTimer = null;
        let msgSentCount = parseInt(localStorage.getItem('msgSentCount') || '0');

        // Check on load if we are in a cooldown
        document.addEventListener('DOMContentLoaded', () => {
            const cooldownEnd = parseInt(localStorage.getItem('msgCooldownEnd') || '0');
            const now = Date.now();
            if (cooldownEnd > now) {
                const remaining = Math.ceil((cooldownEnd - now) / 1000);
                const btn = document.getElementById('msgSendBtn');
                const statusDiv = document.getElementById('msgStatus');
                const cooldownText = document.getElementById('msgCooldown');
                const statusIcon = document.getElementById('msgStatusIcon');
                const statusText = document.getElementById('msgStatusText');
                
                statusIcon.textContent = '?';
                statusIcon.style.color = '#8C2DF6';
                statusText.textContent = 'You are on cooldown.';
                
                startCooldown(statusDiv, cooldownText, btn, remaining);
            }
        });

        async function sendDiscordMessage(e) {
            e.preventDefault();

            if (msgCooldownActive) return;

            const name = document.getElementById('msgName').value.trim();
            const email = document.getElementById('msgEmail').value.trim();
            const message = document.getElementById('msgContent').value.trim();
            const btn = document.getElementById('msgSendBtn');
            const statusDiv = document.getElementById('msgStatus');
            const statusIcon = document.getElementById('msgStatusIcon');
            const statusText = document.getElementById('msgStatusText');
            const cooldownText = document.getElementById('msgCooldown');

            if (!name || !message) return;

            btn.disabled = true;
            btn.innerHTML = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle></svg> Sending...';

            // Build embed fields
            const fields = [
                { name: '?? Name', value: name, inline: true }
            ];
            if (email) {
                fields.push({ name: '?? Email', value: email, inline: true });
            }
            fields.push({ name: '?? Message', value: message });

            try {
                const response = await fetch('https://discord.com/api/webhooks/1475587623358828704/jm2_P1PHBQu-fOzmwBuNyNdObie8VQq7DXYhpJXdMKJQrFPIhnzDiPMjgvTqred27D6E', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        embeds: [{
                            title: 'New Contact Form Submission',
                            color: 9186806, // #8C2DF6 in decimal
                            fields: fields,
                            timestamp: new Date().toISOString()
                        }]
                    })
                });

                if (response.ok) {
                    msgSentCount++;
                    localStorage.setItem('msgSentCount', msgSentCount);

                    statusIcon.textContent = '?';
                    statusIcon.style.color = '#8C2DF6';
                    statusText.textContent = 'Message sent successfully!';
                    document.getElementById('discordMessageForm').reset();

                    if (msgSentCount >= 2) {
                        // Set cooldown end time in localStorage (120 seconds)
                        const cooldownEnd = Date.now() + 120 * 1000;
                        localStorage.setItem('msgCooldownEnd', cooldownEnd.toString());
                        startCooldown(statusDiv, cooldownText, btn, 120);
                    } else {
                        // First message: just show success briefly
                        statusDiv.style.display = 'flex';
                        cooldownText.textContent = '';
                        setTimeout(() => {
                            statusDiv.style.display = 'none';
                            btn.disabled = false;
                            resetBtnText(btn);
                        }, 2000);
                    }
                } else {
                    statusIcon.textContent = '?';
                    statusIcon.style.color = '#f85149';
                    statusText.textContent = 'Failed to send. Try again later.';
                    statusDiv.style.display = 'flex';
                    setTimeout(() => { statusDiv.style.display = 'none'; btn.disabled = false; resetBtnText(btn); }, 3000);
                }
            } catch (err) {
                statusIcon.textContent = '?';
                statusIcon.style.color = '#f85149';
                statusText.textContent = 'Network error. Please try again.';
                statusDiv.style.display = 'flex';
                setTimeout(() => { statusDiv.style.display = 'none'; btn.disabled = false; resetBtnText(btn); }, 3000);
            }
        }

        function startCooldown(statusDiv, cooldownText, btn, initialRemaining) {
            msgCooldownActive = true;
            btn.disabled = true;
            statusDiv.style.display = 'flex';
            let remaining = initialRemaining;

            function updateTimer() {
                const mins = Math.floor(remaining / 60);
                const secs = remaining % 60;
                cooldownText.textContent = You can send again in :;
                
                if (remaining <= 0) {
                    msgCooldownActive = false;
                    statusDiv.style.display = 'none';
                    cooldownText.textContent = '';
                    btn.disabled = false;
                    resetBtnText(btn);
                    localStorage.removeItem('msgCooldownEnd');
                    return;
                }
                remaining--;
                msgCooldownTimer = setTimeout(updateTimer, 1000);
            }
            updateTimer();
        }

        function resetBtnText(btn) {
            btn.innerHTML = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg> Send';
        }
    </script>'''

content = old_script_pattern.sub(new_script, content)

with open('contacts.html', 'w', encoding='windows-1252') as f:
    f.write(content)

print("Cooldown persists via localStorage!")
