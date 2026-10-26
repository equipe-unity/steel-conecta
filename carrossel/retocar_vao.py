# Retoca fotos/vao-glasroc-sem-moto.jpg: esvazia a abertura da janela e remove entulho/paletes da base
import numpy as np, cv2
from PIL import Image, ImageFilter, ImageDraw
src=Image.open('fotos/vao-glasroc-sem-moto.jpg').convert('RGB')
W,H=src.size
img=src.copy()
def mask_poly(pts,feather):
    m=Image.new('L',(W,H),0); ImageDraw.Draw(m).polygon(pts,fill=255)
    return m.filter(ImageFilter.GaussianBlur(feather))
# A) interior da abertura grande: usa o interior escuro da janela da esquerda (mesmo tipo de vão)
left=src.crop((340,2090,545,2500)).resize((540,640),Image.LANCZOS)
fill=Image.new('RGB',(W,H),(0,0,0)); fill.paste(left,(1008,1960))
shade=Image.new('L',(W,H),0)
sd=np.zeros((H,W),np.float32)
yy=np.linspace(0,1,640)[:,None]
sd[1960:2600,1008:1548]=(1-0.35*(1-yy))   # sombra no topo
fill=Image.fromarray((np.array(fill).astype(np.float32)*sd[...,None]).astype('uint8'))
poly=[(1012,1998),(1538,1952),(1545,2618),(1012,2578)]
img=Image.composite(fill,img,mask_poly(poly,3))
# B) entulho: clona parede limpa (mesmo padrão impresso) por cima
def clone(img,pts,dy,dx=0,feather=10):
    shifted=Image.new('RGB',(W,H))
    shifted.paste(img.crop((0-dx,0-dy,W-dx,H-dy)) if False else img.transform((W,H),Image.AFFINE,(1,0,dx,0,1,dy)),(0,0))
    return Image.composite(shifted,img,mask_poly(pts,feather))
th=lambda p:(p[0]*3,p[1]*3+2200)
M1=[(110,2420),(300,2400),(332,2520),(326,2820),(190,2880),(40,2780),(50,2600)]
M2=[(60,2700),(820,2700),(835,2740),(915,3004),(1335,3064),(1335,3140),(60,3140)]
img=clone(img,M1,-600)
img=clone(img,M2,-1100)
img.save('fotos/vao-glasroc-limpo.jpg',quality=95)
img.crop((0,1800,2124,3300)).resize((708,500)).save('check_limpo.png')
