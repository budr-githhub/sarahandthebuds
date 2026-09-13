"""Package checked-in assets; run after logo exports and approved photo/copy changes."""
from pathlib import Path
import json,zipfile
r=Path(__file__).resolve().parents[1];d=r/'public/downloads'
copy=json.loads((r/'src/data/press.json').read_text())
text='SARAH & THE BUDS — PRESS MATERIALS\n\nFull band\n'+copy['band']+'\n\nAcoustic duo\n'+copy['duo']+'\n\nBooking: booksarahandbud@gmail.com | (859) 519-0840\nYouTube: https://www.youtube.com/@sarahandbud\n'
(d/'promotional-copy.txt').write_text(text)
usage='''SARAH & THE BUDS — PRESS KIT

COMING SOON
- Expanded band and duo promotional descriptions
- Photo credits and promotional usage guidance
- Featured performance videos

For specific promotional needs, contact booksarahandbud@gmail.com.

Use the correct act name: Sarah & the Buds (full band); Sarah & Bud (acoustic duo).
Keep logo proportions, black/warm-white colors and clear space. Do not retype S&B.
The portrait S&B asset intentionally has inward-facing microphones and no act name.
Place the appropriate act name elsewhere in promotional material using that mark.

SVG silhouettes were traced from the supplied binary raster; these are not original designer masters.
They retain source edge irregularities. PDF preserves scalable paths. PNG is raster.
No font files are distributed; labels use Avenir Next/Arial as available at export.
Photos retain the real performers. AI-edited homepage hero is excluded.
Confirm photo credit and usage with booksarahandbud@gmail.com before external distribution.
'''
(d/'read-me.txt').write_text(usage)
extras=['favicon.svg','favicon.ico','favicon-16.png','favicon-32.png','apple-touch-icon.png']
with zipfile.ZipFile(d/'sarah-and-the-buds-logo-set.zip','w',zipfile.ZIP_DEFLATED) as z:
 for f in sorted((d/'logos').iterdir()):z.write(f,'logos/'+f.name)
 for f in extras:z.write(r/'public'/f,'icons/'+f)
 z.write(d/'read-me.txt','read-me.txt')
photos=json.loads((r/'src/data/press-photos.json').read_text())
with zipfile.ZipFile(d/'sarah-and-the-buds-press-kit.zip','w',zipfile.ZIP_DEFLATED) as z:
 for p in photos:z.write(d/'photos'/p['file'],p['act']+'/'+p['file'])
 for f in sorted((d/'logos').iterdir()):z.write(f,'logos/'+f.name)
 for f in extras:z.write(r/'public'/f,'icons/'+f)
 for f in ['read-me.txt','promotional-copy.txt']:z.write(d/f,f)
print('Created logo and press kit archives')
