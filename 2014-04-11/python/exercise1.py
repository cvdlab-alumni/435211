'''
Created on 11/apr/2014

@author: khorda
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
dom1 = STRUCT(MKPOLS((V_F0,EV_F0)))
domCircle = STRUCT(MKPOLS((Vcircle,EVcircle)))

domFullOut = STRUCT([dom1,domCircle])
domFullIn = STRUCT([S([1,2])([0.95,0.95])(domFullOut)])
domFull = STRUCT([domFullOut,domFullIn])
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

V_S7 = []
EV_S7 = V2E(V_S7)

V_S8 = []
EV_S8 = V2E(V_S8)

V_Ramp = [[42,64],[42,84],[51,84],[51,38],[48,38],[48,79],[47,79],[47,64]]
EV_Ramp = V2E(V_Ramp)
del EV_Ramp[3]

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

composizione = larCompone([[Vcircle,EVcircle],[V_S1,EV_S1],[V_S2,EV_S2],[V_S3,EV_S3],[V_S4,EV_S4],[V_S5,EV_S5],[V_S6,EV_S6],[V_S7,EV_S8],[V_S8,EV_S8],[V_Ramp,EV_Ramp],[V_F0,EV_F0]])

    
