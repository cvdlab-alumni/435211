'''
Created on 12/apr/2014

@author: khorda
'''

from larcc import *
from exercise1 import *
from exercise2 import *

def mkRoad(lunghezza=5):
     #V_Base = [[0,0], [9,0],[9,6],[6,6],[6,7],[9,7],[9,13],[0,13],[0,7],[3,7],[3,6],[0,6],[0,0]]
     #E_Base = [[i for i in range(0,len(V_Base))]]
     b = STRUCT(MKPOLS(([[0,0],[9,0],[9,13],[0,13]],[[0,1,2,3]])))
     s_s = STRUCT(MKPOLS(([[0,6],[3,6],[3,7],[0,7]],[[0,1,2,3]])))
     s_d = STRUCT(MKPOLS(([[9,6],[6,6],[6,7],[9,7]],[[0,1,2,3]])))
     base = DIFFERENCE([b,s_s,s_d])
     return STRUCT([T(1)(9*i)(base) for i in range(0,lunghezza+1)])

def mkCross():
     b = STRUCT(MKPOLS(([[3,0],[3,3],[0,3],[0,16],[3,16],[3,19],[16,19],[16,16],[19,16],[19,3],[16,3],[16,0]],[[0,1,2,3,4,5,6,7,8,9,10,11]])))
     s_l = STRUCT(MKPOLS(([[0,9],[3,9],[3,10],[0,10]],[[0,1,2,3]])))
     s_r = STRUCT(MKPOLS(([[19,9],[16,9],[16,10],[19,10]],[[0,1,2,3]])))
     s_u = STRUCT(MKPOLS(([[9,19],[9,16],[10,16],[10,19]],[[0,1,2,3]])))
     s_d = STRUCT(MKPOLS(([[9,0],[9,3],[10,3],[10,0]],[[0,1,2,3]])))
     return T(2)(-3)(DIFFERENCE([b,s_l,s_r,s_u,s_d]))
 
def mkHouse():
    verts = [[0,0],[4,0],[4,4],[2,6],[0,4]]
    wall = PROD([JOIN(AA(MK)(verts)), Q(4)])
    door = T(1)(1.5)(CUBOID([1,3]))
    window = T([1,2])([2.75,1.5])(CUBOID([1,1.5]))
    Home = STRUCT([ COLOR(GRAY)(wall) , COLOR(BROWN)(door), COLOR(BLUE)(window) ])
    return R([2,3])(PI/2)(Home)

def vicinato():
    strada1 = mkRoad()
    strada2 = T([1,2])([45+16,16])(R([1,2])(PI/2)(mkRoad()))
    incrocio = T(1)(45)(mkCross())
    s_par1 = STRUCT([strada1,strada2,incrocio])
    
    s_par2 = T(1)(-(45+19))(s_par1)
    
    s_par3 = T(2)(45+19)(STRUCT([s_par1,s_par2]))
    complesso_stradale = STRUCT([s_par1,s_par2,s_par3])
    
    n_house = mkHouse()
    neighborhood = STRUCT(NN(4)([n_house,T(1)(5)]))
    
    neighborhood=S([1,2,3])([2.5,2.5,2.5])(T([1,2])([-7,7])(R([1,2])(PI)(neighborhood)))
    
    villa = T([1,2])([3,13])(S([1,2,3])([5,5,5])(STRUCT(walls()+floors())))
    
    tot = STRUCT([neighborhood,complesso_stradale,villa])
    return tot

#VIEW(STRUCT([villa,neighborhood,complesso_stradale]))


