# Post 24/10 - o que enviar para a análise do projeto (4 slides). Reutiliza as funções de gerar2.py
src=open('gerar2.py',encoding='utf-8').read()
src=src[:src.index("os.makedirs('slides'")]
src=src.replace("def draw_text(d,y,text,f,lh,default,maxw=W-2*M):","def draw_text(d,y,text,f,lh,default,maxw=W-2*M,x0=None):")
src=src.replace("        x=M\n        for word,c in line:","        x=M if x0 is None else x0\n        for word,c in line:")
src=src.replace("y=draw_text(d,y,p,font(bs,False),int(bs*1.42),SOFT); y+=14","y=para(d,y,p,bs)")
src=src.replace("def measure(","""def para(d,y,p,bs):
    if p.startswith('• '):
        d.rectangle([M,y+int(bs*0.62),M+18,y+int(bs*0.62)+5],fill=GOLD)
        y=draw_text(d,y,p[2:],font(bs,False),int(bs*1.42),WHITE,maxw=W-2*M-40,x0=M+40)
        return y+10
    return draw_text(d,y,p,font(bs,False),int(bs*1.42),SOFT)+14
def measure(""",1)
src=src.replace("g0=ytxt-430; g1=ytxt+40","g0=ytxt-240; g1=ytxt-10")
src=src.replace("fade=min(380,ph-80)","fade=min(200,ph-80)")
src=src.replace("logo_y=H-150","logo_y=H-125").replace("ytxt=logo_y-70-block","ytxt=logo_y-45-block")
src=src.replace("draw_text(d,200,headline","draw_text(d,170,headline")
src=src.replace("    return im.crop((left,top,left+w,top+h))","    from PIL import ImageEnhance\n    im=ImageEnhance.Color(ImageEnhance.Contrast(im).enhance(1.10)).enhance(1.12)\n    return im.crop((left,top,left+w,top+h))")
exec(src)
import os
os.makedirs('slides_24_10',exist_ok=True)
slide(1,'O que enviar para a análise do **seu projeto.**',70,['Quanto mais completo o material, mais precisa a análise.'],'fotos/campo-montanhas.jpg',0.50,out='slides_24_10/slide-1.png',bs=36)
slide_bottom(2,'1. Projeto de **arquitetura**',70,['Plantas, cortes e fachadas.'],'fotos/planta-estudo-prancheta.jpg',0.55,out='slides_24_10/slide-2.png',bs=38)
slide(3,'2. Projetos **complementares**',66,['Estrutural, elétrico e hidráulico, quando já existirem.'],'fotos/planta-pontos-eletricos-quadro.jpg',0.50,out='slides_24_10/slide-3.png',bs=36)
slide_bottom(4,'3. Memorial e **escopo**',70,['Materiais, acabamentos e o que você espera da execução.'],'fotos/inst-equipe-planejando.jpg',0.50,cta=('Salve este post para consultar depois.','Envie seu projeto para análise.'),arrow=False,out='slides_24_10/slide-4.png',bs=34)
