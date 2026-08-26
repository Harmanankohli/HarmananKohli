(function() {
  'use strict';

  const COOKIE_CONSENT_KEY = 'cookie_consent';

  function getConsent() {
    return localStorage.getItem(COOKIE_CONSENT_KEY);
  }

  function setConsent(value) {
    localStorage.setItem(COOKIE_CONSENT_KEY, value);
    const banner = document.querySelector('.cookie-banner');
    if (banner) {
      banner.classList.remove('cookie-banner--visible');
    }
  }

  function showBanner() {
    const banner = document.querySelector('.cookie-banner');
    if (banner) {
      banner.classList.add('cookie-banner--visible');
    }
  }

  function respectDoNotTrack() {
    if (navigator.doNotTrack === '1' || window.doNotTrack === '1') {
      return true;
    }
    return false;
  }

  document.addEventListener('DOMContentLoaded', function() {
    if (respectDoNotTrack()) {
      setConsent('rejected');
      return;
    }

    const consent = getConsent();
    if (!consent) {
      showBanner();
    }

    const acceptBtn = document.querySelector('[data-consent="accept"]');
    const rejectBtn = document.querySelector('[data-consent="reject"]');

    if (acceptBtn) {
      acceptBtn.addEventListener('click', function() {
        setConsent('accepted');
      });
    }

    if (rejectBtn) {
      rejectBtn.addEventListener('click', function() {
        setConsent('rejected');
      });
    }
  });
})();
