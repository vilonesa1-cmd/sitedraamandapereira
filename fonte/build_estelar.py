import re
old=open('/mnt/user-data/outputs/amanda-pereira-previa.html',encoding='utf-8').read()
head=old[:old.index('<style>')]
logo=re.search(r'<nav id="nav">.*?<img src="(data:image/png;base64,[^"]+)"',old,re.S).group(1)
photo=re.search(r'<div class="photo" id="photo"><img src="(data:image/jpeg;base64,[^"]+)"',old,re.S).group(1)

import base64,io
from PIL import Image
A='/mnt/user-data/attachments/70a0c245-7fd5-5c63-879b-2604a505d588/'
PF=Image.open(A+'461143f4-image.jpg').convert('RGB')
PF=PF.resize((900,round(PF.size[1]*900/PF.size[0])),Image.LANCZOS)
_b=io.BytesIO();PF.save(_b,'JPEG',quality=80,optimize=True);PHOTO2='data:image/jpeg;base64,'+base64.b64encode(_b.getvalue()).decode()
PF_H=PF.size[1]
BA=[]
CEN={'622c5819':.41,'d29d4ce6':.40,'0646ccd7':.42,'aa98d706':.42,'5fad84f4':.48,'513b4b21':.41}
def _enc(im):
    bb=io.BytesIO();im.save(bb,'JPEG',quality=76,optimize=True);return 'data:image/jpeg;base64,'+base64.b64encode(bb.getvalue()).decode()
for f in ['622c5819','d29d4ce6','0646ccd7','aa98d706','5fad84f4','513b4b21']:
    im=Image.open(A+f+'-image.jpg').convert('RGB')
    w,h=im.size;m=8;hw=w//2
    parts=[im.crop((0,0,hw-m,h)),im.crop((hw+m,0,w,h))]
    out=[]
    for q in parts:
        qw,qh=q.size;ch=min(qh,round(qw*8/5));top=int(max(0,min(qh-ch,qh*CEN[f]-ch/2)))
        q=q.crop((0,top,qw,top+ch)).resize((560,round(ch*560/qw)),Image.LANCZOS);out.append(_enc(q))
    BA.append(out)
WA="https://api.whatsapp.com/send/?phone=5531998420605&text=Oi%21%20Vim%20do%20site%20da%20Dr%C2%AA.%20Amanda%20e%20gostaria%20de%20agendar%20uma%20avalia%C3%A7%C3%A3o."
MAP="https://www.google.com/maps/search/?api=1&query=Av.+dos+Andradas+3323+Santa+Efig%C3%AAnia+Belo+Horizonte+MG"
EMB="https://maps.google.com/maps?q=Av.+dos+Andradas+3323+Santa+Efig%C3%AAnia+Belo+Horizonte+MG&output=embed"

