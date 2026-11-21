# usage: python3 brand_bar.py <in.png> <out.jpg> "<HEADLINE>"
import sys,os,urllib.request
from PIL import Image,ImageDraw,ImageFont
src,out,h=sys.argv[1],sys.argv[2],sys.argv[3].upper()
def font(name,size):
    for d in ['/usr/local/share/fonts/asi-document/','/tmp/']:
        if os.path.exists(d+name): return ImageFont.truetype(d+name,size)
    urllib.request.urlretrieve('https://github.com/JulietaUla/Montserrat/raw/master/fonts/ttf/'+name,'/tmp/'+name)
    return ImageFont.truetype('/tmp/'+name,size)
im=Image.open(src).convert('RGB').resize((1600,900),Image.LANCZOS)
ov=Image.new('RGBA',im.size,(0,0,0,0));d=ImageDraw.Draw(ov)
for y in range(160): d.line([(0,740+y),(1600,740+y)],fill=(0,0,0,int(240*(y/160)**0.7)))
im=Image.alpha_composite(im.convert('RGBA'),ov);d=ImageDraw.Draw(im)
sz=58;fh=font('Montserrat-ExtraBold.ttf',sz)
while d.textlength(h,font=fh)>1500: sz-=2;fh=font('Montserrat-ExtraBold.ttf',sz)
w=d.textlength(h,font=fh);d.text(((1600-w)/2,786),h,font=fh,fill=(255,214,92),stroke_width=3,stroke_fill=(0,0,0))
fs=font('Montserrat-Bold.ttf',27);s='VIP SWIPE PASS  •  FREE-PLAY BLACKJACK & SLOTS  •  LIVE CHAT  •  21+  •  CHATTIMENOW.COM'
w=d.textlength(s,font=fs);d.text(((1600-w)/2,856),s,font=fs,fill='white',stroke_width=2,stroke_fill=(0,0,0))
im.convert('RGB').save(out,quality=92)
