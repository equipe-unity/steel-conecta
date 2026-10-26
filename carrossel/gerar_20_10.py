# Post estático 20/10 - quem executa entra antes. Reutiliza as funções de gerar2.py
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
import re
src=re.sub(r"    d\.text\(\(M,70\),f'0\{n\}/0\d'.*\n","",src)
src=src.replace("d.text((M,y),q,font=font(40),fill=WHITE); y+=64","(d.text((M,y),q,font=font(40),fill=WHITE) if q else None); y+=(64 if q else 0)")
src=src.replace("if cta: block+=40+120","if cta: block+=40+(120 if cta[0] else 64)")
exec(src)
import os
os.makedirs('slides_20_10',exist_ok=True)
slide(1,'Quem executa deve entrar **antes** de a obra começar.',72,['Vãos, reforços e instalações previstos desde o projeto ajudam a evitar ajustes depois.'],'fotos/equipe-estrutura-cobertura.jpg',0.38,cta=('','Fale com a Steel Conecta.'),arrow=False,out='slides_20_10/post-executora-antes.png',bs=34)
