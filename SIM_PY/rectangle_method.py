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
def rect(f,xmin,xmax,nbr):    
    # METHODE DES RECTANGLE CALCUL ET GRAPH 
    x=np.linspace(xmin,xmax,nbr+1)
    y = f(x)
    integrale_rectangle = 0
    for i in range(nbr):
        integrale_rectangle = integrale_rectangle + y[i]*(x[i+1]-x[i]) 
        x_rect = [x[i], x[i], x[i+1], x[i+1], x[i]] 
        y_rect = [0 , y[i], y[i] , 0 , 0 ] 
        plt.plot(x_rect, y_rect,"c") 
        
    plt.title("Représentation visuelle de l'intégrale avec la méthode des réctangles",loc='center')
    
    X=np.linspace(xmin,xmax,501)
    Y=f(X)
    plt.plot(X,Y,"0.4")
    
    plt.show()
    print("\tméthode des réctangles: integrale =", "{:.7f}".format(integrale_rectangle) )
    return(integrale_rectangle)