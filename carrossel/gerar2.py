from PIL import Image, ImageDraw, ImageFont, ImageOps
import numpy as np, os
W,H=1080,1350; M=80
NAVY=(23,66,99); GOLD=(219,160,78); WHITE=(255,255,255); SOFT=(214,224,234)
F='C:/Windows/Fonts/'
def font(sz,b=True): return ImageFont.truetype(F+('arialbd.ttf' if b else 'arial.ttf'),sz)
# logo branco: tudo que for azul vira branco; dourado mantido; ícone vira branco translúcido
lg=np.array(Image.open('fotos/logo.png').convert('RGBA')).astype(int)
r,g,b,a=lg[...,0],lg[...,1],lg[...,2],lg[...,3]
blue=(b>r+20)
lg[blue,0:3]=255
pale=(~blue)&(r>225)&(g>225)&(b>225)&(a>0)
lg[pale,0:3]=255; lg[pale,3]=(lg[pale,3]*0.55).astype(int)
logo=Image.fromarray(lg.astype('uint8'),'RGBA')
def draw_text(d,y,text,f,lh,default,maxw=W-2*M):
    parts=[];gold=False
    for tok in text.split(' '):
        g=gold
        if tok.startswith('**'): gold=True;g=True;tok=tok[2:]
        if tok.endswith('**'): tok=tok[:-2];gold=False
        parts.append((tok,GOLD if g else default))
    lines=[[]];w=0;sp=d.textlength(' ',font=f)
    for word,c in parts:
        ww=d.textlength(word,font=f)
        if w+ww>maxw and lines[-1]: lines.append([]);w=0
        lines[-1].append((word,c));w+=ww+sp
    for line in lines:
        x=M
        for word,c in line:
            if d is not None and y is not None: d.text((x,y),word,font=f,fill=c)
            x+=d.textlength(word,font=f)+sp
        y+=lh
    return y
def measure(text,f,lh,maxw=W-2*M):
    d=ImageDraw.Draw(Image.new('RGB',(10,10)))
    return draw_text(d,0,text,f,lh,WHITE,maxw)
def photo(path,w,h,focus,ctop=None):
    im=ImageOps.exif_transpose(Image.open(path)).convert('RGB')
    s=max(w/im.width,h/im.height); im=im.resize((round(im.width*s),round(im.height*s)),Image.LANCZOS)
    left=(im.width-w)//2; top=int(max(0,min(im.height-h,im.height*focus-h/2))) if ctop is None else ctop
    return im.crop((left,top,left+w,top+h))
