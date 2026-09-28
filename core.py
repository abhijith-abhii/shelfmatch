from pathlib import Path
import json,math
import numpy as np
from PIL import Image
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
ROOT=Path(__file__).parent

def descriptor(image):
 arr=np.asarray(image.convert('RGB').resize((64,64)),dtype=float)/255
 hist=np.concatenate([np.histogram(arr[:,:,c],bins=8,range=(0,1),density=False)[0]/4096 for c in range(3)])
 texture=np.array([np.abs(np.diff(arr,axis=a)).mean() for a in [0,1]])
 return np.concatenate([hist,texture*4])
def rank(query='',image_id='none',weight=.6,category='all'):
 rows=json.loads((ROOT/'data/materials.json').read_text());ids=[r['id'] for r in rows]
 if not isinstance(query,str) or len(query)>500:raise ValueError('Query must be at most 500 characters')
 if image_id not in ['none']+ids:raise ValueError('Unknown reference image')
 if not math.isfinite(weight) or not 0<=weight<=1:raise ValueError('Weight must be 0–1')
 if category not in ['all','fabric','tile']:raise ValueError('Unsupported category')
 if not query.strip() and image_id=='none':raise ValueError('Enter text or choose a reference image')
 v=TfidfVectorizer(ngram_range=(1,2));x=v.fit_transform([r['description'] for r in rows]);text=cosine_similarity(v.transform([query]),x)[0]
 features=np.stack([descriptor(Image.open(ROOT/r['image'].lstrip('/'))) for r in rows]);visual=cosine_similarity(features[[ids.index(image_id)]],features)[0] if image_id!='none' else np.zeros(len(rows))
 alpha=weight if image_id!='none' and query.strip() else 1 if query.strip() else 0
 result=[]
 for i,r in enumerate(rows):
  if category!='all' and r['category']!=category:continue
  result.append({**r,'text_score':round(float(text[i]),4),'visual_score':round(float(visual[i]),4),'score':round(float(alpha*text[i]+(1-alpha)*visual[i]),4)})
 return sorted(result,key=lambda x:(-x['score'],x['id']))
def analyze(p):
 rows=rank(p.get('query','blue striped fabric'),p.get('image_id','none'),float(p.get('weight',.6)),p.get('category','all'))
 return dict(metrics={'Matching materials':len(rows),'Best score':rows[0]['score'] if rows else 0},rows=rows,details={'method':'TF-IDF cosine + color-histogram/texture cosine; explicitly engineered visual baseline','data':'16 original procedural swatches; MIT','weight_semantics':'Text weight applies only when both modalities are present'},notice='Scores measure similarity within this sample catalog, not probabilities or product quality. Visual reference is selected from the catalog; arbitrary uploads are not supported.')
