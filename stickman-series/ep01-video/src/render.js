// usage: node render.js scene.html outDir fps [t1,t2,...]
const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path');
(async () => {
  const [html, out, fpsS, list] = process.argv.slice(2); const fps = +fpsS;
  fs.mkdirSync(out, { recursive: true });
  const b = await chromium.launch(); const pg = await b.newPage({ viewport: { width: 1920, height: 1080 } });
  pg.on('pageerror', e => console.error('PAGEERR', e.message));
  await pg.goto('file://' + path.resolve(html)); await pg.waitForTimeout(300);
  const times = list ? list.split(',').map(Number) : [...Array(Math.ceil(55.56 * fps)).keys()].map(i => i / fps);
  let i = 0;
  for (const t of times) {
    await pg.evaluate(t => window.render(t), t);
    await pg.screenshot({ path: path.join(out, `f${String(i).padStart(5, '0')}.jpg`), type: 'jpeg', quality: 92 });
    i++;
  }
  await b.close(); console.log('frames', i);
})();