css='''
:root{--bege:#C8A97E;--taupe:#6B5444;--marrom:#3B2D25;--hero:#5d493c;--areia:#E8DCCB;--creme:#F7F3EC;--texto:#2B2420;--ink-2:#5b4d44;
--serif:"Cormorant Garamond",Georgia,serif;--sans:"Manrope",system-ui,sans-serif;
--fs-xs:13px;--fs-sm:15px;--fs-body:17px;--fs-lead:20px;--fs-h4:24px;--fs-h3:32px;--fs-h2:clamp(34px,4.4vw,56px);--fs-h1:clamp(38px,5.4vw,76px);
--s1:8px;--s2:16px;--s3:24px;--s4:40px;--s5:64px;--block:clamp(40px,6vw,64px);--sec:clamp(72px,9vw,120px);--gap:clamp(32px,6vw,80px);
--r-sm:3px;--r-md:6px;--r-lg:20px;--pill:999px;--line:rgba(107,84,68,.25);--sh-card:0 24px 60px -34px rgba(107,84,68,.45);--measure:60ch}
*,*::before,*::after{box-sizing:border-box}
html{scroll-behavior:smooth;scroll-padding-top:84px}
body{margin:0;color:var(--texto);font:400 var(--fs-body)/1.65 var(--sans);background:linear-gradient(135deg,#f7f1ea 0%,#e5ece8 42%,#eee4da 76%,#f9f4ee 100%) fixed;position:relative;isolation:isolate;overflow-x:hidden}
body::before{content:"";position:fixed;inset:-8%;z-index:-1;pointer-events:none;background:radial-gradient(ellipse 34% 25% at 14% 18%,rgba(239,199,179,.58),transparent 70%),radial-gradient(ellipse 30% 28% at 79% 28%,rgba(198,177,155,.45),transparent 72%),radial-gradient(ellipse 36% 28% at 62% 82%,rgba(241,218,221,.7),transparent 72%),radial-gradient(ellipse 28% 24% at 8% 78%,rgba(229,236,232,.8),transparent 70%);filter:blur(46px)}
img{max-width:100%;display:block}a{color:inherit}
h1,h2,h3{font-family:var(--serif);font-weight:400;line-height:1.08;margin:0;text-wrap:balance}
h2{font-size:var(--fs-h2);max-width:22ch}
p{max-width:var(--measure);margin:0}
.wrap{max-width:1120px;margin:0 auto;padding:0 28px}
section{padding:var(--sec) 0}
.sand,.deep{position:relative}.sand::before,.deep::before{content:"";position:absolute;inset:0;z-index:0;pointer-events:none;backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px)}
.sand::before{background:rgba(255,253,249,.42)}
.deep::before{background:rgba(214,196,176,.55)}
.kicker{font-size:var(--fs-xs);font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:var(--taupe);margin:0 0 var(--s2)}
.lead{font-size:var(--fs-lead);line-height:1.55;color:var(--ink-2);margin-top:var(--s3)}
.micro{font-size:var(--fs-sm);color:var(--ink-2);margin-top:var(--s2)}
:focus-visible{outline:2px solid var(--bege);outline-offset:3px}
.skip{position:absolute;left:-999px;top:8px;z-index:90;background:var(--creme);color:var(--marrom);padding:10px 16px;border-radius:var(--r-sm)}.skip:focus{left:12px}
/* botões e links */
.btn{display:inline-flex;align-items:center;justify-content:center;min-height:48px;padding:12px 28px;background:var(--hero);color:#fffcf8;text-decoration:none;font-weight:500;font-size:var(--fs-sm);border-radius:var(--r-sm);border:1px solid var(--hero);transition:background .25s,transform .25s,color .25s}
.btn:hover{background:var(--marrom)}.btn:active{transform:translateY(1px)}
.btn.light{background:#fffcf8;color:var(--hero);border-color:var(--bege)}.btn.light:hover{background:var(--areia)}
.btn.gold{background:var(--bege);color:var(--marrom);border-color:var(--bege)}.btn.gold:hover{background:#d8bd96}
.btn.pill{border-radius:var(--pill);min-height:44px;padding:10px 22px}
.link{display:inline-block;text-decoration:none;border-bottom:1px solid var(--bege);padding-bottom:3px;font-size:var(--fs-sm);font-weight:500}
.actions{display:flex;flex-wrap:wrap;align-items:center;gap:var(--s2) var(--s3)}
/* nav */
nav{position:fixed;inset:0 0 auto 0;z-index:50;background:rgba(247,243,236,.92);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);border-bottom:1px solid rgba(107,84,68,.14);padding-top:env(safe-area-inset-top,0)}
nav .wrap{display:flex;align-items:center;justify-content:space-between;gap:var(--s3);height:72px;max-width:1240px}
nav .logo img{height:50px;mix-blend-mode:multiply}
nav ul{display:flex;gap:28px;list-style:none;margin:0;padding:0;font-size:var(--fs-sm)}
nav ul a{text-decoration:none;opacity:.8}nav ul a:hover{opacity:1}
.bar{position:absolute;left:0;bottom:-1px;height:2px;width:100%;background:var(--bege);transform-origin:left;transform:scaleX(var(--p,0))}
.menu{all:unset;display:none;cursor:pointer;width:44px;height:44px;align-items:center;justify-content:center}
.menu span,.menu span::before,.menu span::after{display:block;width:22px;height:2px;background:var(--marrom);content:"";position:relative}
.menu span::before{position:absolute;top:-7px}.menu span::after{position:absolute;top:7px}
/* hero */
.hero{position:relative;min-height:100svh;padding:0;background:var(--hero);color:#fffcf8;overflow:hidden;display:flex;align-items:center}
.hero img.bg{position:absolute;right:0;top:0;height:100%;width:62%;object-fit:cover;object-position:50% 14%;-webkit-mask-image:linear-gradient(90deg,transparent 0,#000 38%);mask-image:linear-gradient(90deg,transparent 0,#000 38%)}
.hero::after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgba(60,44,35,.55),transparent 55%);pointer-events:none}
.hero .wrap{position:relative;z-index:2;padding-top:120px;padding-bottom:80px;width:100%}
.hero .id{font-size:var(--fs-xs);font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:#efe4d6;margin-bottom:var(--s3)}
.hero h1{font-size:var(--fs-h1);color:#fffcf8;line-height:1.02;max-width:12ch}
.em{position:relative;display:inline-block;font-style:italic}
.em::after{content:"";position:absolute;left:0;right:0;bottom:-.06em;height:.09em;background:var(--bege);border-radius:99px;transform-origin:left;transform:scaleX(0);animation:ul 1.1s .9s forwards cubic-bezier(.2,.8,.2,1)}
@keyframes ul{to{transform:scaleX(1)}}
.hero p.sub{font-size:var(--fs-lead);line-height:1.55;color:#f1e7da;max-width:36ch;margin:var(--s3) 0 var(--s4)}
.hero .reass{font-size:var(--fs-sm);color:#efe3d3;margin-top:var(--s2);max-width:44ch}.hero .city{font-size:var(--fs-sm);color:#e6d8c6;margin-top:var(--s3)}
/* faixa */
.strip{background:var(--taupe);color:#f3e9dc;overflow:hidden;padding:18px 0;white-space:nowrap;font-size:var(--fs-xs);letter-spacing:.16em;text-transform:uppercase;font-weight:600}
.strip div{display:inline-flex;gap:0;animation:mq 38s linear infinite}
.strip span{padding:0 28px;position:relative}.strip span::after{content:"";position:absolute;right:-3px;top:50%;width:6px;height:6px;background:var(--bege);transform:translateY(-50%) rotate(45deg)}
@keyframes mq{to{transform:translateX(-50%)}}
/* sobre */
.about{display:grid;grid-template-columns:.85fr 1.15fr;gap:var(--gap);align-items:center}
.arch{position:relative}
.arch .ph{aspect-ratio:3/4;border-radius:999px 999px var(--r-md) var(--r-md);overflow:hidden;background:var(--areia)}
.arch img{width:100%;height:100%;object-fit:cover;object-position:50% 22%}
.cap{position:absolute;left:-8px;bottom:-22px;background:#fffcf8;padding:14px 22px;border-left:2px solid var(--bege);box-shadow:var(--sh-card);font-size:var(--fs-sm);max-width:260px;border-radius:2px}
.about p+p{margin-top:var(--s2)}.about .lead{margin:var(--s3) 0 var(--s2)}.about .link{margin-top:var(--s3)}
/* carrossel */
.sh{display:grid;grid-template-columns:7fr 5fr;gap:var(--gap);align-items:end}
.sh p{color:var(--ink-2);justify-self:end}
.ctrl{display:flex;justify-content:space-between;align-items:center;margin:var(--block) 0 var(--s3);font-size:var(--fs-sm);color:var(--ink-2)}
.ctrl .nv{display:flex;align-items:center;gap:var(--s2)}
.arr{all:unset;cursor:pointer;width:44px;height:44px;border-radius:50%;background:#fffcf8;box-shadow:0 6px 18px -8px rgba(59,45,37,.5);display:inline-flex;align-items:center;justify-content:center;transition:background .2s,opacity .2s}
.arr:hover{background:var(--areia)}.arr[disabled]{opacity:.4;cursor:default}
.arr svg{width:18px;height:18px;stroke:var(--marrom);fill:none;stroke-width:1.8}
.track{display:flex;gap:var(--s3);overflow-x:auto;scroll-snap-type:x mandatory;scrollbar-width:none;padding:6px 28px 30px;margin:0 -28px;scroll-padding-left:28px;-webkit-overflow-scrolling:touch}
.track::-webkit-scrollbar{display:none}
.card{flex:0 0 min(340px,82vw);scroll-snap-align:start;background:#fffcf8;border:1px solid var(--line);border-radius:var(--r-md);overflow:hidden;display:flex;flex-direction:column;transition:border-color .25s,transform .25s}
.card:hover{border-color:var(--bege);transform:translateY(-3px)}
.media{position:relative;aspect-ratio:4/3;background:linear-gradient(135deg,#efe1d3,#e7d4c8 55%,#f1dadd);display:flex;align-items:center;justify-content:center;color:rgba(107,84,68,.55);font-family:var(--serif);font-size:var(--fs-h3)}
.media.dim{font-size:var(--fs-sm);font-family:var(--sans)}
.num{position:absolute;left:14px;top:14px;width:34px;height:34px;border-radius:50%;background:#fffcf8;display:flex;align-items:center;justify-content:center;font-size:var(--fs-xs);font-weight:600;color:var(--taupe);box-shadow:0 4px 12px -6px rgba(0,0,0,.3)}
.card .body{padding:var(--s3);display:flex;flex-direction:column;gap:var(--s1);flex:1}
.card .ey{font-size:var(--fs-xs);color:var(--ink-2)}
.card h3{font-size:var(--fs-h4)}.card p{font-size:var(--fs-sm);color:var(--ink-2)}
.card .link{margin-top:auto;align-self:flex-start}
.tag{display:inline-block;font-size:var(--fs-xs);border:1px solid var(--taupe);color:var(--taupe);padding:2px 10px;border-radius:var(--pill);margin-left:10px;vertical-align:middle;font-family:var(--sans)}
.gal .card{flex-basis:min(380px,84vw);background:transparent;border:0}
.gal .media{aspect-ratio:4/5;border-radius:var(--r-lg)}
.gal figcaption{font-size:var(--fs-sm);color:var(--ink-2);padding-top:var(--s1)}
/* especialista */
.spec{display:grid;grid-template-columns:1fr 1fr;gap:var(--gap);align-items:center}
.spec .cred{font-size:var(--fs-xs);font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:var(--taupe);margin:var(--s2) 0 var(--s3)}
.spec p+p{margin-top:var(--s2)}.spec .link{margin-top:var(--s3)}
.hi{background:linear-gradient(transparent 62%,rgba(200,169,126,.45) 62%)}
.spec .ph{aspect-ratio:4/5;border-radius:var(--r-md);overflow:hidden;background:var(--areia);box-shadow:var(--sh-card)}
.spec .ph img{width:100%;height:100%;object-fit:cover;object-position:50% 30%}.spec .ph{position:sticky;top:104px}
/* etapas empilhadas */
.stack{margin-top:var(--block);display:grid;gap:var(--s3);position:relative}
.step{position:sticky;top:calc(96px + var(--i)*14px);display:flex;gap:var(--s3);align-items:center;padding:clamp(24px,4vw,44px);background:#fffcf8;border:1px solid var(--bege);border-radius:var(--r-md);box-shadow:var(--sh-card)}
.step .n{flex:0 0 auto;width:52px;height:52px;border-radius:50%;border:1px solid var(--bege);display:flex;align-items:center;justify-content:center;font-size:var(--fs-sm);color:var(--taupe);background:var(--creme)}
.step h3{font-size:var(--fs-h3);margin-bottom:6px}.step p{font-size:var(--fs-sm);color:var(--ink-2)}
/* resultados */
.res{display:grid;grid-template-columns:5fr 6fr;gap:var(--gap);align-items:center}
.res .lead{margin:var(--s3) 0 var(--s4)}
.ba{margin:0;background:#fffcf8;border:1px solid var(--line);border-radius:var(--r-md);padding:12px;box-shadow:var(--sh-card)}
.ba .pair{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.ba .f{position:relative;aspect-ratio:3/4;border-radius:var(--r-sm);overflow:hidden;background:linear-gradient(135deg,#efe1d3,#e7d4c8 55%,#f1dadd);display:flex;align-items:center;justify-content:center;text-align:center;padding:var(--s2);font-size:var(--fs-sm);color:var(--ink-2)}
.ba .f img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.ba .f b{position:absolute;left:10px;top:10px;background:rgba(255,252,248,.92);font-size:var(--fs-xs);letter-spacing:.12em;text-transform:uppercase;padding:4px 10px;border-radius:var(--pill);color:var(--marrom)}
.ba figcaption{font-size:var(--fs-sm);color:var(--ink-2);padding:var(--s2) 6px 4px}
.ba{min-width:0;width:100%;max-width:440px;justify-self:end;background:none;border:0;padding:0;box-shadow:none;border-radius:0}.ba .track{margin:0;padding:0 0 12px;scroll-padding-left:0;gap:var(--s2)}
.ba .ctrl{margin:0 0 var(--s2)}
.bs{flex:0 0 100%;scroll-snap-align:start;position:relative;border-radius:var(--r-md);overflow:hidden;background:var(--areia);box-shadow:var(--sh-card)}
.bs img{display:block;width:100%;height:auto;aspect-ratio:5/8;object-fit:cover;user-select:none;-webkit-user-drag:none}
.bs .bef{position:absolute;inset:0;height:100%;clip-path:inset(0 calc(100% - var(--x)) 0 0)}
.bs b{position:absolute;top:12px;z-index:3;background:rgba(255,252,248,.92);font-size:var(--fs-xs);letter-spacing:.12em;text-transform:uppercase;padding:4px 12px;border-radius:var(--pill);color:var(--marrom)}
.bs .ln{position:absolute;top:0;bottom:0;left:var(--x);width:2px;margin-left:-1px;background:#fffcf8;z-index:2;pointer-events:none;box-shadow:0 0 8px rgba(0,0,0,.25)}
.hd{position:absolute;top:50%;left:var(--x);z-index:4;width:48px;height:48px;margin:-24px 0 0 -24px;border-radius:50%;background:#fffcf8;box-shadow:0 6px 18px -4px rgba(0,0,0,.45);display:flex;align-items:center;justify-content:center;cursor:ew-resize;touch-action:none}
.hd svg{width:22px;height:22px;fill:none;stroke:var(--marrom);stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}
.hd:focus-visible{outline:2px solid var(--bege);outline-offset:3px}
.cmp.dragging{cursor:ew-resize}.cmp{user-select:none;-webkit-user-select:none}.ctrl [data-count]{white-space:nowrap}
.bs .l1{left:12px}.bs .l2{right:12px}
.media.ph{aspect-ratio:6/7;display:block;padding:0}.media.ph img{width:100%;height:100%;object-fit:cover;object-position:50% 20%}
.media.ph b{position:absolute;bottom:12px;background:rgba(255,252,248,.92);font-size:var(--fs-xs);letter-spacing:.12em;text-transform:uppercase;padding:4px 12px;border-radius:var(--pill);color:var(--marrom)}
.media.ph .l1{left:12px}.media.ph .l2{left:calc(50% + 12px)}

/* simulador de agendamento */
.sim{display:grid;grid-template-columns:7fr 5fr;gap:var(--gap);align-items:start;margin-top:var(--block)}
.form{background:#fffcf8;border:1px solid var(--line);border-radius:var(--r-md);padding:clamp(24px,4vw,44px);box-shadow:var(--sh-card);display:grid;gap:var(--s4)}
.fld legend,.fld>label{display:block;font:400 var(--fs-h4)/1.2 var(--serif);margin:0 0 var(--s1);padding:0}
.fld{border:0;padding:0;margin:0;min-width:0}
.fld .hint{font-size:var(--fs-sm);color:var(--ink-2);margin:0 0 var(--s2)}
.fld .n{display:inline-flex;align-items:center;justify-content:center;width:28px;height:28px;border-radius:50%;border:1px solid var(--bege);font:600 var(--fs-xs) var(--sans);color:var(--taupe);margin-right:10px;vertical-align:middle}
.fi{width:100%;font:inherit;font-size:var(--fs-body);padding:14px 16px;border:1px solid var(--line);border-radius:var(--r-sm);background:#fff;color:var(--texto);transition:border-color .2s,box-shadow .2s}
.fi:focus{outline:none;border-color:var(--bege);box-shadow:0 0 0 3px rgba(200,169,126,.3)}
textarea.fi{min-height:110px;resize:vertical}
.opts{display:flex;flex-wrap:wrap;gap:10px}
.opt{all:unset;box-sizing:border-box;cursor:pointer;min-height:44px;display:inline-flex;align-items:center;padding:8px 18px;border:1px solid var(--line);border-radius:var(--pill);font-size:var(--fs-sm);color:var(--taupe);background:#fff;transition:background .2s,color .2s,border-color .2s,transform .2s}
.opt:hover{border-color:var(--bege);transform:translateY(-1px)}
.opt[aria-pressed=true],.opt[aria-checked=true]{background:var(--hero);color:#fffcf8;border-color:var(--hero)}
.opt:focus-visible{outline:2px solid var(--bege);outline-offset:3px}
.pv{position:sticky;top:104px;display:grid;gap:var(--s3)}
.pv .lbl{font-size:var(--fs-xs);font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:var(--taupe)}
.bubble{background:#fffcf8;border:1px solid var(--line);border-left:3px solid var(--bege);border-radius:var(--r-md);padding:var(--s3);box-shadow:var(--sh-card);font-size:var(--fs-body);line-height:1.55;white-space:pre-line;overflow-wrap:anywhere;min-height:160px}
.pv .btn{width:100%}
.pv .micro{margin:0}
@media(max-width:860px){.sim{grid-template-columns:1fr}.pv{position:static}}
.rev{flex-basis:min(380px,84vw);padding:var(--s4) var(--s3) var(--s3);position:relative}
.rev:hover{transform:none}
.rev .q{position:absolute;top:6px;left:var(--s3);font:400 72px/1 var(--serif);color:var(--bege)}
.rev blockquote{margin:var(--s3) 0 var(--s3);font:400 var(--fs-body)/1.6 var(--sans);color:var(--texto);flex:1}
.rev figcaption{display:flex;flex-direction:column;gap:2px;border-top:1px solid var(--line);padding-top:var(--s2);font-size:var(--fs-sm)}
.rev figcaption b{font-weight:600}.rev figcaption span{color:var(--ink-2);font-size:var(--fs-xs)}
#depoimentos .micro{margin-top:var(--s2)}
/* mito ou verdade */
.mvg{display:grid;grid-template-columns:5fr 6fr;gap:var(--gap);align-items:center}
.mv-score{display:flex;flex-wrap:wrap;gap:10px;margin-top:var(--s3);font-size:var(--fs-sm)}
.mv-score span{border:1px solid var(--line);background:#fffcf8;border-radius:var(--pill);padding:6px 16px;color:var(--taupe)}
.mv-list{grid-column:1/-1;list-style:none;margin:0;padding:0;display:grid;gap:var(--s2)}
.mv-list li{background:#fffcf8;border:1px solid var(--line);border-radius:var(--r-md);padding:var(--s3)}
.mv-list .mv-s{font:400 var(--fs-h4)/1.25 var(--serif);margin-bottom:var(--s1)}
.mv-list .mv-e{font-size:var(--fs-sm);color:var(--ink-2)}
.mv.on .mv-list{display:none}
.mv-stage{position:relative;width:min(100%,380px);height:470px;margin:0 auto;perspective:1200px;outline:none}
.mv-stage:focus-visible{outline:2px solid var(--bege);outline-offset:8px;border-radius:var(--r-lg)}
.mv-card{position:absolute;inset:0;touch-action:pan-y;user-select:none;-webkit-user-select:none;transition:transform .35s cubic-bezier(.2,.8,.2,1),opacity .35s;will-change:transform}
.mv-card.pos0{z-index:3;cursor:grab}.mv-card.pos0.drag{transition:none;cursor:grabbing}
.mv-card.pos1{z-index:2;transform:translateY(14px) scale(.95);pointer-events:none}
.mv-card.pos2{z-index:1;transform:translateY(28px) scale(.9);pointer-events:none}
.mv-card.out{transform:translateX(130%) rotate(14deg);opacity:0;pointer-events:none}
.mv-flip{position:absolute;inset:0;transform-style:preserve-3d;transition:transform .6s cubic-bezier(.2,.8,.2,1)}
.mv-card.flipped .mv-flip{transform:rotateY(180deg)}
.mv-face{position:absolute;inset:0;backface-visibility:hidden;-webkit-backface-visibility:hidden;border-radius:var(--r-lg);padding:clamp(24px,5vw,36px);display:flex;flex-direction:column;box-shadow:var(--sh-card)}
.mv-front{background:#fffcf8;border:1px solid var(--bege);justify-content:center;gap:var(--s3)}
.mv-back{background:#6e2a37;color:#fffcf8;transform:rotateY(180deg);justify-content:center;gap:var(--s2)}
.mv-tag{font-size:var(--fs-xs);font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:var(--taupe);position:absolute;top:26px;left:0;right:0;text-align:center}
.mv-back .mv-tag{color:#e8c9a8}
.mv-st{font:400 clamp(24px,4.4vw,30px)/1.25 var(--serif);text-align:center;max-width:none}
.mv-res{font:400 var(--fs-h3)/1.1 var(--serif);color:#fffcf8}
.mv-ex{font-size:var(--fs-sm);line-height:1.6;color:#f3e4e0;max-width:none}
.mv-fb{font-size:var(--fs-sm);font-weight:600;color:#e8c9a8;max-width:none}
.mv-stamp{position:absolute;top:58px;font:700 22px/1 var(--serif);letter-spacing:.14em;text-transform:uppercase;padding:6px 14px;border:3px solid currentColor;border-radius:6px;opacity:0;pointer-events:none}
.mv-stamp.m{left:20px;color:var(--taupe);transform:rotate(-12deg)}
.mv-stamp.v{right:20px;color:#9a7440;transform:rotate(12deg)}
.mv-hint{position:absolute;left:50%;bottom:-10px;z-index:5;transform:translateX(-50%) rotate(-3deg);background:#f3e2c4;color:var(--marrom);font-size:var(--fs-sm);padding:8px 16px;border-radius:2px;box-shadow:0 8px 18px -8px rgba(59,45,37,.5);white-space:nowrap;transition:opacity .3s}
.mv-hint.gone{opacity:0;pointer-events:none}
.mv-actions{display:flex;justify-content:center;gap:var(--s2);margin-top:var(--s5);flex-wrap:wrap}
.mv-actions .btn{min-width:140px}
.mv-final{position:absolute;inset:0;border-radius:var(--r-lg);background:var(--marrom);color:#fffcf8;padding:clamp(24px,5vw,36px);display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;gap:var(--s2);box-shadow:var(--sh-card)}
.mv-final h3{font-size:var(--fs-h3);color:#fffcf8}.mv-final p{font-size:var(--fs-sm);color:#e8dccb;max-width:30ch}
.mv-fa{display:grid;gap:12px;width:100%;margin-top:var(--s2)}
@media(max-width:860px){.mvg{grid-template-columns:1fr}.mv-stage{height:440px}}
@media(prefers-reduced-motion:reduce){.mv-card,.mv-flip{transition:none}}
/* faixas do instagram */
.ig{margin-top:var(--block);display:grid;gap:var(--s2);overflow:hidden}
.ig-row{overflow:hidden}
.ig-track{display:inline-flex;white-space:nowrap;animation:igm 60s linear infinite;will-change:transform}
.ig-row.rev .ig-track{animation-direction:reverse}
@keyframes igm{from{transform:translateX(0)}to{transform:translateX(-50%)}}
.ig-row:hover .ig-track,.ig-row:focus-within .ig-track,.ig.paused .ig-track{animation-play-state:paused}
.ig-t{flex:0 0 auto;display:block;width:clamp(150px,18vw,220px);aspect-ratio:4/5;margin-right:var(--s2);border-radius:var(--r-md);overflow:hidden;background:var(--areia);position:relative;text-decoration:none}
.ig-t img{width:100%;height:100%;object-fit:cover;display:block}
.ig-t .ph{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,#efe1d3,#e7d4c8 55%,#f1dadd);color:rgba(107,84,68,.55);font:400 var(--fs-h4) var(--serif)}
.ig-t:focus-visible{outline:2px solid var(--bege);outline-offset:-4px}
@media(prefers-reduced-motion:reduce){.ig-track{animation:none}.ig-row{overflow-x:auto}}
/* faq */
.faq{display:grid;grid-template-columns:5fr 7fr;gap:var(--gap);align-items:start}
.faq-h{position:sticky;top:110px}.faq-p{margin:var(--s2) 0 var(--s3);color:var(--ink-2);max-width:38ch}
details{border-top:1px solid var(--line);padding:var(--s3) 0}details:last-child{border-bottom:1px solid var(--line)}details:first-child{border-top:0;padding-top:0}
summary{cursor:pointer;font:400 var(--fs-h4)/1.2 var(--serif);list-style:none;display:flex;justify-content:space-between;gap:20px}
summary::-webkit-details-marker{display:none}summary::after{content:"+";color:var(--bege);transition:transform .3s}
details[open] summary::after{transform:rotate(45deg)}
details p{margin-top:var(--s2);color:var(--ink-2)}
/* convite final (bloco escuro) */
.final{background:var(--marrom);color:#f7f1ea;text-align:center;padding:calc(var(--sec)*1.2) 0;position:relative;overflow:hidden}
.final::before{content:"";position:absolute;inset:0;background:radial-gradient(ellipse 50% 60% at 50% 0,rgba(239,199,179,.22),transparent 70%),radial-gradient(ellipse 40% 50% at 90% 100%,rgba(200,169,126,.2),transparent 70%);pointer-events:none}
.final .wrap{position:relative}
.final h2{margin:0 auto var(--s3);color:#fffcf8}
.final .lead{color:#e8dccb;margin:0 auto var(--s4);max-width:44ch}
.chips{display:flex;flex-wrap:wrap;justify-content:center;gap:12px;margin-bottom:var(--s3)}
.chip{all:unset;cursor:pointer;padding:12px 22px;border:1px solid rgba(247,241,234,.55);border-radius:var(--pill);font-size:var(--fs-sm);color:#f7f1ea;transition:background .25s,color .25s,transform .25s}
.chip:hover{transform:translateY(-2px)}.chip[aria-pressed=true]{background:var(--bege);color:var(--marrom);border-color:var(--bege)}
.prevlabel{font-size:var(--fs-sm);color:#d9c9b4;margin:0 auto var(--s1)}
.prev{font:italic var(--fs-h4)/1.4 var(--serif);max-width:520px;margin:0 auto var(--s4);padding:14px 18px;border-left:2px solid var(--bege);text-align:left;color:#fffcf8}
.final .micro{color:#d9c9b4;margin:var(--s2) auto 0}
/* contato */
.ct{display:grid;grid-template-columns:5fr 6fr;gap:var(--gap);align-items:stretch}
.info{background:#fffcf8;border:1px solid var(--line);border-radius:var(--r-md);padding:clamp(26px,4vw,44px);box-shadow:var(--sh-card)}

/* ramo */
main .wrap{position:relative;z-index:2}.strip{position:relative;z-index:2}
.ramo{position:absolute;left:0;top:0;z-index:1;pointer-events:none;overflow:visible}
.ramo .rl{filter:drop-shadow(0 0 3px rgba(200,169,126,.35))}
.ramo .tip{filter:drop-shadow(0 0 7px rgba(232,201,168,.95)) drop-shadow(0 0 14px rgba(200,169,126,.7))}
.ramo .lf path{transform-box:view-box;transform-origin:0 0;transform:scale(0);transition:transform .7s cubic-bezier(.3,1.6,.5,1)}
.ramo .lf.on path{transform:scale(1)}
.ramo .wv{transform-box:fill-box;transform-origin:center;animation:wv 1.1s ease-out forwards}
@keyframes wv{from{transform:scale(1);opacity:.7}to{transform:scale(7);opacity:0}}
.info.lit{border-color:var(--bege)}.info.pulse{animation:pls 1.7s ease-out 1}
@keyframes pls{0%{box-shadow:var(--sh-card),0 0 0 0 rgba(200,169,126,.75)}60%{box-shadow:var(--sh-card),0 0 0 26px rgba(200,169,126,0)}100%{box-shadow:var(--sh-card),0 0 0 0 rgba(200,169,126,0)}}
@media (prefers-reduced-motion:reduce){.ramo .lf path{transition:none}.info.pulse{animation:none}}
.info dl{margin:var(--s3) 0}.info dt{font-weight:600;font-size:var(--fs-sm);margin-top:var(--s3)}.info dt:first-child{margin-top:0}.info dd{margin:4px 0 0}
.map{border-radius:var(--r-md);overflow:hidden;min-height:340px;background:var(--areia);border:1px solid var(--line)}
.map{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:var(--s1);text-align:center;text-decoration:none;background:linear-gradient(135deg,#efe1d3,#e7d4c8 55%,#f1dadd);transition:border-color .25s}.map:hover{border-color:var(--bege)}.map b{font:400 var(--fs-h4) var(--serif)}.map span:last-child{font-size:var(--fs-sm);color:var(--ink-2);border-bottom:1px solid var(--bege);padding-bottom:3px}.pin{width:18px;height:18px;border-radius:50% 50% 50% 0;transform:rotate(-45deg);background:var(--taupe);margin-bottom:var(--s2)}
/* rodapé */
footer{background:var(--taupe);color:#efe4d6;padding:var(--s5) 0 var(--s4);font-size:var(--fs-sm)}
footer .cols{display:flex;justify-content:space-between;gap:var(--s4);flex-wrap:wrap}
footer b{color:#fffdf9;font:500 var(--fs-h4) var(--serif)}
footer a{text-decoration:underline;text-underline-offset:3px}
.priv{max-width:640px;margin-top:var(--s4);color:#cbbba6}.priv h2{font-size:var(--fs-h4);color:#fffdf9;margin-bottom:var(--s1)}
/* botão flutuante */
.wa{position:fixed;right:18px;bottom:calc(18px + env(safe-area-inset-bottom,0));z-index:60;width:56px;height:56px;border-radius:50%;background:var(--hero);display:flex;align-items:center;justify-content:center;box-shadow:0 10px 26px -8px rgba(59,45,37,.6);transition:opacity .25s,transform .25s}
.wa:hover{transform:scale(1.06)}.wa.off{opacity:0;pointer-events:none}
.wa svg{width:26px;height:26px;fill:none;stroke:#fffcf8;stroke-width:1.7;stroke-linejoin:round;stroke-linecap:round}
/* entrada suave */
.js .rv{opacity:0;transform:translateY(18px);transition:opacity .8s ease,transform .8s cubic-bezier(.2,.8,.2,1)}
.js .rv.in{opacity:1;transform:none}
@media(max-width:860px){
nav ul,nav .btn.pill{display:none}.menu{display:inline-flex}
nav.open ul{display:flex;position:absolute;top:72px;left:0;right:0;flex-direction:column;gap:0;background:rgba(247,243,236,.98);padding:var(--s2) 28px var(--s3);border-bottom:1px solid var(--line)}
nav.open ul a{display:block;padding:14px 0;opacity:1;font-size:var(--fs-body)}
.hero img.bg{width:100%;-webkit-mask-image:none;mask-image:none;opacity:.55;object-position:50% 12%}
.hero::after{background:linear-gradient(180deg,rgba(60,44,35,.2) 0,rgba(60,44,35,.78) 70%)}
.hero{align-items:flex-end}.hero .wrap{padding-top:110px;padding-bottom:56px}
.about,.sh,.spec,.res,.faq,.ct{grid-template-columns:1fr}
.sh p{justify-self:start}.faq-h{position:static}.cap{left:12px;bottom:-26px}
.step{position:static;flex-direction:column;align-items:flex-start}
.arch{max-width:420px}.spec .ph{order:-1;position:static;max-width:460px}
}
/* Fitts: áreas de toque de 44px */
.link{position:relative}.link::before{content:"";position:absolute;inset:-10px -6px}
summary{min-height:44px;align-items:center}
@media(max-width:860px){.ramo .rl{opacity:.5}details{padding:8px 0}details:first-child{padding-top:0}footer a{display:inline-block;padding:12px 0}footer .cols a{margin-right:var(--s2)}}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}.strip div{animation:none}.js .rv{opacity:1;transform:none;transition:none}.em::after{animation:none;transform:none}}
'''

