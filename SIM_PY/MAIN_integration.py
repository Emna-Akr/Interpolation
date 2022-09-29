"SOLUTION DE L'EXERCICE 2"
 
import numpy as np

from rectangle_method import rect
from trapezoid_method import trapz

f=lambda x : np.sin(4*x)*np.exp(-x**2+3*x)

xmin=0
xmax=5
nbr_list =[ 100, 150, 450, 1000]

for nbr in nbr_list:
  print('\t\033[2;36mCalcul d"integrale pour nbr = \033[0;0m', nbr)
  rect(f,xmin,xmax,nbr)
  trapz(f,xmin,xmax,nbr)
  print('\n')
