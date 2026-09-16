const fs = require('fs');
const translations = require('./js/translations.js');

console.log('AR keys:', Object.keys(translations.ar).length);
console.log('TR keys:', Object.keys(translations.tr).length);
console.log('EN keys:', Object.keys(translations.en).length);

const html = fs.readFileSync('./index.html', 'utf8');

const regex = /data-i18n(?:-[a-z]+)?="([^"]+)"/g;
const keysInHtml = new Set();
let m;
while ((m = regex.exec(html)) !== null) {
  keysInHtml.add(m[1]);
}
console.log('Keys in HTML:', keysInHtml.size);

const missingInAr = [...keysInHtml].filter(k => translations.ar[k] === undefined);
const missingInTr = [...keysInHtml].filter(k => translations.tr[k] === undefined);
const missingInEn = [...keysInHtml].filter(k => translations.en[k] === undefined);

console.log('Missing in AR:', missingInAr);
console.log('Missing in TR:', missingInTr);
console.log('Missing in EN:', missingInEn);

const arRegex = /[\u0600-\u06FF]/;
const trArabic = Object.entries(translations.tr).filter(([k, v]) => arRegex.test(v));
const enArabic = Object.entries(translations.en).filter(([k, v]) => arRegex.test(v));

console.log('Arabic in TR count:', trArabic.length);
if (trArabic.length > 0) console.log('TR keys with Arabic:', trArabic.map(x => x[0]));
console.log('Arabic in EN count:', enArabic.length);
if (enArabic.length > 0) console.log('EN keys with Arabic:', enArabic.map(x => x[0]));
