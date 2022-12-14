import numpy as np
import matplotlib.pyplot as plt

'''
  Parameters
  ----------
  f : function
  xmin, xmax : numbers
    Interval of integration [xmin,xmax]
  nbr : integer
    Number of subintervals of [xmin,xmax]

  Returns
  -------
    float
      Approximation of the integral of f(x)
'''
def trapz(f,xmin,xmax,nbr):    
    # CALCUL METHODE DES TRAPEZ
    x=np.linspace(xmin,xmax,nbr+1)
    y = f(x)
    y_right = y[1:] # right endpoints
    y_left = y[:-1] # left endpoints
    dx = (xmax - xmin)/nbr
    integral_trapeze= (dx/2) * np.sum(y_right + y_left)
        
    # GRAPHE METHODE DES TRAPEZE   
    for i in range(nbr):
        x_trap = [x[i],x[i],x[i+1],x[i+1]]
        y_trap = [0,f(x[i]),f(x[i+1]),0]
        plt.fill(x_trap,y_trap,'y',edgecolor='y',alpha=0.2)
    
    plt.title("Représentation visuelle de l'intégrale avec la méthode des trapèzes",loc='center')
   
    X=np.linspace(xmin,xmax,501)
    Y=f(X)
    
    plt.plot(X,Y,"0.4")

    plt.show()

    print("\tméthode des trapèzes: integrale   =","{:.7f}".format(integral_trapeze))
    return (integral_trapeze)