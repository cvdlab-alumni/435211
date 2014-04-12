'''
Created on 11/apr/2014

@author: khorda
'''
'''
#from larcc import *
# contorno piano terra
V_F0 = [[15,52],[15,96],[19,96],[19,101],[73,101],[73,96],[77,96],[77,52]]
EV_F0 = [[0,1],[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]

# funzione larCircle modificata per soddisfare le esigenze del progetto
def larHalfCircle(radius):
    def larHalfCircle0(shape=36):
        domain = larIntervals([shape])([-PI])
        V,CV = domain
        x = lambda coords : [radius*COS(p[0]) for p in V]
        y = lambda coords : [radius*SIN(p[0]) for p in V]
        return larMap([x,y])(domain)
    return larHalfCircle0

Vcircle, EVcircle = larHalfCircle(31)()

#forma la porta nel semicerchio 
for i in range(0,5):
    del EVcircle[16]
EVcircle.append([16,21])

#traslo il semicerchio verso la struttura del perimetro
Vcircle = translatePoints(Vcircle,[46,52,0])

'''
'''
dom1 = STRUCT(MKPOLS((V_F0,EV_F0)))
domCircle = STRUCT(MKPOLS((Vcircle,EVcircle)))

domFullOut = STRUCT([dom1,domCircle])
domFullIn = STRUCT([S([1,2])([0.95,0.95])(domFullOut)])
domFull = STRUCT([domFullOut,domFullIn])
'''
'''
def V2E(vertici):
    ret = []
    for i in range(0,len(vertici)):
        if((i+1)==len(vertici)):
            ret.append([i,0])
        else:
            ret.append([i,i+1])
    return ret

V_S1 = [[16,95],[23,95],[23,92],[23,88],[23,85],[16,85]]
EV_S1 = V2E(V_S1)

V_S2 = [[20,100],[41,100],[41,85],[36,85],[36,88],[35,88],[35,85],[24,85],[24,88],[23,88],[23,92],[24,92],[24,96],[20,96]]
EV_S2 = V2E(V_S2)

V_S3 = [[16,75],[16,84],[35,84],[35,75]]
EV_S3 = V2E(V_S3)

V_S4 = [[16,74],[16,61],[24,61],[24,56],[35,56],[35,74]]
EV_S4 = V2E(V_S4)

V_S5 = [[52,84],[58,84],[76,71],[76,52],[66,30],[56,38],[52,38]]
EV_S5 = V2E(V_S5)

V_S6 = [[42,100],[72,100],[72,95],[68,95],[68,88],[76,88],[76,72],[58,85],[42,85]]
EV_S6 = V2E(V_S6)

V_S7 = []#[[67,94],[76,95],[76,87],[69,90],[69,89],[67,89]]
EV_S7 = V2E(V_S7)

V_S8 = [[39,22],[16,55],[36,55],[36,84],[41,84],[41,63],[47,63],[47,37],[56,37],[66,29],[52,22]]
EV_S8 = V2E(V_S8)

V_Ramp = [[42,64],[42,84],[51,84],[51,38],[48,38],[48,79],[47,79],[47,64]]
EV_Ramp = V2E(V_Ramp)
# del EV_Ramp[3]

# compone le singole istanze di Vertici e Spigoli in una sola istanza complessiva
def larCompone(elements):
    V = []
    E = []
    for e in elements:
        X = e[0]
        Y = e[1]
        X = [[i[0],i[1]] for i in X]
        Y = [[k[0]+len(V),k[1]+len(V)] for k in Y]
        E = E + Y
        V = V + X
    return (V,E)


def E2F(edges):
    indexes = set()
    for e in edges:
        for i in e:
            indexes.add(i)
    return [sorted([k for k in indexes])]


composizioneStanze = larCompone([[V_S1,EV_S1],[V_S2,EV_S2],[V_S3,EV_S3],[V_S4,EV_S4],[V_S5,EV_S5],[V_S6,EV_S6],[V_S7,EV_S8],[V_S8,EV_S8],[V_Ramp,EV_Ramp]])
composizionePerimetro = larCompone([[Vcircle,EVcircle],[V_F0,EV_F0]])
stanze = [[V_S1,EV_S1],[V_S2,EV_S2],[V_S3,EV_S3],[V_S4,EV_S4],[V_S5,EV_S5],[V_S6,EV_S6],[V_S8,EV_S8],[V_Ramp,EV_Ramp]]
stanze2D = [STRUCT(MKPOLS((i[0],E2F(i[1])))) for i in stanze]

stanzePlasm = STRUCT(MKPOLS(composizioneStanze))
perimetroPlasm = STRUCT(MKPOLS(composizionePerimetro))
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




    return floor0+floor1+roof

#VIEW(STRUCT(floors()))
