"""Trace supplied binary artwork; preserve lettering, remove isolated scan specks.
Run with Python + Pillow + numpy. SVG shapes are traced polygons, not embedded bitmaps.
PNG/PDF exports are generated from SVG using scripts/export-logo-set.cjs.
"""
from pathlib import Path
import numpy as np
from PIL import Image
import json
ROOT=Path(__file__).resolve().parents[1]
a=np.array(Image.open(ROOT/'public/images/brand/sb-mark.png').convert('L'))>128

def paths(crop):
 x,y,r,b=crop; m=a[y:b,x:r]; h,w=m.shape; edges={}
 for yy,xx in zip(*np.where(m)):
  for on,p,q in [(yy==0 or not m[yy-1,xx],(xx,yy),(xx+1,yy)),(xx==w-1 or not m[yy,xx+1],(xx+1,yy),(xx+1,yy+1)),(yy==h-1 or not m[yy+1,xx],(xx+1,yy+1),(xx,yy+1)),(xx==0 or not m[yy,xx-1],(xx,yy+1),(xx,yy))]:
   if on: edges.setdefault(p,[]).append(q)
 loops=[]
 while edges:
  start=next(iter(edges)); p=start; pts=[p]
  while True:
   q=edges[p].pop()
   if not edges[p]: del edges[p]
   p=q
   if p==start: break
   pts.append(p)
  if len(pts)<20: continue
  # Drop collinear points; retain the exact supplied silhouette.
  pts=[p for i,p in enumerate(pts) if (p[0]-pts[i-1][0],p[1]-pts[i-1][1]) != (pts[(i+1)%len(pts)][0]-p[0],pts[(i+1)%len(pts)][1]-p[1])]
  loops.append('M'+' L'.join(f'{x},{y}' for x,y in pts)+'Z')
 return '<path fill-rule="evenodd" d="'+''.join(loops)+'"/>'
mark=paths((205,218,975,559)); mic=paths((417,58,797,179)); primary=paths((205,55,975,790))
def group(shape,x,y,s=1,flip=False):
 return f'<g transform="translate({x} {y}) scale({-s if flip else s} {s})">{shape}</g>'
# The lettering and microphones share one centerline in the requested portrait canvas.
side=group(mark,245,360,.66)+group(mic,32,445.3,.45)+group(mic,968,445.3,.45,True)
compact=group(mark,90,329,1.065)
layouts={
 'sb-primary':(1000,1000,group(primary,190,205,.80)),
 'sb-portrait':(1000,1250,side),
 'sb-compact':(1000,1000,compact),
}
# Move portrait artwork to the true vertical center; no act name in this asset.
layouts['sb-portrait']=(1000,1250,'<g transform="translate(0 152.5)">'+side+'</g>')
for act,name in [('full-band','SARAH &amp; THE BUDS'),('acoustic-duo','SARAH &amp; BUD')]:
 for arrangement in ['horizontal','stacked']:
  if arrangement=='horizontal':
   w,h=1600,600; art='<g transform="translate(0 -150) scale(.95)">'+side+'</g>'+f'<text x="1010" y="315" font-size="40">{name}</text>'
  else:
   w,h=1000,1250; art=group(primary,269,160,.60)+f'<text x="500" y="810" text-anchor="middle" font-size="47">{name}</text>'
  layouts[f'{act}-{arrangement}']=(w,h,art)
out=ROOT/'public/downloads/logos'; inventory=[]
for key,(w,h,art) in layouts.items():
 for label,color in [('black','#111111'),('warm-white','#F5F2EA')]:
  filename=f'{key}-{label}.svg'
  svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><title>{key.replace("-"," ")} — {label}</title><g fill="{color}" font-family="Avenir Next,Montserrat,Arial,sans-serif" letter-spacing="2">{art}</g></svg>'
  (out/filename).write_text(svg)
  inventory.append({'name':key.replace('-',' ').title()+' · '+label.replace('-',' '),'file':filename[:-4],'width':w,'height':h,'color':label})
# Background-bearing social avatars and compact favicon.
for label,bg,fg in [('dark','#111111','#F5F2EA'),('light','#F5F2EA','#111111')]:
 svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1080" viewBox="0 0 1000 1000"><rect width="1000" height="1000" fill="{bg}"/><g fill="{fg}">{compact}</g></svg>'
 (out/f'sb-social-{label}.svg').write_text(svg)
 inventory.append({'name':'Social avatar · '+label,'file':'sb-social-'+label,'width':1080,'height':1080,'color':label})
favicon=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1000"><rect width="1000" height="1000" rx="140" fill="#111111"/><g fill="#F5F2EA">{compact}</g></svg>'
(ROOT/'public/favicon.svg').write_text(favicon)
(ROOT/'src/data/logos.json').write_text(json.dumps(inventory,indent=2)+'\n')
print('Created',len(inventory),'logo arrangements/color variants')
