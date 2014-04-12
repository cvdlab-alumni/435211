'''
Created on 12/apr/2014

@author: khorda
'''
from larcc import *
from exercise1 import *
from exercise2 import *
from exercise3 import *

def mkTree():
    foglie = COLOR(GREEN)(STRUCT([JOIN([STRUCT(MKPOLS(larCircle(5)())),MK([0,0,7])])]))
    tronco = COLOR(BROWN)(STRUCT(MKPOLS((larRod([1,5])()))))
    return STRUCT([T(3)(5)(foglie),tronco])

r_trees = STRUCT(NN(4)([mkTree(),T(1)(9)]))
square_trees = T([1,2])([-55,37])(STRUCT(NN(3)([r_trees,T(2)(9)])))

    
VIEW(STRUCT([square_trees,vicinato()]))