arrow_l='<svg viewBox="0 0 24 24"><path d="M15 5l-7 7 7 7"/></svg>'
arrow_r='<svg viewBox="0 0 24 24"><path d="M9 5l7 7-7 7"/></svg>'
def ctrl(label,n,idx):
    return f'''<div class="ctrl"><span>{label}</span><div class="nv"><button class="arr" type="button" data-dir="-1" aria-label="Anterior">{arrow_l}</button><span data-count>01 / {n:02d}</span><button class="arr" type="button" data-dir="1" aria-label="Próximo">{arrow_r}</button></div></div>'''

procs=[("Harmonização facial","O rosto como um todo","Um plano que considera proporções e equilíbrio entre as regiões do rosto, definido depois da avaliação.","Depende da avaliação",False),
("Tratamento 2","A definir","Descrição a combinar com a Dra. Amanda.","",True),
("Tratamento 3","A definir","Descrição a combinar com a Dra. Amanda.","",True),
("Tratamento 4","A definir","Descrição a combinar com a Dra. Amanda.","",True),
("Tratamento 5","A definir","Descrição a combinar com a Dra. Amanda.","",True),
("Tratamento 6","A definir","Descrição a combinar com a Dra. Amanda.","",True)]
cards=''
for i,(t,e,d,m,c) in enumerate(procs,1):
    cards+=f'''<article class="card"><div class="media ph"><img src="{BA[i-1]}" alt="Antes e depois, caso {i}" width="900" height="1050" loading="lazy"><span class="num">{i:02d}</span><b class="l1">Antes</b><b class="l2">Depois</b></div><div class="body"><div class="ey">{e}</div><h3>{t}{'<span class="tag">prévia</span>' if c else ''}</h3><p>{d}</p><a class="link" href="{WA}" target="_blank" rel="noopener">Avaliar meu caso</a></div></article>'''
