const { chromium } = require('playwright'); const fs=require('fs'), path=require('path');
(async()=>{ const dir=process.argv[2]; const b=await chromium.launch(); const pg=await b.newPage({viewport:{width:1024,height:1024}});
for (const f of fs.readdirSync(dir).filter(f=>f.endsWith('.svg'))){ const svg=fs.readFileSync(path.join(dir,f),'utf8');
 await pg.setContent(`<html><body style="margin:0;background:transparent">${svg}</body></html>`);
 await pg.locator('svg').screenshot({path:path.join(dir,f.replace('.svg','.png')),omitBackground:true}); }
await b.close();})();
