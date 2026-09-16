# -*- coding: utf-8 -*-
import os

js_code = """/**
 * TEMiZO (تميزو) - Main Interactive Script
 * High performance Vanilla JavaScript
 * Instant & All-Istanbul Coverage (European & Asian sides)
 */

// Global App State
let currentAppLang = 'ar';
const OFFICIAL_PHONE = '905435110530';

document.addEventListener('DOMContentLoaded', () => {
  initThreeJsBubbleScene();
  initBubbleCursor();
  init3DCardTilt();
  initNavbarAndDrawer();
  initHeroSwitcher();
  initCalculator();
  initBeforeAfterSlider();
  initCoverageDistricts();
  initFaqAccordion();
  initWhatsAppWidget();
  initBackToTop();
  initLanguageSwitcher();
});

/* ==========================================================================
   1. Navbar, Sticky Header & Mobile Drawer
   ========================================================================== */
function initNavbarAndDrawer() {
  const header = document.querySelector('.site-header');
  const drawerOpenBtn = document.getElementById('drawerOpenBtn');
  const drawerCloseBtn = document.getElementById('drawerCloseBtn');
  const mobileDrawer = document.getElementById('mobileDrawer');
  const drawerBackdrop = document.getElementById('drawerBackdrop');
  const drawerLinks = document.querySelectorAll('.drawer-nav-link');

  // Sticky header shadow
  window.addEventListener('scroll', () => {
    if (window.scrollY > 40) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  });

  function openDrawer() {
    if (mobileDrawer && drawerBackdrop) {
      mobileDrawer.classList.add('active');
      drawerBackdrop.classList.add('active');
      document.body.style.overflow = 'hidden';
    }
  }

  function closeDrawer() {
    if (mobileDrawer && drawerBackdrop) {
      mobileDrawer.classList.remove('active');
      drawerBackdrop.classList.remove('active');
      document.body.style.overflow = '';
    }
  }

  if (drawerOpenBtn) drawerOpenBtn.addEventListener('click', openDrawer);
  if (drawerCloseBtn) drawerCloseBtn.addEventListener('click', closeDrawer);
  if (drawerBackdrop) drawerBackdrop.addEventListener('click', closeDrawer);

  drawerLinks.forEach(link => {
    link.addEventListener('click', closeDrawer);
  });
}

/* ==========================================================================
   2. Hero Visual Switcher
   ========================================================================== */
function initHeroSwitcher() {
  const tabBtns = document.querySelectorAll('.hero-tab-btn');
  const heroImg = document.getElementById('heroMainImage');
  const badgeTitle = document.getElementById('badgeTopTitle');
  const badgeSub = document.getElementById('badgeTopSub');

  const getApartmentBanner = () => {
    if (currentAppLang === 'tr') return 'assets/images/banner-turkish.jpg';
    if (currentAppLang === 'en') return 'assets/images/banner-english.jpg';
    return 'assets/images/banner-apartment.png';
  };

  tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      tabBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const target = btn.dataset.target;
      let src = '';
      let bTitle = '';
      let bSub = '';

      const dict = (typeof translations !== 'undefined' && translations[currentAppLang]) ? translations[currentAppLang] : {};

      if (target === 'apartment') {
        src = getApartmentBanner();
        bTitle = dict.floating_top_title || 'تنظيف احترافي لشقتك';
        bSub = dict.floating_top_sub || 'خدمة راقية وسريعة للشقق والمنازل';
      } else if (target === 'office') {
        src = 'assets/images/banner-office.png';
        if (currentAppLang === 'tr') {
          bTitle = 'Ofisler İçin Günlük Hijyen';
          bSub = 'Şık ve Sağlıklı Çalışma Alanı';
        } else if (currentAppLang === 'en') {
          bTitle = 'Daily Office Cleaning';
          bSub = 'Elegant & Healthy Workplace';
        } else {
          bTitle = 'نظافة يومية للمكاتب';
          bSub = 'بيئة عمل أنيقة وصحية';
        }
      } else if (target === 'home') {
        src = 'assets/images/banner-home.png';
        if (currentAppLang === 'tr') {
          bTitle = 'Kapsamlı ve Güvenilir Temizlik';
          bSub = 'Üniformalı ve Eğitimli Kadro';
        } else if (currentAppLang === 'en') {
          bTitle = 'Comprehensive & Trusted Clean';
          bSub = 'Uniformed & Trained Staff';
        } else {
          bTitle = 'نظافة راقية وموثوقة';
          bSub = 'فريق مدرّب بزي موحد';
        }
      }

      if (heroImg && src) {
        heroImg.style.opacity = '0.3';
        heroImg.style.transform = 'scale(0.98)';
        setTimeout(() => {
          heroImg.src = src;
          heroImg.style.opacity = '1';
          heroImg.style.transform = 'scale(1)';
        }, 120);

        if (badgeTitle && bTitle) badgeTitle.textContent = bTitle;
        if (badgeSub && bSub) badgeSub.textContent = bSub;
      }
    });
  });
}

/* ==========================================================================
   3. Specifications & Custom Quote Calculator (NO FIXED PRICES)
   ========================================================================== */
function initCalculator() {
  const propertyBtns = document.querySelectorAll('.calc-prop-btn');
  const bathBtns = document.querySelectorAll('.calc-bath-btn');
  const balconyBtns = document.querySelectorAll('.calc-balcony-btn');
  const cleanTypeBtns = document.querySelectorAll('.calc-type-btn');
  const addonCheckboxes = document.querySelectorAll('.calc-addon-input');
  const districtSelect = document.getElementById('calcDistrict');
  const preferredDate = document.getElementById('calcDate');
  const notesInput = document.getElementById('calcNotes');
  
  // Summary Elements
  const sumProperty = document.getElementById('sumProperty');
  const sumSubDetails = document.getElementById('sumSubDetails');
  const sumType = document.getElementById('sumType');
  const sumDistrict = document.getElementById('sumDistrict');
  const sumAddons = document.getElementById('sumAddons');
  const whatsappBtn = document.getElementById('calcBookWhatsApp');

  if (preferredDate) {
    preferredDate.min = new Date().toISOString().split('T')[0];
  }

  // Key-based state (independent of language strings)
  let calcState = {
    propertyKey: 'prop_2plus1',
    bathKey: 'bath_2',
    balconyKey: 'balcony_1',
    cleanTypeKey: 'type_deep',
    addonKeys: [],
    districtKey: 'dist_basaksehir',
    date: '',
    notes: ''
  };

  // Property Selection
  propertyBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      propertyBtns.forEach(b => b.classList.remove('selected'));
      btn.classList.add('selected');
      calcState.propertyKey = btn.dataset.key;
      updateSummary();
    });
  });

  // Bathrooms Selection
  bathBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      bathBtns.forEach(b => b.classList.remove('selected'));
      btn.classList.add('selected');
      calcState.bathKey = btn.dataset.key;
      updateSummary();
    });
  });

  // Balconies Selection
  balconyBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      balconyBtns.forEach(b => b.classList.remove('selected'));
      btn.classList.add('selected');
      calcState.balconyKey = btn.dataset.key;
      updateSummary();
    });
  });

  // Cleaning Type Selection
  cleanTypeBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      cleanTypeBtns.forEach(b => b.classList.remove('selected'));
      btn.classList.add('selected');
      calcState.cleanTypeKey = btn.dataset.key;
      updateSummary();
    });
  });

  // Addons Selection
  addonCheckboxes.forEach(cb => {
    cb.addEventListener('change', () => {
      const parentLabel = cb.closest('.addon-checkbox-label');
      if (cb.checked) {
        parentLabel.classList.add('checked');
      } else {
        parentLabel.classList.remove('checked');
      }
      recalculateAddons();
      updateSummary();
    });
  });

  function recalculateAddons() {
    calcState.addonKeys = [];
    addonCheckboxes.forEach(cb => {
      if (cb.checked && cb.dataset.key) {
        calcState.addonKeys.push(cb.dataset.key);
      }
    });
  }

  // District Selection
  if (districtSelect) {
    districtSelect.addEventListener('change', (e) => {
      calcState.districtKey = e.target.value;
      updateSummary();
    });
  }

  // Date Selection
  if (preferredDate) {
    preferredDate.addEventListener('change', (e) => {
      calcState.date = e.target.value;
      updateSummary();
    });
  }

  // Notes Selection
  if (notesInput) {
    notesInput.addEventListener('input', (e) => {
      calcState.notes = e.target.value;
      updateSummary();
    });
  }

  function updateSummary() {
    const dict = (typeof translations !== 'undefined' && translations[currentAppLang])
      ? translations[currentAppLang]
      : (typeof translations !== 'undefined' ? translations.ar : {});

    const propName = dict[calcState.propertyKey] || calcState.propertyKey;
    const bathName = dict[calcState.bathKey] || calcState.bathKey;
    const balconyName = dict[calcState.balconyKey] || calcState.balconyKey;
    const typeName = dict[calcState.cleanTypeKey] || calcState.cleanTypeKey;
    const districtName = dict[calcState.districtKey] || calcState.districtKey;

    if (sumProperty) sumProperty.textContent = propName;
    if (sumSubDetails) sumSubDetails.textContent = `${bathName} • ${balconyName}`;
    if (sumType) sumType.textContent = typeName;
    if (sumDistrict) sumDistrict.textContent = districtName;

    const sep = (currentAppLang === 'ar') ? '، ' : ', ';
    if (sumAddons) {
      if (calcState.addonKeys.length > 0) {
        const addonNames = calcState.addonKeys.map(k => dict[k] || k);
        sumAddons.textContent = addonNames.join(sep);
      } else {
        sumAddons.textContent = dict.calc_sum_no_addons || 'لا توجد إضافات';
      }
    }

    // Format WhatsApp message in current language with zero Arabic in TR/EN!
    let msg = (dict.wa_intro || 'السلام عليكم ورحمة الله،\\n');
    msg += (dict.wa_prop || '📍 نوع العقار: ') + propName + '\\n';
    msg += (dict.wa_details || '🛁 تفاصيل المكان: ') + bathName + ' | ' + balconyName + '\\n';
    msg += (dict.wa_level || '✨ مستوى الخدمة: ') + typeName + '\\n';
    msg += (dict.wa_district || '🏙️ المنطقة في اسطنبول: ') + districtName + '\\n';
    if (calcState.addonKeys.length > 0) {
      const addonNames = calcState.addonKeys.map(k => dict[k] || k);
      msg += (dict.wa_addons || '➕ خدمات إضافية: ') + addonNames.join(sep) + '\\n';
    }
    if (calcState.date) {
      msg += (dict.wa_date || '📅 التاريخ المفضل: ') + calcState.date + '\\n';
    }
    if (calcState.notes && calcState.notes.trim()) {
      msg += (dict.wa_notes || '💬 ملاحظات: ') + calcState.notes.trim() + '\\n';
    }
    msg += (dict.wa_closing || '\\nبانتظار ردكم، شكراً لكم.');

    const encodedMsg = encodeURIComponent(msg);
    if (whatsappBtn) {
      whatsappBtn.href = `https://wa.me/${OFFICIAL_PHONE}?text=${encodedMsg}`;
    }
  }

  window.updateCalcSummary = updateSummary;

  recalculateAddons();
  updateSummary();
}

/* ==========================================================================
   4. Before & After Comparison Slider
   ========================================================================== */
function initBeforeAfterSlider() {
  const container = document.querySelector('.ba-container');
  const slider = document.querySelector('.ba-range-slider');
  const beforeImg = document.querySelector('.ba-image.before-img');
  const handle = document.querySelector('.ba-handle');

  if (!container || !slider || !beforeImg || !handle) return;

  function updateSlider(val) {
    beforeImg.style.width = `${val}%`;
    handle.style.left = `${val}%`;
  }

  slider.addEventListener('input', (e) => {
    updateSlider(e.target.value);
  });

  slider.addEventListener('change', (e) => {
    updateSlider(e.target.value);
  });

  updateSlider(50);
}

/* ==========================================================================
   5. Istanbul Coverage Districts
   ========================================================================== */
function initCoverageDistricts() {
  const districtCards = document.querySelectorAll('.district-card');
  const districtSelect = document.getElementById('calcDistrict');

  districtCards.forEach(card => {
    card.addEventListener('click', () => {
      const key = card.dataset.key;
      if (districtSelect && key) {
        districtSelect.value = key;
        districtSelect.dispatchEvent(new Event('change'));
        
        const calcSection = document.getElementById('calculator');
        if (calcSection) {
          calcSection.scrollIntoView({ behavior: 'smooth' });
        }
      }
    });
  });
}

/* ==========================================================================
   6. FAQ Accordion
   ========================================================================== */
function initFaqAccordion() {
  const faqItems = document.querySelectorAll('.faq-item');

  faqItems.forEach(item => {
    const header = item.querySelector('.faq-header');
    header.addEventListener('click', () => {
      const isOpen = item.classList.contains('active');
      faqItems.forEach(i => i.classList.remove('active'));
      if (!isOpen) {
        item.classList.add('active');
      }
    });
  });
}

/* ==========================================================================
   7. WhatsApp Floating Widget & Quick Popup
   ========================================================================== */
function initWhatsAppWidget() {
  const floatBtn = document.getElementById('floatingWhatsApp');
  const chatModal = document.getElementById('quickChatModal');
  const closeBtn = document.getElementById('chatCloseBtn');

  if (floatBtn && chatModal) {
    floatBtn.addEventListener('click', () => {
      chatModal.classList.toggle('open');
    });

    if (closeBtn) {
      closeBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        chatModal.classList.remove('open');
      });
    }

    document.addEventListener('click', (e) => {
      if (!chatModal.contains(e.target) && !floatBtn.contains(e.target)) {
        chatModal.classList.remove('open');
      }
    });
  }
}

/* ==========================================================================
   8. Back to Top Button
   ========================================================================== */
function initBackToTop() {
  const backBtn = document.getElementById('backToTop');
  if (!backBtn) return;

  window.addEventListener('scroll', () => {
    if (window.scrollY > 400) {
      backBtn.classList.add('visible');
    } else {
      backBtn.classList.remove('visible');
    }
  });

  backBtn.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
}

/**
 * Pre-select service from card buttons and scroll
 */
window.selectServiceAndScroll = function(key) {
  const calcSection = document.getElementById('calculator');
  if (calcSection) {
    calcSection.scrollIntoView({ behavior: 'smooth' });
  }

  const propOption = document.querySelector(`.calc-prop-btn[data-key="${key}"]`);
  if (propOption) {
    propOption.click();
    return;
  }

  const typeOption = document.querySelector(`.calc-type-btn[data-key="${key}"]`);
  if (typeOption) {
    typeOption.click();
    return;
  }

  const addonOption = document.querySelector(`.calc-addon-input[data-key="${key}"]`);
  if (addonOption && !addonOption.checked) {
    addonOption.click();
  }
};

/* ==========================================================================
   9. Multi-Language Switcher (AR / TR / EN) - 100% Comprehensive Localization
   ========================================================================== */
function applyLanguage(lang) {
  if (typeof translations === 'undefined' || !translations[lang]) return;
  currentAppLang = lang;
  const dict = translations[lang];

  // 1. Direction and HTML attributes
  document.documentElement.lang = lang;
  document.documentElement.dir = (lang === 'ar') ? 'rtl' : 'ltr';
  document.body.dir = (lang === 'ar') ? 'rtl' : 'ltr';

  // 2. Document Title & Meta Description
  if (dict.doc_title) {
    document.title = dict.doc_title;
  }
  const metaDesc = document.getElementById('metaDescription') || document.querySelector('meta[name="description"]');
  if (metaDesc && dict.doc_desc) {
    metaDesc.setAttribute('content', dict.doc_desc);
  }

  // 3. Update all [data-i18n] text nodes
  document.querySelectorAll('[data-i18n]').forEach(el => {
    const key = el.getAttribute('data-i18n');
    if (dict[key] !== undefined) {
      el.innerHTML = dict[key];
    }
  });

  // 4. Update [data-i18n-ph] input placeholders
  document.querySelectorAll('[data-i18n-ph]').forEach(el => {
    const key = el.getAttribute('data-i18n-ph');
    if (dict[key] !== undefined) {
      el.placeholder = dict[key];
    }
  });

  // 5. Update [data-i18n-title] tooltip titles
  document.querySelectorAll('[data-i18n-title]').forEach(el => {
    const key = el.getAttribute('data-i18n-title');
    if (dict[key] !== undefined) {
      el.title = dict[key];
    }
  });

  // 6. Update [data-i18n-aria] accessibility labels
  document.querySelectorAll('[data-i18n-aria]').forEach(el => {
    const key = el.getAttribute('data-i18n-aria');
    if (dict[key] !== undefined) {
      el.setAttribute('aria-label', dict[key]);
    }
  });

  // 7. Update [data-i18n-alt] image alt text
  document.querySelectorAll('[data-i18n-alt]').forEach(el => {
    const key = el.getAttribute('data-i18n-alt');
    if (dict[key] !== undefined) {
      el.setAttribute('alt', dict[key]);
    }
  });

  // 8. Update [data-i18n-label] optgroup labels
  document.querySelectorAll('[data-i18n-label]').forEach(el => {
    const key = el.getAttribute('data-i18n-label');
    if (dict[key] !== undefined) {
      el.setAttribute('label', dict[key]);
    }
  });

  // 9. Update [data-i18n-content] meta content tags
  document.querySelectorAll('[data-i18n-content]').forEach(el => {
    const key = el.getAttribute('data-i18n-content');
    if (dict[key] !== undefined) {
      el.setAttribute('content', dict[key]);
    }
  });

  // 9. Update language switcher button states
  document.querySelectorAll('.lang-btn, .header-lang-btn').forEach(btn => {
    if (btn.dataset.lang === lang) {
      btn.classList.add('active');
    } else {
      btn.classList.remove('active');
    }
  });

  // 10. Update Hero Main Image Banner
  const heroMainImg = document.getElementById('heroMainImage');
  if (heroMainImg) {
    const activeTab = document.querySelector('.hero-tab-btn.active');
    const target = activeTab ? activeTab.dataset.target : 'apartment';

    let targetSrc = 'assets/images/banner-apartment.png';
    if (target === 'apartment') {
      if (lang === 'tr') targetSrc = 'assets/images/banner-turkish.jpg';
      else if (lang === 'en') targetSrc = 'assets/images/banner-english.jpg';
      else targetSrc = 'assets/images/banner-apartment.png';
    } else if (target === 'office') {
      targetSrc = 'assets/images/banner-office.png';
    } else if (target === 'home') {
      targetSrc = 'assets/images/banner-home.png';
    }

    heroMainImg.style.opacity = '0.3';
    heroMainImg.style.transform = 'scale(0.98)';
    setTimeout(() => {
      heroMainImg.src = targetSrc;
      heroMainImg.style.opacity = '1';
      heroMainImg.style.transform = 'scale(1)';
    }, 120);
  }

  // 11. Update floating badges
  const badgeTopTitle = document.getElementById('badgeTopTitle');
  const badgeTopSub = document.getElementById('badgeTopSub');
  if (badgeTopTitle && dict.floating_top_title) badgeTopTitle.textContent = dict.floating_top_title;
  if (badgeTopSub && dict.floating_top_sub) badgeTopSub.textContent = dict.floating_top_sub;

  // 12. Update Top Bar Text
  const topBarLabel = document.getElementById('topBarLabel');
  const topBarText = document.getElementById('topBarText');
  if (topBarLabel && dict.topbar_label) topBarLabel.textContent = dict.topbar_label;
  if (topBarText && dict.topbar_text) topBarText.textContent = dict.topbar_text;

  // 13. Update Header WhatsApp Button Text
  const headerBtn = document.getElementById('headerWhatsAppActionText');
  if (headerBtn && dict.header_whatsapp) headerBtn.textContent = dict.header_whatsapp;

  // 14. Update WhatsApp links with localized default text
  const heroWhatsAppBtn = document.getElementById('heroWhatsAppBtn');
  const defaultWhatsAppText = encodeURIComponent(
    lang === 'tr' ? 'Merhaba TEMiZO, İstanbul genelinde temizlik hizmeti hakkında bilgi ve randevu almak istiyorum.' :
    lang === 'en' ? 'Hello TEMiZO, I would like to inquire about cleaning services in Istanbul.' :
    'مرحباً تميزو، أود الاستفسار عن خدمات التنظيف الفورية في اسطنبول'
  );

  const directWhatsAppUrls = [
    heroWhatsAppBtn,
    document.querySelector('.drawer-actions a.btn-whatsapp'),
    document.querySelector('.cta-buttons a.btn-whatsapp'),
    document.querySelector('.chat-start-btn')
  ];

  directWhatsAppUrls.forEach(link => {
    if (link) link.href = `https://wa.me/${OFFICIAL_PHONE}?text=${defaultWhatsAppText}`;
  });

  // 15. Re-render calculator summary and dynamic quote message
  if (typeof window.updateCalcSummary === 'function') {
    window.updateCalcSummary();
  }
}

function initLanguageSwitcher() {
  const allLangBtns = document.querySelectorAll('.lang-btn, .header-lang-btn');

  allLangBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const lang = btn.dataset.lang;
      if (lang) {
        applyLanguage(lang);
      }
    });
  });

  // Read URL query param ?lang=tr or ?lang=en
  const urlParams = new URLSearchParams(window.location.search);
  const langParam = urlParams.get('lang');
  if (langParam && (langParam === 'tr' || langParam === 'en' || langParam === 'ar')) {
    applyLanguage(langParam);
  }
}

/* ==========================================================================
   10. 3D WebGL Soap Bubbles Scene (Three.js Engine - Inspired by byte-lab.tech)
   ========================================================================== */
function initThreeJsBubbleScene() {
  const container = document.getElementById('webgl-bubbles-container');
  if (!container || typeof THREE === 'undefined') return;

  // Scene & Camera setup
  const scene = new THREE.Scene();
  scene.fog = new THREE.FogExp2(0xffffff, 0.0032);

  const camera = new THREE.PerspectiveCamera(60, window.innerWidth / window.innerHeight, 0.1, 1000);
  camera.position.z = 32;

  const renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true, powerPreference: 'high-performance' });
  renderer.setSize(window.innerWidth, window.innerHeight);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
  container.appendChild(renderer.domElement);

  // 1. Procedural Realistic Iridescent Soap Bubble Texture
  const bubbleTexture = (() => {
    const size = 256;
    const canvas = document.createElement('canvas');
    canvas.width = size;
    canvas.height = size;
    const ctx = canvas.getContext('2d');
    const c = size / 2;
    const r = size * 0.44;

    ctx.clearRect(0, 0, size, size);

    // Subtle iridescent body refraction
    const bodyGrad = ctx.createRadialGradient(c - 18, c - 18, r * 0.1, c, c, r);
    bodyGrad.addColorStop(0, 'rgba(255, 255, 255, 0.06)');
    bodyGrad.addColorStop(0.48, 'rgba(0, 240, 255, 0.08)');
    bodyGrad.addColorStop(0.72, 'rgba(195, 115, 255, 0.12)');
    bodyGrad.addColorStop(0.88, 'rgba(0, 191, 165, 0.24)');
    bodyGrad.addColorStop(1, 'rgba(0, 240, 255, 0.42)');
    ctx.fillStyle = bodyGrad;
    ctx.beginPath();
    ctx.arc(c, c, r, 0, Math.PI * 2);
    ctx.fill();

    // Luminous specular rim
    ctx.lineWidth = 3.8;
    const rimGrad = ctx.createLinearGradient(c - r, c - r, c + r, c + r);
    rimGrad.addColorStop(0, 'rgba(255, 255, 255, 0.96)');
    rimGrad.addColorStop(0.28, 'rgba(0, 240, 255, 0.88)');
    rimGrad.addColorStop(0.58, 'rgba(215, 125, 255, 0.72)');
    rimGrad.addColorStop(0.82, 'rgba(0, 191, 165, 0.9)');
    rimGrad.addColorStop(1, 'rgba(255, 255, 255, 0.86)');
    ctx.strokeStyle = rimGrad;
    ctx.stroke();

    // Inner bright reflection circle
    ctx.lineWidth = 1.2;
    ctx.strokeStyle = 'rgba(255, 255, 255, 0.65)';
    ctx.beginPath();
    ctx.arc(c, c, r - 3, 0, Math.PI * 2);
    ctx.stroke();

    // Crescent specular highlight (top-left)
    ctx.save();
    ctx.beginPath();
    ctx.arc(c, c, r - 8, Math.PI * 1.05, Math.PI * 1.55);
    ctx.strokeStyle = 'rgba(255, 255, 255, 0.9)';
    ctx.lineWidth = 6.5;
    ctx.lineCap = 'round';
    ctx.stroke();
    ctx.restore();

    // Primary bright glint pinpoint
    const glint = ctx.createRadialGradient(c - r * 0.42, c - r * 0.42, 0, c - r * 0.42, c - r * 0.42, 14);
    glint.addColorStop(0, 'rgba(255, 255, 255, 1)');
    glint.addColorStop(0.45, 'rgba(255, 255, 255, 0.88)');
    glint.addColorStop(1, 'rgba(255, 255, 255, 0)');
    ctx.fillStyle = glint;
    ctx.beginPath();
    ctx.arc(c - r * 0.42, c - r * 0.42, 14, 0, Math.PI * 2);
    ctx.fill();

    // Secondary soft bounce glint (bottom-right)
    ctx.save();
    ctx.beginPath();
    ctx.arc(c, c, r - 9, Math.PI * 0.12, Math.PI * 0.42);
    ctx.strokeStyle = 'rgba(0, 240, 255, 0.5)';
    ctx.lineWidth = 3.2;
    ctx.lineCap = 'round';
    ctx.stroke();
    ctx.restore();

    return new THREE.CanvasTexture(canvas);
  })();

  // 2. Micro Sparkle/Glint Texture for ambient mist & pop bursts
  const sparkleTexture = (() => {
    const size = 64;
    const canvas = document.createElement('canvas');
    canvas.width = size;
    canvas.height = size;
    const ctx = canvas.getContext('2d');
    const c = size / 2;

    const grad = ctx.createRadialGradient(c, c, 0, c, c, c);
    grad.addColorStop(0, 'rgba(255, 255, 255, 1)');
    grad.addColorStop(0.25, 'rgba(0, 240, 255, 0.75)');
    grad.addColorStop(0.65, 'rgba(0, 191, 165, 0.28)');
    grad.addColorStop(1, 'rgba(0, 191, 165, 0)');
    ctx.fillStyle = grad;
    ctx.fillRect(0, 0, size, size);

    ctx.fillStyle = 'rgba(255, 255, 255, 0.95)';
    ctx.fillRect(c - 1, 6, 2, size - 12);
    ctx.fillRect(6, c - 1, size - 12, 2);

    return new THREE.CanvasTexture(canvas);
  })();

  // 3. Floating 3D Soap Bubbles (Main Foreground/Midground)
  const bubbleCount = 48;
  const bubbles = [];
  const bubbleMaterial = new THREE.SpriteMaterial({
    map: bubbleTexture,
    transparent: true,
    opacity: 0.88,
    depthWrite: false
  });

  for (let i = 0; i < bubbleCount; i++) {
    const sprite = new THREE.Sprite(bubbleMaterial.clone());
    const baseScale = 1.0 + Math.random() * 3.8;
    sprite.scale.set(baseScale, baseScale, 1);

    const bData = {
      baseX: (Math.random() - 0.5) * 65,
      y: (Math.random() - 0.5) * 65,
      z: (Math.random() - 0.5) * 26,
      scale: baseScale,
      riseSpeed: 0.022 + Math.random() * 0.052,
      wobbleSpeed: 0.7 + Math.random() * 1.5,
      wobbleAmp: 0.35 + Math.random() * 0.75,
      wobblePhase: Math.random() * Math.PI * 2,
      repelX: 0,
      repelY: 0,
      popped: false,
      popTime: 0
    };

    sprite.position.set(bData.baseX, bData.y, bData.z);
    sprite.userData = bData;
    scene.add(sprite);
    bubbles.push(sprite);
  }

  // 4. Ambient Sparkle Particles (Micro-Foam / Crystal Sheen)
  const mistCount = 260;
  const mistGeometry = new THREE.BufferGeometry();
  const mistPositions = new Float32Array(mistCount * 3);
  const mistColors = new Float32Array(mistCount * 3);
  const mistSpeeds = new Float32Array(mistCount);

  const colorPalette = [
    new THREE.Color('#00BFA5'),
    new THREE.Color('#02C39A'),
    new THREE.Color('#38BDF8'),
    new THREE.Color('#FFFFFF')
  ];

  for (let i = 0; i < mistCount; i++) {
    mistPositions[i * 3] = (Math.random() - 0.5) * 80;
    mistPositions[i * 3 + 1] = (Math.random() - 0.5) * 80;
    mistPositions[i * 3 + 2] = (Math.random() - 0.5) * 40;

    const col = colorPalette[Math.floor(Math.random() * colorPalette.length)];
    mistColors[i * 3] = col.r;
    mistColors[i * 3 + 1] = col.g;
    mistColors[i * 3 + 2] = col.b;

    mistSpeeds[i] = 0.015 + Math.random() * 0.03;
  }

  mistGeometry.setAttribute('position', new THREE.BufferAttribute(mistPositions, 3));
  mistGeometry.setAttribute('color', new THREE.BufferAttribute(mistColors, 3));

  const mistMaterial = new THREE.PointsMaterial({
    size: 0.65,
    map: sparkleTexture,
    vertexColors: true,
    transparent: true,
    opacity: 0.6,
    blending: THREE.AdditiveBlending,
    depthWrite: false
  });

  const mistPoints = new THREE.Points(mistGeometry, mistMaterial);
  scene.add(mistPoints);

  // 5. Pop Particles Burst System
  const maxBurstParticles = 96;
  const burstGeo = new THREE.BufferGeometry();
  const burstPos = new Float32Array(maxBurstParticles * 3);
  const burstVel = [];
  for (let i = 0; i < maxBurstParticles; i++) {
    burstPos[i * 3] = 9999;
    burstPos[i * 3 + 1] = 9999;
    burstPos[i * 3 + 2] = 9999;
    burstVel.push({ vx: 0, vy: 0, vz: 0, life: 0 });
  }
  burstGeo.setAttribute('position', new THREE.BufferAttribute(burstPos, 3));
  const burstMat = new THREE.PointsMaterial({
    size: 0.8,
    map: sparkleTexture,
    transparent: true,
    opacity: 0.92,
    blending: THREE.AdditiveBlending,
    depthWrite: false
  });
  const burstPoints = new THREE.Points(burstGeo, burstMat);
  scene.add(burstPoints);

  function triggerBubbleBurst(x, y, z) {
    let spawned = 0;
    const countToSpawn = 14;
    for (let i = 0; i < maxBurstParticles && spawned < countToSpawn; i++) {
      if (burstVel[i].life <= 0) {
        burstPos[i * 3] = x;
        burstPos[i * 3 + 1] = y;
        burstPos[i * 3 + 2] = z;
        const angle = Math.random() * Math.PI * 2;
        const speed = 0.12 + Math.random() * 0.22;
        burstVel[i].vx = Math.cos(angle) * speed;
        burstVel[i].vy = Math.sin(angle) * speed + 0.05;
        burstVel[i].vz = (Math.random() - 0.5) * speed;
        burstVel[i].life = 1.0;
        spawned++;
      }
    }
    burstGeo.attributes.position.needsUpdate = true;
  }

  // 6. Interaction & Parallax Handlers
  let targetCamX = 0;
  let targetCamY = 0;
  let worldMouse = new THREE.Vector3(0, 0, 0);

  function onMouseMove(e) {
    const normX = (e.clientX / window.innerWidth) * 2 - 1;
    const normY = -(e.clientY / window.innerHeight) * 2 + 1;

    targetCamX = normX * 3.8;
    targetCamY = normY * 2.6;

    worldMouse.set(normX * 24, normY * 16, 0);
  }

  let scrollY = window.scrollY;
  function onScroll() {
    scrollY = window.scrollY;
  }

  function onSceneClick(e) {
    const normX = (e.clientX / window.innerWidth) * 2 - 1;
    const normY = -(e.clientY / window.innerHeight) * 2 + 1;
    const clickWorld = new THREE.Vector3(normX * 24, normY * 16, 0);

    let poppedAny = false;
    bubbles.forEach(b => {
      if (b.userData.popped) return;
      const d = b.position.distanceTo(clickWorld);
      if (d < b.userData.scale * 1.5 + 2.5) {
        b.userData.popped = true;
        b.userData.popTime = performance.now();
        triggerBubbleBurst(b.position.x, b.position.y, b.position.z);
        b.scale.set(0.001, 0.001, 1);
        poppedAny = true;
      }
    });

    if (!poppedAny) {
      triggerBubbleBurst(clickWorld.x, clickWorld.y, 0);
    }
  }

  window.addEventListener('mousemove', onMouseMove, { passive: true });
  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('click', onSceneClick, { passive: true });

  function onWindowResize() {
    const w = window.innerWidth;
    const h = window.innerHeight;
    camera.aspect = w / h;
    camera.updateProjectionMatrix();
    renderer.setSize(w, h);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
  }
  window.addEventListener('resize', onWindowResize, { passive: true });

  let clock = new THREE.Clock();

  function animate() {
    requestAnimationFrame(animate);
    const elapsedTime = clock.getElapsedTime();

    const maxScroll = Math.max(1, document.documentElement.scrollHeight - window.innerHeight);
    const scrollFactor = scrollY / maxScroll;

    camera.position.x += (targetCamX - camera.position.x) * 0.045;
    camera.position.y += (targetCamY - scrollFactor * 14 - camera.position.y) * 0.045;
    camera.position.z = 32 + Math.sin(elapsedTime * 0.4) * 0.8;
    camera.lookAt(0, -scrollFactor * 8, 0);

    for (let i = 0; i < bubbleCount; i++) {
      const b = bubbles[i];
      const data = b.userData;

      if (data.popped) {
        if (performance.now() - data.popTime > 1800) {
          data.popped = false;
          data.y = -35;
          data.baseX = (Math.random() - 0.5) * 65;
          b.position.set(data.baseX, data.y, data.z);
          b.scale.set(data.scale, data.scale, 1);
        }
        continue;
      }

      data.y += data.riseSpeed;
      const sway = Math.sin(elapsedTime * data.wobbleSpeed + data.wobblePhase) * data.wobbleAmp;

      const distToMouse = b.position.distanceTo(worldMouse);
      if (distToMouse < 9.0) {
        const force = (9.0 - distToMouse) / 9.0;
        const dirX = b.position.x - worldMouse.x;
        const dirY = b.position.y - worldMouse.y;
        data.repelX += dirX * force * 0.06;
        data.repelY += dirY * force * 0.06;
      }
      data.repelX *= 0.92;
      data.repelY *= 0.92;

      b.position.x = data.baseX + sway + data.repelX;
      b.position.y = data.y + data.repelY;

      const breathe = 1.0 + Math.sin(elapsedTime * 2.0 + data.wobblePhase) * 0.04;
      b.scale.set(data.scale * breathe, data.scale * breathe, 1);

      if (data.y > 36) {
        data.y = -36;
        data.baseX = (Math.random() - 0.5) * 65;
        data.scale = 1.0 + Math.random() * 3.8;
      }
    }

    const positions = mistGeometry.attributes.position.array;
    for (let i = 0; i < mistCount; i++) {
      positions[i * 3 + 1] += mistSpeeds[i];
      if (positions[i * 3 + 1] > 40) {
        positions[i * 3 + 1] = -40;
        positions[i * 3] = (Math.random() - 0.5) * 80;
      }
    }
    mistGeometry.attributes.position.needsUpdate = true;

    let activeBursts = false;
    for (let i = 0; i < maxBurstParticles; i++) {
      if (burstVel[i].life > 0) {
        burstPos[i * 3] += burstVel[i].vx;
        burstPos[i * 3 + 1] += burstVel[i].vy;
        burstPos[i * 3 + 2] += burstVel[i].vz;
        burstVel[i].vy -= 0.004;
        burstVel[i].life -= 0.028;
        if (burstVel[i].life <= 0) {
          burstPos[i * 3] = 9999;
          burstPos[i * 3 + 1] = 9999;
        }
        activeBursts = true;
      }
    }
    if (activeBursts) {
      burstGeo.attributes.position.needsUpdate = true;
    }

    renderer.render(scene, camera);
  }

  animate();
}

/* ==========================================================================
   11. Dual-Ring Soap Bubble Interactive Cursor (byte-lab.tech style)
   ========================================================================== */
function initBubbleCursor() {
  const dot = document.getElementById('cursorDot');
  const ring = document.getElementById('cursorRing');
  if (!dot || !ring) return;

  if (window.matchMedia('(hover: none)').matches || window.innerWidth <= 991) {
    return;
  }

  let mouseX = window.innerWidth / 2;
  let mouseY = window.innerHeight / 2;
  let ringX = mouseX;
  let ringY = mouseY;

  window.addEventListener('mousemove', (e) => {
    mouseX = e.clientX;
    mouseY = e.clientY;
    dot.style.left = `${mouseX}px`;
    dot.style.top = `${mouseY}px`;
  }, { passive: true });

  const hoverElements = document.querySelectorAll(
    'a, button, input, select, textarea, .service-card, .feature-item, .stat-box, .district-card, .faq-header, .ba-range-slider, .hero-tab-btn'
  );

  hoverElements.forEach(el => {
    el.addEventListener('mouseenter', () => {
      document.body.classList.add('cursor-hover');
    });
    el.addEventListener('mouseleave', () => {
      document.body.classList.remove('cursor-hover');
    });
  });

  window.addEventListener('mousedown', () => {
    document.body.classList.add('cursor-pressed');
  });

  window.addEventListener('mouseup', () => {
    document.body.classList.remove('cursor-pressed');
  });

  function updateCursor() {
    ringX += (mouseX - ringX) * 0.16;
    ringY += (mouseY - ringY) * 0.16;
    ring.style.left = `${ringX}px`;
    ring.style.top = `${ringY}px`;
    requestAnimationFrame(updateCursor);
  }
  updateCursor();
}

/* ==========================================================================
   12. 3D Tilt Cards with Dynamic Specular Glare (byte-lab.tech style)
   ========================================================================== */
function init3DCardTilt() {
  if (window.matchMedia('(hover: none)').matches || window.innerWidth <= 991) {
    return;
  }

  const tiltCards = document.querySelectorAll(
    '.service-card, .feature-item, .stat-box, .district-card, .testimonial-card'
  );

  tiltCards.forEach(card => {
    card.classList.add('tilt-card');

    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;

      const centerX = rect.width / 2;
      const centerY = rect.height / 2;

      const rotX = ((y - centerY) / centerY) * -6.5;
      const rotY = ((x - centerX) / centerX) * 6.5;

      const xPercent = (x / rect.width) * 100;
      const yPercent = (y / rect.height) * 100;

      card.style.setProperty('--mouse-x', `${xPercent}%`);
      card.style.setProperty('--mouse-y', `${yPercent}%`);
      card.style.transform = `perspective(1000px) rotateX(${rotX.toFixed(2)}deg) rotateY(${rotY.toFixed(2)}deg) translateY(-5px) scale3d(1.02, 1.02, 1.02)`;
    });

    card.addEventListener('mouseleave', () => {
      card.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) translateY(0) scale3d(1, 1, 1)';
    });
  });
}
"""

out_path = os.path.join(os.path.dirname(__file__), "main.js")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(js_code)

print(f"Successfully generated {out_path}")