gal=''
for i,c in enumerate(["Recepção","Sala de atendimento","Detalhes do consultório"],1):
    gal+=f'<figure class="card" style="margin:0"><div class="media dim"><span class="num">{i:02d}</span>foto: {c.lower()}</div><figcaption>{c}</figcaption></figure>'

bas=''.join(f'<figure class="bs cmp" style="margin:0;--x:50%"><img class="aft" src="{u[1]}" alt="Depois, caso {i}" width="560" height="896" loading="lazy"><img class="bef" src="{u[0]}" alt="Antes, caso {i}" width="560" height="896" loading="lazy"><b class="l1">Antes</b><b class="l2">Depois</b><span class="ln"></span><div class="hd" role="slider" tabindex="0" aria-label="Comparar antes e depois, caso {i}" aria-valuemin="0" aria-valuemax="100" aria-valuenow="50"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 7l-5 5 5 5M15 7l5 5-5 5"/></svg></div></figure>' for i,u in enumerate(BA,1))

html_sim='''<section id="simulador" class="deep"><div class="wrap">
<div class="sh rv"><div><div class="kicker">Agendamento</div><h2>Monte sua mensagem e chame no WhatsApp.</h2></div><p>Escolha o que você procura e a mensagem já sai pronta para a Dra. Amanda.</p></div>
<div class="sim rv">
<div class="form" id="sim">
<div class="fld"><label for="f-nome"><span class="n">1</span>Seu nome</label><input class="fi" id="f-nome" type="text" autocomplete="given-name" maxlength="40" placeholder="Como você se chama?"></div>
<fieldset class="fld"><legend><span class="n">2</span>O que você quer fazer?</legend><p class="hint">Pode marcar mais de uma opção. A indicação final é definida na avaliação.</p><div class="opts" data-grp="proc" role="group">{OPT_PROC}</div></fieldset>
<fieldset class="fld"><legend><span class="n">3</span>Em qual região do rosto?</legend><div class="opts" data-grp="reg" role="group">{OPT_REG}</div></fieldset>
<fieldset class="fld"><legend><span class="n">4</span>Melhor período para você</legend><div class="opts" data-grp="per" role="radiogroup">{OPT_PER}</div></fieldset>
<div class="fld"><label for="f-obs"><span class="n">5</span>Quer contar mais alguma coisa?</label><textarea class="fi" id="f-obs" maxlength="300" placeholder="Ex.: queria suavizar as linhas da testa, nunca fiz antes..."></textarea></div>
</div>
<div class="pv">
<div class="lbl">Mensagem que vai para o WhatsApp</div>
<div class="bubble" id="bubble" aria-live="polite"></div>
<a class="btn" id="simbtn" href="{WA}" target="_blank" rel="noopener">Enviar para a Dra. Amanda pelo WhatsApp</a>
<p class="micro">Você confere e pode editar o texto no WhatsApp antes de enviar. Este site não guarda o que você escreve.</p>
</div>
</div>
</div></section>'''
def opts(lst,mode):
    out=''
    for o in lst:
        if mode=='radio': out+='<button type="button" class="opt" role="radio" aria-checked="false">'+o+'</button>'
        else: out+='<button type="button" class="opt" aria-pressed="false">'+o+'</button>'
    return out
