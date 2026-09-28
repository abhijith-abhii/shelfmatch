from PIL import Image,ImageDraw
from pathlib import Path
import json,random
ROOT=Path(__file__).parent;(ROOT/'static/swatches').mkdir(parents=True,exist_ok=True);rows=[]
colors={'blue':(49,105,184),'red':(190,60,62),'green':(42,135,99),'gold':(201,155,58)};i=0
for category in ['fabric','tile']:
 for color,rgb in colors.items():
  for pattern in ['striped','speckled']:
   i+=1;im=Image.new('RGB',(240,240),rgb);draw=ImageDraw.Draw(im);rng=random.Random(i)
   if pattern=='striped':
    for x in range(0,240,24):draw.rectangle((x,0,x+7,240),fill=tuple(min(255,v+45) for v in rgb))
   else:
    for _ in range(1100):
     x,y=rng.randrange(240),rng.randrange(240);d=rng.randint(-40,40);draw.ellipse((x,y,x+2,y+2),fill=tuple(max(0,min(255,v+d)) for v in rgb))
   if category=='tile':
    for x in [0,80,160,239]:draw.line((x,0,x,239),fill=(220,220,220),width=3);draw.line((0,x,239,x),fill=(220,220,220),width=3)
   id=f'M{i:02}';im.save(ROOT/f'static/swatches/{id}.png');rows.append({'id':id,'name':f'{color.title()} {pattern} {category}','description':f'{color} {pattern} {category} material sample','category':category,'color':color,'pattern':pattern,'image':f'/static/swatches/{id}.png'})
(ROOT/'data').mkdir(exist_ok=True);(ROOT/'data/materials.json').write_text(json.dumps(rows,indent=2))
