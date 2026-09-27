/**
 * Agastya Nadi Jyotish - Main JavaScript
 * Handles: Mobile menu toggle, FAQ Accordion, Form Validation & Analytics Hooks
 */

document.addEventListener('DOMContentLoaded', function() {
  // 1. Mobile Menu Toggle
  const mobileToggle = document.getElementById('mobile-toggle');
  const mainNav = document.getElementById('main-nav');
  
  if (mobileToggle && mainNav) {
    mobileToggle.addEventListener('click', function() {
      const isExpanded = mobileToggle.getAttribute('aria-expanded') === 'true';
      mobileToggle.setAttribute('aria-expanded', !isExpanded);
      mainNav.classList.toggle('show');
    });
  }

  // 2. FAQ Accordion
  const faqQuestions = document.querySelectorAll('.faq-question');
  faqQuestions.forEach(function(button) {
    button.addEventListener('click', function() {
      const faqItem = button.parentElement;
      const isActive = faqItem.classList.contains('active');
      
      // Close all other active FAQ items in the same container
      const parentContainer = faqItem.closest('.faq-list');
      if (parentContainer) {
        parentContainer.querySelectorAll('.faq-item.active').forEach(function(item) {
          if (item !== faqItem) item.classList.remove('active');
        });
      }
      
      faqItem.classList.toggle('active');
    });
  });

  // 3. Consultation Booking Form Validation & Analytics Trigger
  const bookingForm = document.getElementById('booking-form');
  if (bookingForm) {
    bookingForm.addEventListener('submit', function(e) {
      const nameInput = document.getElementById('full-name');
      const phoneInput = document.getElementById('phone-number');
      const emailInput = document.getElementById('email-address');
      const consentCheck = document.getElementById('consent-check');

      let isValid = true;
      let errorMsg = [];

      if (nameInput && !nameInput.value.trim()) {
        isValid = false;
        errorMsg.push('Please enter your full name.');
      }

      if (phoneInput && !phoneInput.value.trim()) {
        isValid = false;
        errorMsg.push('Please enter a valid phone or WhatsApp number.');
      }

      if (consentCheck && !consentCheck.checked) {
        isValid = false;
        errorMsg.push('Please check the consent box to proceed.');
      }

      if (!isValid) {
        e.preventDefault();
        alert(errorMsg.join('\n'));
      } else {
        // Event tracking trigger if GA4 gtag is present
        if (typeof gtag === 'function') {
          gtag('event', 'generate_lead', {
            'event_category': 'Booking',
            'event_label': 'Consultation Booking Form Submitted'
          });
        }
      }
    });
  }

  // 4. Analytics Hooks for CTA Buttons
  const whatsappBtns = document.querySelectorAll('.btn-whatsapp, a[href*="wa.me"]');
  whatsappBtns.forEach(function(btn) {
    btn.addEventListener('click', function() {
      if (typeof gtag === 'function') {
        gtag('event', 'click_whatsapp', {
          'event_category': 'Contact',
          'event_label': 'WhatsApp CTA Click'
        });
      }
    });
  });

  const phoneBtns = document.querySelectorAll('a[href^="tel:"]');
  phoneBtns.forEach(function(btn) {
    btn.addEventListener('click', function() {
      if (typeof gtag === 'function') {
        gtag('event', 'click_phone', {
          'event_category': 'Contact',
          'event_label': 'Phone Call CTA Click'
        });
      }
    });
  });
});
