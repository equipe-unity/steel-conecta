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
src=src.replace('/04','/05')
src=src.replace("d.text((M,y),q,font=font(40),fill=WHITE); y+=64","(d.text((M,y),q,font=font(40),fill=WHITE) if q else None); y+=(64 if q else 0)")
src=src.replace("if cta: block+=40+120","if cta: block+=40+(120 if cta[0] else 64)")
exec(src)
import os
os.makedirs('slides_institucional',exist_ok=True)
slide(1,'Construção **a seco:** como a Steel Conecta executa a sua obra.',68,['Do projeto à obra entregue, em quatro etapas.'],'fotos/inst-montador-trelica.jpg',0.45,out='slides_institucional/slide-1.png',bs=36)
slide_bottom(2,'O que é construção **a seco**',68,['Sistemas construtivos que usam perfis de aço e placas de fechamento, como o Steel Frame e o drywall.'],'fotos/inst-equipe-fechamento.jpg',0.50,out='slides_institucional/slide-2.png',bs=36)
slide(3,'Como **trabalhamos**',72,['1. Análise do projeto','2. Planejamento das etapas','3. Execução em campo','4. Controle e acompanhamento da obra'],'fotos/inst-equipe-planejando.jpg',0.45,out='slides_institucional/slide-3.png',bs=36)
slide_bottom(4,'O que **executamos**',72,['• Estrutura em Steel Frame, conforme o projeto','• Fechamento: placas, fachadas e revestimentos','• Reformas em drywall'],'fotos/dw-parede-verde-eletrica.jpg',0.50,out='slides_institucional/slide-4.png',bs=36)
slide(5,'Quer entender como seria a execução do **seu projeto?**',64,['Envie para a Steel Conecta e solicite uma análise.','Siga o perfil para acompanhar conteúdos sobre construção a seco.'],'fotos/inst-montador-encaixe.jpg',0.58,cta=('','Envie seu projeto para análise.'),arrow=False,out='slides_institucional/slide-5.png',bs=34)
