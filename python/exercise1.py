'''
Created on 22/mar/2014

@author: khorda
'''
from pyplasm import *
def floors():
    
    def mkcolonna(r=0.05):
        def mkcolonnaX(dx):
            def mkcolonnaY(dy):
                c = CIRCUMFERENCE(r)(16)
                cj = JOIN(c)
                trans = T([1,2])([dx,dy])(cj)
                return COLOR(BLACK)(trans)
            return mkcolonnaY
        return mkcolonnaX
    
    colonneX_1 = [mkcolonna()(0.05)(0.5), mkcolonna()(2.05)(0.5), mkcolonna()(4.05)(0.5), mkcolonna()(6.05)(0.5), mkcolonna()(8.05)(0.5)]
    
    colonneY_sin = [mkcolonna()(0.05)(0.5), mkcolonna()(0.05)(2.5), mkcolonna()(0.05)(4.5), mkcolonna()(0.05)(6.5), mkcolonna()(0.05)(8.5)]
    
    colonneY_des = [mkcolonna()(8.05)(0.5), mkcolonna()(8.05)(2.5), mkcolonna()(8.05)(4.5), mkcolonna()(8.05)(6.5), mkcolonna()(8.05)(8.5)]
    
    colonneX_2 = [mkcolonna()(1.9)(2.3), mkcolonna()(6.25)(2.3)]
    
    colonne = colonneX_1+colonneY_sin+colonneY_des+colonneX_2
    
    col2D = []
    
    for col in colonne:
        col2D.append(PROD([col,QUOTE([3])]))
    
    perimetroSUD = [QUOTE([0.01,-0.01]*(400+10))]
    
    perimetroOVEST = [R([1,2])(PI/2)(QUOTE([0.01,-0.01]*(400+50+10)))]
    
    perimetroNORD = [T(2)(9+0.15)(QUOTE([0.01,-0.01]*(400+10)))]
    
    perimetroEST = [T(1)(8+0.15)(R([1,2])(PI/2)(QUOTE([0.01,-0.01]*(400+50+10))))]
    
    perimetro = perimetroSUD+perimetroOVEST+perimetroNORD+perimetroEST
    
    def mkhalfcirc(r):
        def mkhalfcirc1(p):
            return [r*COS(p[0]),r*SIN(p[0])]
        def mkdomain(dens=16):
            return INTERVALS(PI)(dens)
        return MAP(mkhalfcirc1)(mkdomain())
    
    
    halfcirc = JOIN([R([1,2])(PI)(mkhalfcirc(2.6))])
    
    pos_halfcirc = T([1,2])([4.1,4.3])(halfcirc)
    
    base = T([1,2])([1.1,4.3])(PROD([QUOTE([6]),QUOTE([4])]))
    
    main = [pos_halfcirc]+[base]
    
    st1 = COLOR(RED)(MKPOL([[[1.1,4.3],[2.8,4.3],[1.1,5.94],[2.8,5.94]],[[1,2,3,4]],None]))
    st1_scaled = T([1,2])([0.1,0.1])(SCALE([1,2])([0.9])(st1))
    st1_diff = DIFFERENCE([st1,st1_scaled])
    st2 = COLOR(GREEN)(MKPOL([[[1.1,5.94],[2.8,5.94],[1.1,7.57],[2.8,7.57]],[[1,2,3,4]],None]))
    st3 = COLOR(BLUE)(MKPOL([[[1.1,8],[3.2,8],[1.1,7.57],[3.2,7.57]],[[1,2,3,4]],None]))
    st4 = COLOR(YELLOW)(MKPOL([[[3.2,7.57],[3.2,8],[7.1,8],[7.1,7.57]],[[1,2,3,4]],None]))
    st5 = COLOR(PURPLE)(MKPOL([[[3.2,3.3],[4.5,3.3],[4.57,7.57],[3.2,7.57]],[[1,2,3,4]],None]))
    st6 = COLOR(ORANGE)(MKPOL([[[7.1,3.5],[4.5,3.3],[4.57,7.57],[7.1,7.5],[6.8,4.3]],[[1,2,3,4,5]],None]))
    
    stanze = [st1,st2,st3,st4,st5,st6]
    stanze_up = []
    for i in stanze:
        stanze_up.append(T(3)(0.01)(i))
        
    
    '''
    scal1 = PROD([QUOTE([0.8]),QUOTE([0.8])])
    scal2 = T([1,2])([2,1])(R([1,2])(3*PI/2)(mkhalfcirc(0.4)))
    scale = T([1,2])([1.2,3.2])(JOIN([scal1,scal2]))
    '''
    
    floor0 = col2D+perimetro+main+stanze_up
    
    base2 = MKPOL([[[0,0,-0.01],[8,0,-0.01],[8,7.5,-0.01],[0,7.5,-0.01]],[[1,2,3,4]],None])
    st2_1 = COLOR(RED)(MKPOL([[[0,0],[0,2.7],[2.7,2.7],[2.7,0]],[[1,2,3,4]],None]))
    st2_2 = COLOR(GREEN)(MKPOL([[[8,2.7],[8,0],[2.7,2.7],[2.7,0]],[[1,2,3,4]],None]))
    st2_3 = COLOR(BLUE)(MKPOL([[[0,2.7],[1.4,2.7],[0,7.5],[1.4,7.5]],[[1,2,3,4]],None]))
    st2_4 = COLOR(YELLOW)(MKPOL([[[5.3,7.5],[8,7.5],[5.3,6],[8,6]],[[1,2,3,4]],None]))
    st2_5 = COLOR(PURPLE)(MKPOL([[[5.3,7],[3.35,7],[3.35,3.5],[5.3,3.5]],[[1,2,3,4]],None]))
    
    f1 = [base2,st2_1,st2_2,st2_3,st2_4,st2_5]
    
    
    floor1 = []     
    
    for i in f1:
        floor1.append(T([1,2,3])([0.05,0.5,3])(i))
    
    
    base3 = DIFFERENCE([MKPOL([[[0,0],[8,0],[8,8],[0,8]],[[1,2,3,4]],None]),MKPOL([[[3.35,6],[3.35,3.5],[8,3.5],[8,6]],[[1,2,3,4]],None])])
    roof = [T(2)(0.5)(T(3)([6])(base3))]

#VIEW(STRUCT(floor0+floor1+floor2))


    return floor0+floor1+roof
