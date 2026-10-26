# Post drywall - checklist antes de fechar a parede (4 slides). Reutiliza as funções de gerar2.py
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
os.makedirs('slides_drywall',exist_ok=True)
slide(1,'Antes de fechar a parede de **drywall,** confira isto.',70,['Depois de fechada, qualquer correção vira retrabalho.'],'fotos/dw-estrutura-parede-aberta.jpg',0.55,out='slides_drywall/slide-1.png',bs=36)
slide_bottom(2,'1. **Instalações**',72,['Elétrica, hidráulica e pontos embutidos posicionados e conferidos antes do fechamento.'],'fotos/dw-parede-verde-eletrica.jpg',0.50,out='slides_drywall/slide-2.png',bs=36)
slide(3,'2. **Reforços**',72,['Defina onde vão TV, armários, bancadas e prateleiras. O reforço precisa estar previsto na estrutura da parede.'],'fotos/cmp-painel-instalacoes.jpg',0.50,out='slides_drywall/slide-3.png',bs=34)
slide_bottom(4,'3. **Medidas** e aberturas',70,['Alturas, vãos e aberturas conferidos com o projeto antes de fechar.'],'fotos/dw-parede-interna-perfis.jpg',0.55,cta=('Salve este post para consultar antes da reforma.','Vai reformar com drywall? Fale com a Steel Conecta.'),arrow=False,out='slides_drywall/slide-4.png',bs=34)
