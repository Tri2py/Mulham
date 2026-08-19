/**
 * Author: Shadow Themes (modified by Mulham Ibrahim)
 * Author URL: https://shadow-themes.com
 * 
 * Enhanced with:
 * - Honeypot spam protection
 * - Rate limiting (10s cooldown)
 * - Bot detection (time-based)
 * - Input sanitization (strip HTML tags)
 * - XSS-safe response rendering
 * - Accessible form response (aria-live)
 */
"use strict";

// Rate limiting: prevent rapid-fire submissions
let lastSubmitTime = 0;
const SUBMIT_COOLDOWN = 10000; // 10 seconds

// Record form load time (bot detection)
document.addEventListener('DOMContentLoaded', function() {
    var timeField = document.getElementById('formTime');
    if (timeField) timeField.value = Date.now();
});

function Bringer_Contact_Form() {
    // Form Fields
    if ( jQuery('input[name]:not(.is-init), textarea[name]:not(.is-init)').length ) {
        jQuery('input[name]:not(.is-init), textarea[name]:not(.is-init)').each(function() {
            let $this = jQuery(this);
            $this.addClass('is-init');
            $this.on('focus', function() {
                jQuery('label[for="'+ $this.attr('name') +'"]').addClass('in-focus');
            }).on('blur', function() {
                jQuery('label[for="'+ $this.attr('name') +'"]').removeClass('in-focus');
            });
        });
    }

    // Contact Form
    if ( jQuery('.bringer-contact-form:not(.is-init)').length ) {
        jQuery('.bringer-contact-form:not(.is-init)').each(function() {
            let $form = jQuery(this),
                $response = $form.find('.bringer-contact-form__response'),
                formData;

            $response.slideUp(1);
            
            $form.addClass('is-init');
            
            $form.on('submit', function(e) {
                e.preventDefault();
                
                var now = Date.now();

                // Rate limiting
                if (now - lastSubmitTime < SUBMIT_COOLDOWN) {
                    $response.empty()
                             .removeClass('bringer-alert-success')
                             .addClass('bringer-alert-danger')
                             .html('<span>Please wait a moment before submitting again.</span>')
                             .slideDown(200);
                    return;
                }

                // Bot detection: form filled too fast (< 3 seconds)
                var formTime = parseInt(document.getElementById('formTime') ? document.getElementById('formTime').value : 0);
                if (formTime && (now - formTime) < 3000) {
                    return; // Silently reject — likely a bot
                }

                // Honeypot check
                var honeypot = $form.find('input[name="_gotcha"]');
                if (honeypot.length && honeypot.val()) {
                    return; // Bot filled hidden field
                }

                // Client-side sanitization: strip HTML tags
                $form.find('input[type="text"], input[type="email"], textarea').each(function() {
                    var val = jQuery(this).val();
                    if (val) {
                        val = val.replace(/<[^>]*>/g, '');
                        jQuery(this).val(val);
                    }
                });

                lastSubmitTime = now;
                $form.addClass('is-busy');
                $response.slideUp(200);

                // Send Contact Form
                formData = $form.serialize();
                jQuery.ajax({
                    type: 'POST',
                    url: $form.attr('action'),
                    data: formData
                })
                .done(function(response) {
                    $form.removeClass('is-busy');
                    // Sanitize response before rendering (XSS prevention)
                    var safeMessage = typeof response === 'string'
                        ? response.replace(/<[^>]*>/g, '')
                        : 'Message sent successfully!';
                    $response.empty()
                             .removeClass('bringer-alert-danger')
                             .addClass('bringer-alert-success')
                             .html('<span>' + safeMessage + '</span>')
                             .slideDown(200);
                    $form.find('input:not([type="submit"]):not([type="hidden"]), textarea').val('');
                    setTimeout(function() {
                        $response.slideUp(200, function() {
                            jQuery(this).empty();
                        });
                    }, 5000, $response);
                })
                .fail(function(data) {
                    $form.removeClass('is-busy');
                    $response.empty()
                             .removeClass('bringer-alert-success')
                             .addClass('bringer-alert-danger')
                             .html('<span>Something went wrong. Please try again or email me directly at mulhamlol790@gmail.com</span>')
                             .slideDown(200);
                    $form.addClass('is-error');
                    setTimeout(function() {
                        $form.removeClass('is-error');
                    }, 500, $form);
                });

            });
        });
    }
}