def slide(n,headline,hs,body,pimg,focus,cta=None,arrow=True,out=None,bs=34,ctop=None):
    # altura do bloco de texto (de baixo para cima)
    hh=measure(headline,font(hs),int(hs*1.14))
    bh=sum(measure(p,font(bs,False),int(bs*1.42))+14 for p in body)
    block=hh+24+bh
    if cta: block+=40+120
    logo_y=H-150
    ytxt=logo_y-70-block
    # foto até logo abaixo do início do texto (para o degradê terminar atrás do texto)
    ph=ytxt+150
    img=Image.new('RGB',(W,H),NAVY)
    img.paste(photo(pimg,W,ph,focus,ctop),(0,0))
    # degradê foto -> azul
    g0=ytxt-430; g1=ytxt+40
    arr=np.array(img).astype(float)
    for y in range(max(0,g0),min(H,ph+1)):
        t=min(1,max(0,(y-g0)/(g1-g0))); t=t*t*(3-2*t)
        arr[y]=arr[y]*(1-t)+np.array(NAVY)*t
    for y in range(0,220):
        arr[y]=arr[y]*(1-0.45*(1-y/220))+np.array(NAVY)*0.45*(1-y/220)
    img=Image.fromarray(arr.astype('uint8')); d=ImageDraw.Draw(img)
    # leve escurecimento no topo p/ legibilidade da numeração
    d.text((M,70),f'0{n}/04',font=font(28),fill=WHITE)
    y=draw_text(d,ytxt,headline,font(hs),int(hs*1.14),WHITE)
    y+=24
    for p in body:
        y=draw_text(d,y,p,font(bs,False),int(bs*1.42),SOFT); y+=14
    if cta:
        q,btn=cta; y+=34
        d.text((M,y),q,font=font(40),fill=WHITE); y+=64
        d.rectangle([M,y,W-M,y+72],fill=GOLD)
        d.text((W//2,y+36),btn,font=font(31),fill=NAVY,anchor='mm')
    lw=330; l=logo.resize((lw,round(lw*logo.height/logo.width)),Image.LANCZOS)
    img.paste(l,(M-10,logo_y),l)
    if arrow:
        cx,cy=W-M-30,logo_y+l.height//2
        d.ellipse([cx-30,cy-30,cx+30,cy+30],outline=GOLD,width=4)
        d.line([cx-12,cy,cx+12,cy],fill=GOLD,width=4); d.line([cx+3,cy-10,cx+13,cy],fill=GOLD,width=4); d.line([cx+3,cy+10,cx+13,cy],fill=GOLD,width=4)
    img.save(out)

def slide_bottom(n,headline,hs,body,pimg,focus,cta=None,arrow=True,out=None,bs=34):
    img=Image.new('RGB',(W,H),NAVY); d=ImageDraw.Draw(img)
    lw=330; l=logo.resize((lw,round(lw*logo.height/logo.width)),Image.LANCZOS)
    img.paste(l,(M-10,62),l)
    d.text((W-M,86),f'0{n}/04',font=font(28),fill=WHITE,anchor='ra')
    y=draw_text(d,200,headline,font(hs),int(hs*1.14),WHITE); y+=24
    for p in body:
        y=draw_text(d,y,p,font(bs,False),int(bs*1.42),SOFT); y+=14
    if cta:
        q,btn=cta; y+=34
        d.text((M,y),q,font=font(40),fill=WHITE); y+=64
        d.rectangle([M,y,W-M,y+72],fill=GOLD)
        d.text((W//2,y+36),btn,font=font(31),fill=NAVY,anchor='mm'); y+=72
    top=y-40+0; top=int(y+10)
    ph=H-top
    ph_img=np.array(photo(pimg,W,ph,focus)).astype(float)
    fade=min(380,ph-80)
    for r in range(fade):
        t=r/fade; t=t*t*(3-2*t)
        ph_img[r]=ph_img[r]*t+np.array(NAVY)*(1-t)
    img.paste(Image.fromarray(ph_img.astype('uint8')),(0,top)); d=ImageDraw.Draw(img)
    if arrow:
        cx,cy=W-M-30,H-80
        d.ellipse([cx-30,cy-30,cx+30,cy+30],fill=NAVY,outline=GOLD,width=4)
        d.line([cx-12,cy,cx+12,cy],fill=GOLD,width=4); d.line([cx+3,cy-10,cx+13,cy],fill=GOLD,width=4); d.line([cx+3,cy+10,cx+13,cy],fill=GOLD,width=4)
    img.save(out)
os.makedirs('slides',exist_ok=True)
slide(1,'Seu projeto precisa de execução em **Steel\u00a0Frame?**',78,['Conheça os serviços da Steel Conecta.'],'fotos/campo-montanhas.jpg',0.50,out='slides/slide-1.png',bs=38)
slide_bottom(2,'Execução da estrutura em **Steel\u00a0Frame**',70,['Montagem dos perfis, painéis, travamentos e demais elementos estruturais conforme o projeto.'],'fotos/painel-equipe.jpg',0.50,out='slides/slide-2.png')
slide(3,'Execução de sistemas de **fechamento**',70,['Aplicação de placas, fachadas, revestimentos e demais soluções previstas no escopo da obra.','Também podemos atuar na integração das etapas necessárias à execução, conforme a necessidade do projeto.'],'fotos/glasroc-fachada-andaime.jpg',0.40,out='slides/slide-3.png',bs=31)
slide_bottom(4,'Da estrutura ao **acompanhamento** da obra.',66,['A Steel Conecta trabalha com planejamento, organização das etapas e controle da execução.'],'fotos/dois-pavimentos.jpg',0.45,cta=('Tem um projeto para executar?','Envie para nossa equipe e solicite uma análise.'),arrow=False,out='slides/slide-4.png')