PROC=["Toxina botulínica (botox)","Preenchimento labial","Preenchimento facial","Bioestimulador de colágeno","Contorno de mandíbula e queixo","Olheiras","Rinomodelação","Ainda não sei, quero uma avaliação"]
REG=["Terço superior (testa e olhar)","Terço médio (maçãs e nariz)","Terço inferior (queixo e mandíbula)","Lábios","Rosto todo","Ainda não sei"]
PER=["Manhã","Tarde","Horário flexível"]
SIM=html_sim.replace('{OPT_PROC}',opts(PROC,'chk')).replace('{OPT_REG}',opts(REG,'chk')).replace('{OPT_PER}',opts(PER,'radio')).replace('{WA}',WA)
REVS=[["Carol S.", "Dra. Amanda é sensacional. Há tempos procurava alguém em quem sentisse confiança. Dra. Amanda é uma profissional super qualificada e explicou tudo com muita clareza. Iniciamos o protocolo e em breve estarei de volta."], ["Gabrielly M.", "Atendimento impecável! Ela é super cuidadosa, atenciosa e caprichosa, e o resultado da minha harmonização ficou muito natural e do jeitinho que eu queria. Confio de olhos fechados e recomendo muito!"], ["Livia N.", "A Amanda é uma profissional simplesmente maravilhosa. Sempre muito atenciosa, carinhosa e paciente. Além de competente, demonstra sensibilidade para entender as necessidades de cada paciente e garantir conforto e segurança. Sou muito grata por todo cuidado e dedicação! Recomendo de olhos fechados!"], ["Ana Carolina B.", "Sou simplesmente encantada com os resultados que a Amanda entrega. Uma profissional que planeja muito bem os tratamentos, inclusive os de longo prazo, e os executa com maestria e sem exageros. Parabéns Amanda!"], ["Roberth O.", "Tudo maravilhoso desde o primeiro momento, atenciosa, educada e me explicou todo o procedimento! Deu tudo certo e ficou perfeito!"], ["Igor G.", "Com pouco mais de duas sessões e já vendo avanços, a Dra. Amanda é uma profissional muito capacitada e muito simpática! Não só ela, mas todas as pessoas que trabalham na clínica! Sinto muito à vontade no espaço, então me motiva ainda mais a continuar o tratamento, não só com os resultados, mas com todo o conforto que proporcionam!"], ["Adriana A.", "Excelente experiência e excelente resultado imediato. Atendimento sensacional e Amanda tem muita tranquilidade e paciência ao explicar todos os detalhes e sobre o pós-procedimento!"], ["Danúbia E.", "Excelente profissional. Delicada, gentil e carinhosa! Fiquei muito satisfeita e feliz com o resultado."]]
revcards=''.join(f'<figure class="card rev" style="margin:0"><span class="q" aria-hidden="true">“</span><blockquote>{t}</blockquote><figcaption><b>{n}</b><span>Avaliação no Google</span></figcaption></figure>' for n,t in REVS)

