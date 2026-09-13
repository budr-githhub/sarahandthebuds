// Export traced SVG masters using a local Chromium. Pass PLAYWRIGHT_MODULE if needed.
const {chromium}=require(process.env.PLAYWRIGHT_MODULE || 'playwright');
const fs=require('fs'),path=require('path');
(async()=>{
 const root=path.resolve(__dirname,'..'), folder=path.join(root,'public/downloads/logos');
 const browser=await chromium.launch({channel:'chrome',headless:true});
 const page=await browser.newPage();
 for(const f of fs.readdirSync(folder).filter(f=>f.endsWith('.svg'))){
  const svg=fs.readFileSync(path.join(folder,f),'utf8');
  const width=Number(svg.match(/width="(\d+)"/)[1]),height=Number(svg.match(/height="(\d+)"/)[1]);
  await page.setViewportSize({width,height});
  await page.setContent(`<html><head><style>html,body{margin:0;background:transparent}svg{display:block}@page{margin:0}</style></head><body>${svg}</body></html>`);
  await page.screenshot({path:path.join(folder,f.replace('.svg','.png')),omitBackground:true});
  await page.pdf({path:path.join(folder,f.replace('.svg','.pdf')),width:width+'px',height:height+'px',printBackground:true,pageRanges:'1'});
 }
 await browser.close();
})();
