# Post 09/10 - "O detalhe que ninguém vê" (3 slides). Reutiliza as funções de gerar2.py
src=open('gerar2.py',encoding='utf-8').read()
src=src[:src.index("os.makedirs('slides'")]
src=src.replace("/04","/03")
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
os.makedirs('slides_0910',exist_ok=True)
slide(1,'O detalhe que ninguém vê decide o **acabamento** da sua obra.',70,['Na execução em Steel Frame, o que não é previsto na estrutura aparece depois, no fechamento.'],'fotos/vao-glasroc-limpo.jpg',0.62,out='slides_0910/slide-1.png',bs=34)
slide_bottom(2,'Onde o **detalhe** faz diferença',70,['• Vãos de portas e janelas','• Reforços previstos em projeto','• Encontro entre estrutura, fechamento e instalações','O que não é conferido antes de fechar vira correção depois.'],'fotos/reforco-equipe.jpg',0.40,out='slides_0910/slide-2.png',bs=33)
slide(3,'Execução com planejamento e **controle.**',66,['A Steel Conecta organiza as etapas e acompanha a execução, do projeto ao fechamento.'],'fotos/estrutura-interna-tyvek.jpg',0.30,cta=('Quer revisar a execução do seu projeto?','Envie para a Steel Conecta.'),arrow=False,out='slides_0910/slide-3.png',bs=34)
