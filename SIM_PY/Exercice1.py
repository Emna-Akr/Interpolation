
"""Exercice 1""" 
from utils_lag_tche import *

fonc1=lambda x:1/(1+4*x)

represent(fonc1,0,3,100)

pol_lagrange(fonc1,0,3,5)

#OU BIEN 
#lagrange_math(f,0,3,5)

tchebychev(0,3.5)