html=head+'<style>'+css+'</style>\n</head>\n<body>\n<a class="skip" href="#conteudo">Pular para o conteúdo</a>\n'
html+=f'''<nav id="nav"><div class="wrap">
<a class="logo" href="#inicio" aria-label="Dra. Amanda Pereira, voltar ao início"><img src="{logo}" alt="Dra. Amanda Pereira" width="94" height="50"></a>
<ul id="menu"><li><a href="#sobre">Sobre</a></li><li><a href="#especialista">Quem atende</a></li><li><a href="#resultados">Resultados</a></li><li><a href="#simulador">Agendamento</a></li><li><a href="#atendimento">Atendimento</a></li><li><a href="#duvidas">Dúvidas</a></li><li><a href="#contato">Contato</a></li></ul>
<a class="btn pill" href="{WA}" target="_blank" rel="noopener">Agendar</a>
<button class="menu" id="mbtn" type="button" aria-label="Abrir menu" aria-expanded="false" aria-controls="menu"><span></span></button>
</div><div class="bar" id="bar"></div></nav>
<main id="conteudo">
<header class="hero" id="inicio">
<img class="bg" src="{photo}" alt="Dra. Amanda Pereira" width="720" height="1280" fetchpriority="high">
<div class="wrap">
<div class="id">Dra. Amanda Pereira · Biomédica esteta · CRBM 22528</div>
<h1>Harmonização facial que começa pelo <span class="em">seu rosto.</span></h1>
<p class="sub">Realce seus traços com naturalidade. O primeiro passo é uma avaliação individual.</p>
<div class="actions"><a class="btn light" id="mag" href="{WA}" target="_blank" rel="noopener">Agendar minha avaliação</a></div>
<p class="reass">Você conversa pelo WhatsApp. A avaliação não obriga a fazer nenhum procedimento.</p>
<p class="city">Santa Efigênia · Belo Horizonte, MG</p>
</div>
</header>
<div class="strip" aria-hidden="true"><div><span>Harmonização facial</span><span>Naturalidade</span><span>Avaliação individual</span><span>Planejamento</span><span>Segurança</span><span>Harmonização facial</span><span>Naturalidade</span><span>Avaliação individual</span><span>Planejamento</span><span>Segurança</span><span>Harmonização facial</span><span>Naturalidade</span><span>Avaliação individual</span><span>Planejamento</span><span>Segurança</span><span>Harmonização facial</span><span>Naturalidade</span><span>Avaliação individual</span><span>Planejamento</span><span>Segurança</span></div></div>

<section id="sobre"><div class="wrap about">
<div class="arch rv"><div class="ph"><img src="{photo}" alt="Dra. Amanda Pereira em atendimento" width="720" height="1280" loading="lazy"></div><div class="cap">A avaliação vem antes do procedimento.</div></div>
<div class="rv">
<div class="kicker">Conheça a profissional</div>
<h2>Antes de qualquer procedimento, um olhar para o seu rosto.</h2>
<p class="lead">Você conta o que gostaria de realçar. A Dra. Amanda avalia o seu rosto e indica o que faz sentido para você.</p>
<p>Você não precisa chegar sabendo o que quer fazer. A primeira conversa serve para entender o seu objetivo e para você tirar as dúvidas antes de decidir.</p>
<a class="link" href="{WA}" target="_blank" rel="noopener">Quero entender o meu caso</a>
</div></div></section>

<section id="especialista"><div class="wrap spec">
<div class="rv">
<div class="kicker">Quem atende</div>
<h2>Quem cuida de você: Dra. Amanda Pereira.</h2>
<div class="cred">Biomédica Esteta · CRBM 22528</div>
<p class="lead" style="margin:0 0 var(--s2)">Oi, eu sou a Amanda, e vou te contar um pouco da minha história.</p>
<p>Eu me lembro como se fosse hoje do meu primeiro dia de aula. Todo mundo chegou super arrumado, e eu cheguei de uniforme e botina 😂 Fazer faculdade foi um sonho misturado com muitos desafios. Eu conciliava trabalho e estudo, porque sem o trabalho não existia o estudo. A rotina era intensa, eu dormia cerca de 4 horas por dia, mas me dediquei ao máximo.</p>
<p>Ainda na faculdade, fiz meu primeiro curso na área da estética. Não foi fácil, mas foi leve, porque eu sempre soube que meu propósito era muito maior que qualquer desafio. Quando o propósito é claro, a gente não tropeça: a gente avança.</p>
<p>Hoje eu vivo o meu propósito, o meu sonho. Transformo autoestima e transformo vidas através do meu trabalho, e sou grata a cada paciente que me permite viver isso.</p>
<p><strong>Será um prazer cuidar de você.</strong></p>
<a class="link" href="https://www.instagram.com/draamandapereira/" target="_blank" rel="noopener">@draamandapereira no Instagram</a>
</div>
<div class="ph rv"><img src="{PHOTO2}" alt="Dra. Amanda Pereira" width="900" height="{PF_H}" loading="lazy"></div>
</div></section>

<section id="resultados" class="sand"><div class="wrap res">
<div class="rv">
<div class="kicker">Resultados</div>
<h2>A mudança faz sentido quando respeita você.</h2>
<p class="lead">Veja casos acompanhados pela Dra. Amanda. Cada resultado é individual.</p>
<a class="btn" href="{WA}" target="_blank" rel="noopener">Quero avaliar o meu caso</a>
</div>
<div class="ba rv" data-car>
{ctrl("Arraste para comparar",6,0)}
<div class="track">{bas}</div>
<p class="micro">Casos individuais. Resultados e tempo de evolução variam de pessoa para pessoa.</p>
</div>
</div></section>

<section id="mito-verdade" class="mv"><div class="wrap mvg">
<div class="mv-txt rv"><div class="kicker">Teste o que você sabe</div><h2>Mito ou verdade sobre a harmonização facial.</h2>
<p class="lead">Arraste a carta para a esquerda (mito) ou para a direita (verdade). São 6 perguntas.</p>
<div class="mv-score" aria-live="polite" hidden><span data-q></span><span data-s></span></div></div>
<div class="mv-game rv" hidden></div>
<ol class="mv-list"><li data-a="verdade"><p class="mv-s">A avaliação individual vem antes de qualquer harmonização.</p><p class="mv-e">Verdade. É na avaliação que a Dra. Amanda entende o que você quer realçar, analisa as proporções do seu rosto e indica o que faz sentido para você.</p></li><li data-a="mito"><p class="mv-s">A harmonização facial muda completamente o seu rosto.</p><p class="mv-e">Mito. O objetivo é realçar e equilibrar os seus traços, respeitando a sua identidade. O plano é individual e se define na avaliação.</p></li><li data-a="verdade"><p class="mv-s">A toxina botulínica (botox) é usada para suavizar linhas de expressão.</p><p class="mv-e">Verdade. Ela relaxa músculos responsáveis por certas linhas de expressão. Mesmo assim, só entra no plano se for indicada para você, depois da avaliação.</p></li><li data-a="mito"><p class="mv-s">Preenchimento labial sempre deixa os lábios exagerados.</p><p class="mv-e">Mito. O resultado depende do plano, da técnica e do que você conversa com a profissional. A naturalidade começa na avaliação, e não em uma regra pronta.</p></li><li data-a="mito"><p class="mv-s">O resultado de um procedimento é igual para todas as pessoas.</p><p class="mv-e">Mito. Pele, anatomia, hábitos e resposta do corpo mudam de pessoa para pessoa. Por isso os resultados e o tempo de evolução variam.</p></li><li data-a="verdade"><p class="mv-s">Os cuidados depois do procedimento fazem parte do tratamento.</p><p class="mv-e">Verdade. Seguir as orientações pós-procedimento ajuda na sua segurança e na evolução do tratamento. A Dra. Amanda explica tudo com clareza.</p></li></ol>
</div></section>


{SIM}

<section id="estrutura" class="deep"><div class="wrap">
<div class="sh rv"><div><div class="kicker">O consultório</div><h2>Um espaço pensado para o seu conforto.</h2></div><p>Av. dos Andradas, 3323, sala 901, em Santa Efigênia, Belo Horizonte.</p></div>
<div data-car class="gal rv">
{ctrl("Arraste para explorar",3,0)}
<div class="track">{gal}</div>
</div></div></section>

<section id="atendimento"><div class="wrap">
<div class="sh rv"><div><div class="kicker">Como é o atendimento</div><h2>O atendimento em 4 etapas.</h2></div><p>Veja o que acontece depois que você chama no WhatsApp.</p></div>
<div class="stack">
<div class="step" style="--i:0"><span class="n">01</span><div><h3>Primeiro contato</h3><p>Você chama no WhatsApp e escolhe um horário.</p></div></div>
<div class="step" style="--i:1"><span class="n">02</span><div><h3>Avaliação</h3><p>A Dra. Amanda ouve o que você quer e avalia o seu rosto.</p></div></div>
<div class="step" style="--i:2"><span class="n">03</span><div><h3>Planejamento</h3><p>Se houver indicação, ela explica as possibilidades para o seu caso, e você decide com informação.</p></div></div>
<div class="step" style="--i:3"><span class="n">04</span><div><h3>Acompanhamento</h3><p>Depois, orientações e retorno, se forem necessários.</p></div></div>
</div></div></section>

<section id="depoimentos" class="sand"><div class="wrap">
<div class="sh rv"><div><div class="kicker">Avaliações</div><h2>O que dizem as pacientes.</h2></div><p>Textos originais, publicados pelos próprios pacientes no perfil do Google do consultório.</p></div>
<div data-car class="rv">
{ctrl("Arraste para ler",len(REVS),0)}
<div class="track">{revcards}</div>
</div>
<p class="micro rv"><a class="link" href="https://www.google.com/maps/search/?api=1&query=Dra.+Amanda+Pereira+Est%C3%A9tica+Avan%C3%A7ada+Belo+Horizonte" target="_blank" rel="noopener">Ver todas as avaliações no Google</a></p>
</div></section>\n\n<section id="instagram"><div class="wrap">
<div class="sh rv"><div><div class="kicker">Instagram</div><h2>Acompanhe o dia a dia no Instagram.</h2></div><p>Bastidores, cuidados e novidades do consultório em @draamandapereira.</p></div>
<div class="actions rv" style="margin-top:var(--s3)"><a class="link" href="https://www.instagram.com/draamandapereira/" target="_blank" rel="noopener">Seguir @draamandapereira</a><button class="btn light" id="igpause" type="button" aria-pressed="false" hidden>Pausar fotos</button></div>
</div>
<div class="ig" id="ig" aria-label="Fotos do Instagram da Dra. Amanda"></div>
</section>

<section id="duvidas"><div class="wrap faq">
<div class="faq-h rv"><div class="kicker">Dúvidas</div><h2>O que costuma ser perguntado antes da avaliação.</h2>
<p class="faq-p">Respostas diretas sobre harmonização facial. Se a sua dúvida não estiver aqui, pergunte no WhatsApp.</p>
<div class="actions"><a class="btn" href="{WA}" target="_blank" rel="noopener">Tirar minha dúvida no WhatsApp</a></div></div>
<div class="rv">
<details open><summary>O que é a harmonização facial?</summary><p>É um conjunto de procedimentos que equilibra proporções e traços do rosto, planejado caso a caso. O objetivo não é mudar quem você é. Na avaliação, a Dra. Amanda indica só o que faz sentido para o seu rosto, e isso inclui dizer quando algo não é necessário.</p></details>
<details><summary>Preciso saber o que quero fazer?</summary><p>Não. Você chega com a queixa ou o que gostaria de melhorar, e a Dra. Amanda avalia o seu rosto e explica as possibilidades. Quem decide é você, com informação.</p></details>
<details><summary>Vou ficar com aparência artificial?</summary><p>O planejamento parte dos seus traços e das suas expressões, com a naturalidade como critério. O resultado varia de pessoa para pessoa e não existe garantia. Por isso a avaliação vem antes: você entende o que é esperado no seu caso antes de decidir.</p></details>
<details><summary>Dói?</summary><p>Depende do procedimento e da sensibilidade de cada pessoa, e algum desconforto pode acontecer. Na avaliação, ela explica o que esperar e o que pode ser feito para o seu conforto.</p></details>
<details><summary>Quanto tempo dura e quando vejo o resultado?</summary><p>O prazo varia conforme o procedimento indicado e o seu organismo. Ela explica o tempo esperado para o seu caso na avaliação, antes de qualquer procedimento.</p></details>
<details><summary>Existem riscos e quem não pode fazer?</summary><p>Todo procedimento estético tem riscos. Inchaço e manchas roxas, por exemplo, podem aparecer. Na avaliação, a Dra. Amanda pergunta sobre histórico de saúde, alergias, medicamentos, gestação e amamentação. Se o procedimento não for indicado para você, ela diz.</p></details>
<details><summary>E depois do procedimento?</summary><p>Você recebe as orientações de cuidado e, se for necessário, volta para um retorno. Em caso de dúvida no pós, é só chamar no WhatsApp.</p></details>
<details><summary>Quanto custa?</summary><p>O valor depende do que for indicado para você, por isso é informado depois da avaliação e antes de qualquer procedimento. Fazer a avaliação não obriga você a fazer nenhum tratamento. Para saber as condições, pergunte direto pelo WhatsApp.</p></details>
<details><summary>Como sei que posso confiar?</summary><p>A Dra. Amanda é biomédica esteta com registro no Conselho Regional de Biomedicina (CRBM 22528), número que você pode conferir. O consultório fica na Av. dos Andradas, 3323, sala 901, em Belo Horizonte. Você também pode ver o que pacientes escrevem <a href="https://www.google.com/maps/search/?api=1&query=Dra.+Amanda+Pereira+Est%C3%A9tica+Avan%C3%A7ada+Belo+Horizonte" target="_blank" rel="noopener">no perfil do Google</a>.</p></details>
</div></div></section>

<section class="final cta" id="agendar"><div class="wrap">
<h2>Vamos conversar sobre o seu rosto?</h2>
<p class="lead">Se ainda não sabe o que fazer, tudo bem: é para isso que serve a avaliação.</p>
<a class="btn gold" id="pickbtn" href="{WA}" target="_blank" rel="noopener">Agendar minha avaliação pelo WhatsApp</a>
<p class="micro">Você chama no WhatsApp, escolhe o horário e só decide depois da avaliação.</p>
</div></section>

<section id="contato"><div class="wrap">
<div class="sh rv"><div><div class="kicker">Localização</div><h2>Esperamos por você em Belo Horizonte.</h2></div><span></span></div>
<div class="ct rv" style="margin-top:var(--block)">
<div class="info" id="primeira">
<div class="kicker">Primeira consulta</div>
<dl><dt>Endereço</dt><dd>Av. dos Andradas, 3323, sala 901<br>Santa Efigênia, Belo Horizonte, MG, 31010-560</dd>
<dt>Horários</dt><dd>Segunda a sexta, 09h às 19h<br>Sábado, 09h às 16h30<br>Domingo, fechado</dd>
<dt>Telefone</dt><dd>(31) 99842-0605</dd></dl>
<div class="actions"><a class="btn" href="{WA}" target="_blank" rel="noopener">Agendar pelo WhatsApp</a><a class="link" href="{MAP}" target="_blank" rel="noopener">Como chegar</a></div>
</div>
<a class="map" href="{MAP}" target="_blank" rel="noopener" aria-label="Abrir o endereço no Google Maps"><span class="pin"></span><b>Av. dos Andradas, 3323</b><span>Abrir no Google Maps</span></a>
</div></div></section>
</main>

<footer><div class="wrap">
<div class="cols">
<div><b>Dra. Amanda Pereira</b><br>Biomédica · CRBM 22528<br>© 2026</div>
<div>Av. dos Andradas, 3323, sl 901<br>Santa Efigênia, Belo Horizonte, MG<br>(31) 99842-0605</div>
<div><a href="#privacidade">Política de privacidade</a><br><a href="https://www.instagram.com/draamandapereira/" target="_blank" rel="noopener">Instagram</a><br><a href="{WA}" target="_blank" rel="noopener">WhatsApp</a></div>
</div>
<div class="priv" id="privacidade"><h2>Política de privacidade</h2><p>Esta página não envia dados para nenhum servidor e não tem ferramentas de medição de visitas. O que você preenche no agendamento vira apenas o texto da mensagem do WhatsApp. Ao tocar em Agendar, você abre o WhatsApp e a conversa passa a seguir as regras do próprio WhatsApp. O consultório recebe só o que você escolher enviar na mensagem. As fontes de texto são carregadas do Google Fonts, que pode registrar o endereço de IP de quem visita. Dúvidas sobre seus dados: (31) 99842-0605.</p></div>
</div></footer>
<a class="wa" href="{WA}" target="_blank" rel="noopener" aria-label="Agendar pelo WhatsApp"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 5.5h16v11H10l-5 4v-4H4z"/><path d="M8.5 10.5h7M8.5 13h4"/></svg></a>
'''
js='''
<script>
document.documentElement.classList.add("js");
(function(){
var nav=document.getElementById("nav"),bar=document.getElementById("bar"),mb=document.getElementById("mbtn");
function sc(){var h=document.documentElement.scrollHeight-innerHeight;bar.style.setProperty("--p",h>0?Math.min(1,scrollY/h):0)}
sc();addEventListener("scroll",sc,{passive:true});
mb.addEventListener("click",function(){var o=nav.classList.toggle("open");mb.setAttribute("aria-expanded",o)});
[].forEach.call(document.querySelectorAll("#menu a"),function(a){a.addEventListener("click",function(){nav.classList.remove("open");mb.setAttribute("aria-expanded","false")})});
/* carrosséis */
[].forEach.call(document.querySelectorAll("[data-car]"),function(c){
var t=c.querySelector(".track"),cards=t.children,cnt=c.querySelector("[data-count]"),bs=c.querySelectorAll(".arr"),n=cards.length;
function pad(x){return(x<10?"0":"")+x}
function cur(){var w=cards[0].offsetWidth+parseFloat(getComputedStyle(t).columnGap||24),i=Math.round(t.scrollLeft/w);return Math.max(0,Math.min(n-1,i))}
function upd(){var i=cur();cnt.textContent=pad(i+1)+" / "+pad(n);bs[0].disabled=i===0;bs[1].disabled=t.scrollLeft+t.clientWidth>=t.scrollWidth-4}
[].forEach.call(bs,function(b){b.addEventListener("click",function(){var w=cards[0].offsetWidth+parseFloat(getComputedStyle(t).columnGap||24);t.scrollBy({left:w*parseInt(b.dataset.dir,10),behavior:"smooth"})})});
t.addEventListener("scroll",upd,{passive:true});upd()});
/* mensagem personalizada */
var OR="pelo site";try{if(new URLSearchParams(location.search).get("origem")==="instagram"){OR="do Instagram";[].forEach.call(document.querySelectorAll('a[href*="api.whatsapp.com"]'),function(a){a.href=a.href.replace("Vim%20do%20site","Vim%20do%20Instagram")})}}catch(e){}


/* simulador */
(function(){
var nome=document.getElementById("f-nome"),obs=document.getElementById("f-obs"),bub=document.getElementById("bubble"),btn=document.getElementById("simbtn");
if(!nome||!bub)return;
var st={proc:[],reg:[],per:""};
function lista(a){return a.length>1?a.slice(0,-1).join(", ")+" e "+a[a.length-1]:a[0]}
function msg(){
var n=nome.value.trim(),l=[];
l.push("Oi!"+(n?" Meu nome é "+n+" e":"")+" vim "+OR+".");
l.push("Gostaria de agendar uma avaliação de harmonização facial.");
if(st.proc.length)l.push("Quero fazer: "+lista(st.proc)+".");
if(st.reg.length)l.push("Região: "+lista(st.reg)+".");
if(st.per)l.push("Melhor período: "+st.per.toLowerCase()+".");
var o=obs.value.trim();if(o)l.push("Observações: "+o);
return l.join("\\n")}
function upd(){var m=msg();bub.textContent=m;btn.href="https://api.whatsapp.com/send/?phone=5531998420605&text="+encodeURIComponent(m)}
[].forEach.call(document.querySelectorAll("#sim .opts"),function(g){var k=g.getAttribute("data-grp");
[].forEach.call(g.querySelectorAll(".opt"),function(b){b.addEventListener("click",function(){
var t=b.textContent;
if(k==="per"){var on=b.getAttribute("aria-checked")==="true";[].forEach.call(g.querySelectorAll(".opt"),function(x){x.setAttribute("aria-checked","false")});
if(!on)b.setAttribute("aria-checked","true");st.per=on?"":t}
else{var i=st[k].indexOf(t);if(i>-1)st[k].splice(i,1);else st[k].push(t);b.setAttribute("aria-pressed",i<0)}
upd()})})});
nome.addEventListener("input",upd);obs.addEventListener("input",upd);upd();
window.__simOR=function(){upd()};
})();


/* comparador antes e depois */
(function(){
var reduce=matchMedia("(prefers-reduced-motion: reduce)").matches;
[].forEach.call(document.querySelectorAll(".cmp"),function(f){
var h=f.querySelector(".hd"),x=50,anim=0,done=false;
function set(v){x=Math.max(0,Math.min(100,v));f.style.setProperty("--x",x+"%");h.setAttribute("aria-valuenow",Math.round(x))}
function stop(){anim=0;done=true}
function fromEv(e){var r=f.getBoundingClientRect();set((e.clientX-r.left)/r.width*100)}
h.addEventListener("pointerdown",function(e){stop();h.setPointerCapture(e.pointerId);f.classList.add("dragging");e.preventDefault()});
h.addEventListener("pointermove",function(e){if(h.hasPointerCapture(e.pointerId))fromEv(e)});
h.addEventListener("pointerup",function(e){f.classList.remove("dragging");try{h.releasePointerCapture(e.pointerId)}catch(_){}});
h.addEventListener("keydown",function(e){var d={ArrowLeft:-5,ArrowRight:5,Home:-100,End:100}[e.key];if(d!==undefined){stop();set(e.key==="Home"?0:e.key==="End"?100:x+d);e.preventDefault()}});
if(reduce||!("IntersectionObserver" in window))return;
var io=new IntersectionObserver(function(es){es.forEach(function(en){if(!en.isIntersecting||done)return;io.unobserve(f);
var t0=null,id=++anim,pts=[50,88,12,50],dur=900;
function ease(t){return t<.5?2*t*t:1-Math.pow(-2*t+2,2)/2}
function step(ts){if(anim!==id)return;if(t0===null)t0=ts;var el=ts-t0,seg=Math.min(pts.length-2,Math.floor(el/dur)),t=Math.min(1,(el-seg*dur)/dur);
set(pts[seg]+(pts[seg+1]-pts[seg])*ease(t));if(el<dur*(pts.length-1))requestAnimationFrame(step);else done=true}
requestAnimationFrame(step)})},{threshold:.7});io.observe(f)});
})();

/* mito ou verdade */
(function(){
var sec=document.getElementById("mito-verdade");if(!sec)return;
var items=[].map.call(sec.querySelectorAll(".mv-list li"),function(li){return{s:li.querySelector(".mv-s").textContent,a:li.getAttribute("data-a"),e:li.querySelector(".mv-e").textContent}});
var N=items.length,game=sec.querySelector(".mv-game"),box=sec.querySelector(".mv-score"),q=sec.querySelector("[data-q]"),sc=sec.querySelector("[data-s]");
var i=0,hits=0,revealed=false,busy=false;
game.hidden=false;box.hidden=false;sec.classList.add("on");
game.innerHTML='<div class="mv-stage" tabindex="0" role="group" aria-label="Cartas de mito ou verdade. Use a seta para a esquerda para mito e a seta para a direita para verdade." aria-keyshortcuts="ArrowLeft ArrowRight"></div><div class="mv-actions"></div>';
var stage=game.querySelector(".mv-stage"),acts=game.querySelector(".mv-actions"),hint;
function esc(t){var d=document.createElement("div");d.textContent=t;return d.innerHTML}
function score(){q.textContent="Pergunta "+Math.min(i+1,N)+" de "+N;sc.textContent="Acertos: "+hits}
function hideHint(){if(hint)hint.classList.add("gone")}
function cardHTML(k){return '<div class="mv-card pos'+k+'" data-i="'+(i+k)+'"><div class="mv-flip"><div class="mv-face mv-front"><span class="mv-tag">Mito ou verdade?</span><p class="mv-st">'+esc(items[i+k].s)+'</p><span class="mv-stamp m">Mito</span><span class="mv-stamp v">Verdade</span></div><div class="mv-face mv-back"><span class="mv-tag"></span><h3 class="mv-res"></h3><p class="mv-ex"></p><p class="mv-fb"></p></div></div></div>'}
function render(){var h="";for(var k=Math.min(2,N-1-i);k>=0;k--)h+=cardHTML(k);
stage.innerHTML=h+'<div class="mv-hint">← arrasta pro lado →</div>';hint=stage.querySelector(".mv-hint");
if(i>0||hits>0)hideHint();
revealed=false;busy=false;score();buttons()}
function buttons(){
if(!revealed)acts.innerHTML='<button class="btn light" type="button" data-ans="mito">Mito</button><button class="btn" type="button" data-ans="verdade">Verdade</button>';
else acts.innerHTML='<button class="btn gold" type="button" data-next>'+(i>=N-1?"Ver resultado":"Próxima")+'</button>'}
function answer(ans){if(revealed||busy||i>=N)return;hideHint();
var it=items[i],ok=ans===it.a;if(ok)hits++;revealed=true;
var c=stage.querySelector(".mv-card.pos0");c.classList.remove("drag");c.style.transform="";
var t=c.querySelectorAll(".mv-stamp");[].forEach.call(t,function(x){x.style.opacity=0});
c.querySelector(".mv-back .mv-tag").textContent=ok?"Você acertou":"Quase";
c.querySelector(".mv-res").textContent=it.a==="mito"?"É mito.":"É verdade.";
c.querySelector(".mv-ex").textContent=it.e.replace(/^(Mito|Verdade)\.\s*/,"");
c.querySelector(".mv-fb").textContent=ok?"Boa! Sua resposta estava certa.":"Dessa vez não, mas agora você já sabe.";
c.classList.add("flipped");score();buttons()}
function next(){if(!revealed||busy)return;busy=true;var c=stage.querySelector(".mv-card.pos0");c.classList.add("out");
var go=function(){i++;if(i>=N)final();else render()};
if(matchMedia("(prefers-reduced-motion: reduce)").matches)go();else setTimeout(go,330)}
function final(){
var m="Oi! Vim "+OR+", fiz o Mito ou Verdade e acertei "+hits+" de "+N+". Gostaria de agendar uma avaliação de harmonização facial.";
stage.innerHTML='<div class="mv-final"><span class="mv-tag" style="position:static;color:#e8c9a8">Resultado</span><h3>Você acertou '+hits+' de '+N+'</h3><p>Quer conversar sobre o que é mito e o que é verdade no seu caso? A avaliação é para isso.</p><div class="mv-fa"><a class="btn gold" target="_blank" rel="noopener" href="https://api.whatsapp.com/send/?phone=5531998420605&text='+encodeURIComponent(m)+'">Agendar minha avaliação</a><button class="btn light" type="button" data-again>Jogar de novo</button></div></div>';
acts.innerHTML="";q.textContent="Pergunta "+N+" de "+N;sc.textContent="Acertos: "+hits;
var f=stage.querySelector(".mv-final h3");f.setAttribute("tabindex","-1");f.focus({preventScroll:true})}
function again(){i=0;hits=0;render()}
acts.addEventListener("click",function(e){var b=e.target.closest("button");if(!b)return;
if(b.hasAttribute("data-ans"))answer(b.getAttribute("data-ans"));else if(b.hasAttribute("data-next"))next()});
stage.addEventListener("click",function(e){if(e.target.closest("[data-again]"))again()});
stage.addEventListener("keydown",function(e){if(i>=N)return;
if(e.key==="ArrowLeft"){e.preventDefault();if(!revealed)answer("mito")}
else if(e.key==="ArrowRight"){e.preventDefault();if(!revealed)answer("verdade");else next()}
else if((e.key==="Enter"||e.key===" ")&&revealed){e.preventDefault();next()}});
/* arrastar: só movimento horizontal conta, toque rápido não */
var d=null;
stage.addEventListener("pointerdown",function(e){var c=e.target.closest(".mv-card.pos0");if(!c||revealed||busy)return;
d={c:c,x:e.clientX,y:e.clientY,dx:0,on:false,id:e.pointerId}});
stage.addEventListener("pointermove",function(e){if(!d||e.pointerId!==d.id)return;
var dx=e.clientX-d.x,dy=e.clientY-d.y;
if(!d.on){if(Math.abs(dx)<8||Math.abs(dx)<Math.abs(dy))return;d.on=true;hideHint();d.c.classList.add("drag");try{d.c.setPointerCapture(e.pointerId)}catch(_){}}
d.dx=dx;var th=Math.max(70,d.c.offsetWidth*.28);
d.c.style.transform="translateX("+dx+"px) rotate("+(dx/18)+"deg)";
var m=d.c.querySelector(".mv-stamp.m"),v=d.c.querySelector(".mv-stamp.v");
m.style.opacity=dx<0?Math.min(1,-dx/th):0;v.style.opacity=dx>0?Math.min(1,dx/th):0});
function end(e,cancel){if(!d||(e&&e.pointerId!==d.id))return;var c=d.c,dx=d.dx,on=d.on;d=null;if(!on)return;
c.classList.remove("drag");var th=Math.max(70,c.offsetWidth*.28);
if(!cancel&&Math.abs(dx)>=th){answer(dx<0?"mito":"verdade")}
else{c.style.transform="";[].forEach.call(c.querySelectorAll(".mv-stamp"),function(x){x.style.opacity=0})}}
stage.addEventListener("pointerup",function(e){end(e,false)});
stage.addEventListener("pointercancel",function(e){end(e,true)});
render();
})();

/* faixas do instagram */
(function(){
var ig=document.getElementById("ig"),pb=document.getElementById("igpause");if(!ig)return;
/* POSTS: [arquivo ou endereço da imagem, texto alternativo]. Sem arquivo, aparece um quadro reservado. */
var POSTS=[["","Publicação 1"],["","Publicação 2"],["","Publicação 3"],["","Publicação 4"],["","Publicação 5"],["","Publicação 6"],["","Publicação 7"],["","Publicação 8"]];
POSTS.forEach(function(p,i){p.n=i+1});
var URL="https://www.instagram.com/draamandapereira/";
function tile(p,n,dup){var a=document.createElement("a");a.className="ig-t";a.href=URL;a.target="_blank";a.rel="noopener";
if(dup){a.setAttribute("aria-hidden","true");a.tabIndex=-1}else a.setAttribute("aria-label",p[1]+" no Instagram");
if(p[0]){var im=document.createElement("img");im.src=p[0];im.alt=dup?"":p[1];im.loading="lazy";im.draggable=false;a.appendChild(im)}
else{var d=document.createElement("span");d.className="ph";d.textContent=(n<10?"0":"")+n;a.appendChild(d)}return a}
function row(list,rev){var r=document.createElement("div");r.className="ig-row"+(rev?" rev":"");var t=document.createElement("div");t.className="ig-track";
list.forEach(function(p){t.appendChild(tile(p,p.n,false))});list.forEach(function(p){t.appendChild(tile(p,p.n,true))});r.appendChild(t);return r}
ig.appendChild(row(POSTS,false));ig.appendChild(row(POSTS.slice().reverse(),true));
pb.hidden=false;pb.addEventListener("click",function(){var on=ig.classList.toggle("paused");pb.setAttribute("aria-pressed",on);pb.textContent=on?"Retomar fotos":"Pausar fotos"});
})();
/* ramo que percorre o site */
(function(){try{
var main=document.getElementById("conteudo");if(!main||!main.getBoundingClientRect)return;
var NS="http://www.w3.org/2000/svg",RM=window.matchMedia&&matchMedia("(prefers-reduced-motion: reduce)").matches;
var svg=null,live,back,tip,leaves,L=0,S=[],pts=[],N=0,idx0=-1,done=false,lastW=0,lastH=0,raf=0,card=document.getElementById("primeira");
var CL="#efd9bd",BD="#6e2a37";
function el(n,a,p){var e=document.createElementNS(NS,n);for(var k in a)e.setAttribute(k,a[k]);if(p)p.appendChild(e);return e}
function mob(){return innerWidth<=760}
function at(y){for(var q=0;q<=N;q++)if(pts[q][1]>=y)return q;return N}

function build(){
var mr=main.getBoundingClientRect(),W=Math.round(mr.width),H=Math.round(main.offsetHeight),M=mob();
if(svg)svg.remove();
svg=el("svg",{"class":"ramo","aria-hidden":"true",focusable:"false",width:W,height:H,viewBox:"0 0 "+W+" "+H});
main.insertBefore(svg,main.firstChild);
function rel(e){var r=e.getBoundingClientRect();return{t:r.top-mr.top,b:r.bottom-mr.top,l:r.left-mr.left,w:r.width,h:r.height}}
var secs=[].slice.call(main.querySelectorAll(":scope>header,:scope>section")).map(function(s){var r=rel(s);r.dark=s.classList.contains("hero")||s.classList.contains("final");return r});
S=secs;
var gut=Math.max(22,(W-1120)/4),LX=M?W*.1:gut,RX=M?W*.9:W-gut;
var btn=document.getElementById("mag"),P=[];
if(btn){var b=rel(btn);P.push([b.l+b.w/2,b.b+18])}else P.push([W*.3,secs[0].b*.7]);
var side=1; // 1 = direita
function X(s){return s>0?RX:LX}
var hero=secs[0];
if(M){P.push([RX,hero.b-hero.h*.08])}else P.push([RX,hero.b-hero.h*.1]);
var ci=card?rel(card):null,end=null;
for(var i=1;i<secs.length;i++){var s=secs[i],h=s.h,last=i===secs.length-1;
 if(M){var n=Math.max(2,Math.round(h/520));
  for(var k=0;k<n;k++){side=-side;var f=.1+(.8*k/(n-1));P.push([X(side),s.t+h*f])}
  if(last&&ci){P.pop();P.push([W/2,ci.t-8]);end=1}
 }else{
  side=(i%2)?-1:1; // alterna
  if(last&&ci){P.push([LX,s.t+h*.12]);P.push([ci.l-2,ci.t+ci.h*.32]);end=1}
  else{P.push([X(side),s.t+h*.2]);P.push([X(side),s.t+h*.68]);P.push([W/2,s.b])}
 }
}
// catmull-rom -> bezier
var d="M"+P[0][0].toFixed(1)+" "+P[0][1].toFixed(1);
for(var j=0;j<P.length-1;j++){var p0=P[j-1]||P[j],p1=P[j],p2=P[j+1],p3=P[j+2]||p2;
 d+="C"+(p1[0]+(p2[0]-p0[0])/6).toFixed(1)+" "+(p1[1]+(p2[1]-p0[1])/6).toFixed(1)+" "+(p2[0]-(p3[0]-p1[0])/6).toFixed(1)+" "+(p2[1]-(p3[1]-p1[1])/6).toFixed(1)+" "+p2[0].toFixed(1)+" "+p2[1].toFixed(1)}
// gradiente por seção
var defs=el("defs",{},svg),g=el("linearGradient",{id:"rg",gradientUnits:"userSpaceOnUse",x1:0,y1:0,x2:0,y2:H},defs);
function st(o,c){el("stop",{offset:Math.max(0,Math.min(1,o/H)).toFixed(4),"stop-color":c},g)}
secs.forEach(function(s){var c=s.dark?CL:BD;st(s.t+s.h*.1,c);st(s.b-s.h*.1,c)});
back=el("path",{d:d,"class":"rb",fill:"none",stroke:"url(#rg)","stroke-width":2,"stroke-linecap":"round","stroke-dasharray":"2 7",opacity:.2},svg);
live=el("path",{d:d,"class":"rl",fill:"none",stroke:"url(#rg)","stroke-width":M?2:2.4,"stroke-linecap":"round"},svg);
L=live.getTotalLength();live.style.strokeDasharray=L;
N=Math.ceil(L/5);pts=[];for(var q=0;q<=N;q++){var pp=live.getPointAtLength(Math.min(L,q*L/N));pts.push([pp.x,pp.y])}
function colorAt(y){for(var q=secs.length-1;q>=0;q--)if(y>=secs[q].t)return secs[q].dark?CL:BD;return CL}
// folhinhas
leaves=[];var sz=M?15:20,flip=1;
function leaf(q){q=Math.max(1,Math.min(N-1,q));var a=pts[q-1],b=pts[q+1],ang=Math.atan2(b[1]-a[1],b[0]-a[0])*180/Math.PI;flip=-flip;
 var gp=el("g",{transform:"translate("+pts[q][0].toFixed(1)+" "+pts[q][1].toFixed(1)+") rotate("+(ang+flip*52).toFixed(1)+") scale("+(sz/22)+")","class":"lf"},svg);
 el("path",{d:"M0 0C5-9 15-10 22 0C15 8 5 9 0 0Z",fill:colorAt(pts[q][1]),opacity:.85},gp);
 el("path",{d:"M2 0H17",stroke:"#fff",opacity:.35,"stroke-width":.8,fill:"none"},gp);
 leaves.push({q:q,el:gp})}
secs.forEach(function(s,i){if(i>0)leaf(at(s.t+8));if(i>0&&i<secs.length-1)leaf(at(s.t+s.h*.5))});
tip=el("circle",{"class":"tip",r:5.5,cx:pts[0][0],cy:pts[0][1],fill:"#fff7ea",stroke:"url(#rg)","stroke-width":1.6},svg);
if(RM)tip.style.display="none";
lastW=W;lastH=H;idx0=-1;update(true)}
function update(first){
if(!svg)return;
var mr=main.getBoundingClientRect(),ay=-mr.top+innerHeight*.58;
var q=RM?N:at(ay);if(ay<pts[0][1])q=0;
var cur=L*q/N;live.style.strokeDashoffset=RM?0:(L-cur);
leaves.forEach(function(l){l.el.classList.toggle("on",RM||l.q<=q)});
if(!RM){tip.style.opacity=q<=0?0:1;tip.setAttribute("cx",pts[q][0]);tip.setAttribute("cy",pts[q][1]);
 var idx=-1;for(var i=0;i<S.length;i++)if(pts[q][1]>=S[i].t)idx=i;
 if(idx0>=0&&idx!==idx0&&q>0){var w=el("circle",{"class":"wv",cx:pts[q][0],cy:pts[q][1],r:5,fill:"none",stroke:"url(#rg)","stroke-width":2},svg);w.addEventListener("animationend",function(){w.remove()})}
 idx0=idx}
var fin=q>=N-1;
if(card){if(fin&&!done){done=true;card.classList.add("lit","pulse");setTimeout(function(){card.classList.remove("pulse")},1800)}else if(!fin&&done){done=false;card.classList.remove("lit")}}}
function onS(){if(raf)return;raf=requestAnimationFrame(function(){raf=0;update()})}
var tm=0;function re(){clearTimeout(tm);tm=setTimeout(function(){var W=Math.round(main.getBoundingClientRect().width),H=main.offsetHeight;if(W!==lastW||Math.abs(H-lastH)>2)build()},180)}
addEventListener("scroll",onS,{passive:true});addEventListener("resize",re);addEventListener("load",re);
if(window.ResizeObserver)new ResizeObserver(re).observe(main);
build();
}catch(e){}})();
/* botão flutuante some perto do convite final e do rodapé */
try{var wa=document.querySelector(".wa"),seen={};var io=new IntersectionObserver(function(es){es.forEach(function(e){seen[e.target.id||e.target.tagName]=e.isIntersecting});wa.classList.toggle("off",Object.keys(seen).some(function(k){return seen[k]}))},{threshold:.15});
[].forEach.call(document.querySelectorAll("#agendar,footer"),function(x){io.observe(x)})}catch(e){}
/* entrada suave */
try{var rv=document.querySelectorAll(".rv");if("IntersectionObserver" in window){var o=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add("in");o.unobserve(e.target)}})},{threshold:.12});[].forEach.call(rv,function(x){o.observe(x)})}else{[].forEach.call(rv,function(x){x.classList.add("in")})}}catch(e){[].forEach.call(document.querySelectorAll(".rv"),function(x){x.classList.add("in")})}
})();
</script>
</body>
</html>
<!-- estelar v1 -->
'''
open('/mnt/user-data/outputs/amanda-pereira-estelar.html','w',encoding='utf-8').write(html+js)
print(len(html+js))
