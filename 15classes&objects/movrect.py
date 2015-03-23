class Rectangle(object):
    """it is a rectangle..."""
def current_rect(c,y,z):
    b=Rectangle()
    
    b.l=y.leng+c.cor
    b.w=z.wid+c.cor1
    print "current co-ordinates of rectangle is\n (",c.cor,',',c.cor1,')(',b.l,',',c.cor1,')(',b.l,',',b.w,')(',c.cor,',',b.w,')'
    return b

def movrect(current_rect,g,dx,dy):
    g.cor+=dx.lenx
    g.cor1+=dy.widx
    current_rect.l+=dx.lenx
    current_rect.w+=dy.widx
    print 'after moving rectangle\n (',g.cor,',',g.cor1,')(',current_rect.l,',',g.cor1,')(',current_rect.l,',',current_rect.w,')(',g.cor,',',current_rect.w,')'



def main():
    p=Rectangle()
    q=Rectangle()
    r=Rectangle()
    p.cor=float(raw_input("enter the corner co-ordinates\n"))
    p.cor1=float(raw_input())
    q.leng=float(raw_input("enter the length of rectangle\n"))
    r.wid=float(raw_input("enter the width of rectangle\n"))
    s=current_rect(p,q,r)
    q.lenx=float(raw_input("enter x extension\n"))
    r.widx=float(raw_input("enter y extension\n"))
    movrect(s,p,q,r)
main()
     
