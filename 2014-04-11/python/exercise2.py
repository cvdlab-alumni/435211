'''
Created on 12/apr/2014

@author: khorda
'''

from pyplasm import *

def mkhalfcirc(r):
    def mkhalfcirc1(p):
        return [r*COS(p[0]),r*SIN(p[0])]
    def mkdomain(dens=16):
        return INTERVALS(PI)(dens)
    return MAP(mkhalfcirc1)(mkdomain())

def walls():


    
    sc1 = PROD([mkhalfcirc(3),QUOTE([3])])
    sc = R([1,2])(PI)(sc1)
    pol = T(1)(1)(CUBOID([1,1,3]))
    scdiff = DIFFERENCE([sc,pol])
    s1 = T(2)(-0.1)(T([1,2])([4.1,4.8])(sc))
    
    muro_f2_sud = PROD([QUOTE([8]),QUOTE([3])])
    hollows_sud = PROD([QUOTE([0.52,-0.01]*15),QUOTE([1])])
    t_hollows_sud = T([1,2])([0.01,1])(hollows_sud)
    s2 = T(2)(0.5)(R([2,3])(PI/2)(DIFFERENCE([muro_f2_sud,t_hollows_sud])))
    
    
    sud = [s1, T(3)(3)(s2)]
    
    
    muro_f1_ovest = PROD([QUOTE([3.5]),QUOTE([3])])
    hollows_f1_o = PROD([QUOTE([1,-0.3]*2),QUOTE([1])])
    t_hollows_f1_o = T([1,2])([0.9,1])(hollows_f1_o)
    o1 = T(2)(-0.1)(T([1,2])([1.1,4.8])(R([1,2])(PI/2)(R([2,3])(PI/2)(DIFFERENCE([muro_f1_ovest,t_hollows_f1_o])))))
    
    
    muro_f2_ovest = PROD([QUOTE([8]),QUOTE([3])])
    hollows_f2_o = PROD([QUOTE([0.45,-0.01]*4),QUOTE([0.7])])
    t1_hollows_o = T([1,2])([0.01,1])(hollows_f2_o)
    t2_hollows_o = T([1,2])([2.1,1])(hollows_f2_o)
    t3_hollows_o = T([1,2])([6.1,1])(hollows_f2_o)
    o2_1 = DIFFERENCE([muro_f2_ovest,t1_hollows_o])
    o2_2 = DIFFERENCE([o2_1,t2_hollows_o])
    o2 = T(2)(0.5)(R([1,2])(PI/2)(R([2,3])(-PI/2)(R([1,2])(PI)(DIFFERENCE([o2_2,t3_hollows_o])))))
    
    
    ovest = [o1,T([1,2,3])([0,8,3])(o2)]
    
    
    muro_f1_nord = PROD([QUOTE([6]),QUOTE([3])])
    hollow_f1_n = PROD([QUOTE([0.6,-0.02]*7),QUOTE([0.15,-0.01]*10)])
    n1 = T(2)(-0.1)(T([1,2])([7.1,8.3])(R([2,3])(PI/2)(R([1,3])(PI)(DIFFERENCE([muro_f1_nord,T([1,2])([0.8,1])(hollow_f1_n)])))))
    
    muro_f2_nord = PROD([QUOTE([8]),QUOTE([3])])
    hollows_nord = PROD([QUOTE([0.52,-0.01]*15),QUOTE([1])])
    t_hollows_nord = T([1,2])([0.01,1])(hollows_nord)
    n2 = T(2)(0.5)(T([1,2,3])([8,8,3])(R([2,3])(PI/2)(R([1,3])(PI)(DIFFERENCE([muro_f2_nord,t_hollows_nord])))))
    
    nord = [n1,n2]
    
    muro_f1_est = PROD([QUOTE([3.5]),QUOTE([3])])
    hollows_f1_e = PROD([QUOTE([1,-0.3]*2),QUOTE([1])])
    t_hollows_f1_e = T([1,2])([0.9,1])(hollows_f1_e)
    e1 = T(2)(-0.1)(T([1,2])([7.1,4.8])(R([1,2])(PI/2)(R([2,3])(PI/2)(DIFFERENCE([muro_f1_est,t_hollows_f1_e])))))
    
    
    muro_f2_est = PROD([QUOTE([8]),QUOTE([3])])
    hollows_f2_e = PROD([QUOTE([0.45,-0.01]*4),QUOTE([0.7])])
    t1_hollows_e = T([1,2])([0.01,1])(hollows_f2_e)
    t2_hollows_e = T([1,2])([2.1,1])(hollows_f2_e)
    t3_hollows_e = T([1,2])([6.1,1])(hollows_f2_e)
    e2_1 = DIFFERENCE([muro_f2_est,t1_hollows_e])
    e2_2 = DIFFERENCE([o2_1,t2_hollows_o])
    e2 = T(2)(0.5)(T([1,2,3])([8,0,3])(R([1,2])(PI/2)(R([2,3])(PI/2)((DIFFERENCE([o2_2,t3_hollows_o]))))))
    
    est = [e1,e2]




    return sud+ovest+est+nord

#VIEW(STRUCT(walls()))