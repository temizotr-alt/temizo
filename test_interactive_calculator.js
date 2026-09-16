// Test interactive behavior in Node simulation or Chrome
const fs = require('fs');
const translations = require('./js/translations.js');

function testWhatsAppMessage(lang, state) {
  const dict = translations[lang];
  const propName = dict[state.propertyKey] || state.propertyKey;
  const bathName = dict[state.bathKey] || state.bathKey;
  const balconyName = dict[state.balconyKey] || state.balconyKey;
  const typeName = dict[state.cleanTypeKey] || state.cleanTypeKey;
  const districtName = dict[state.districtKey] || state.districtKey;
  const sep = (lang === 'ar') ? '، ' : ', ';

  let msg = (dict.wa_intro || '');
  msg += (dict.wa_prop || '') + propName + '\n';
  msg += (dict.wa_details || '') + bathName + ' | ' + balconyName + '\n';
  msg += (dict.wa_level || '') + typeName + '\n';
  msg += (dict.wa_district || '') + districtName + '\n';
  if (state.addonKeys && state.addonKeys.length > 0) {
    const addonNames = state.addonKeys.map(k => dict[k] || k);
    msg += (dict.wa_addons || '') + addonNames.join(sep) + '\n';
  }
  if (state.date) {
    msg += (dict.wa_date || '') + state.date + '\n';
  }
  if (state.notes && state.notes.trim()) {
    msg += (dict.wa_notes || '') + state.notes.trim() + '\n';
  }
  msg += (dict.wa_closing || '');

  return msg;
}

const testState = {
  propertyKey: 'prop_2plus1',
  bathKey: 'bath_2',
  balconyKey: 'balcony_1',
  cleanTypeKey: 'type_deep',
  addonKeys: ['addon_sofa', 'addon_express'],
  districtKey: 'dist_basaksehir',
  date: '2026-09-20',
  notes: 'Express morning service'
};

const arRegex = /[\u0600-\u06FF]/;

const msgTR = testWhatsAppMessage('tr', testState);
console.log('--- TR WhatsApp Message ---');
console.log(msgTR);
console.log('Has Arabic in TR message:', arRegex.test(msgTR));

const msgEN = testWhatsAppMessage('en', testState);
console.log('\n--- EN WhatsApp Message ---');
console.log(msgEN);
console.log('Has Arabic in EN message:', arRegex.test(msgEN));

const msgAR = testWhatsAppMessage('ar', testState);
console.log('\n--- AR WhatsApp Message ---');
console.log(msgAR);

if (arRegex.test(msgTR) || arRegex.test(msgEN)) {
  console.error('FAIL: Arabic characters found in TR or EN WhatsApp message!');
  process.exit(1);
} else {
  console.log('\nSUCCESS: TR and EN WhatsApp messages are 100% free of Arabic characters!');
}
