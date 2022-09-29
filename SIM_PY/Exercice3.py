"""Exercice 3"""

from utils_lag_tche import *
from math import  pi  

f=lambda x:np.cos(x)

represent(f,0,pi/2,100)

lagrange_math(f,0,pi/2,5)

tchebychev(0,10)

tchebychev_plot(f,0,pi/2,5,0,10) #choix n=0 x=10 
