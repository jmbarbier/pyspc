# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 12:32:29 2018

@author: guill
"""
from math import *
from numpy import *
import matplotlib.pyplot as plt



def pikachu(t):#creation de la fonction position de pikachu selon y en fonction du temp
    y=-0.5*9.81*t*t+2
    return(y)

def pokeball(t): #fonction de la position de la pokeball selon x en fonction du temps
    y=-0.5*9.81*t*t+15.6*sin(11.3*pi/180)*t
    return(y)

def pokeball1(t): # fonction de la pokeball en y selon le temps
    y=15.6*cos(11.3*pi/180)*t
    return(y)
    
l=[1/10+1/10*(i-1) for i in range (0,20)] # creation de la liste des temps ici tout les 0.1s


k=0  # initialisation du parametre k
Ly=[]# on cree des liste pour stocker les differente valeur calculer 
Lx=[]# en effet cela permet de tracer le graphique en fonction des coordonne y(t) et x(t)
Ly1=[]#pour la pokeball et pikachu
Lx1=[]
while pikachu(l[k])>=0: # boucle while pour calculer les differentes valeur des positions de pikachu et pokeball 
    y=pikachu(l[k]) #calcule des x(t) et y(t) de la pokeball et pikachu
    x=10
    y1=pokeball1(l[k])
    x1=pokeball(l[k])
    Ly.append(y) # ajout des valeur au liste respective
    Lx.append(x)
    Ly1.append(y1)
    Lx1.append(x1)
    k=k+1
    M, =plt.plot(Lx,Ly,'*')# affichage de la valeur sur le graphique
    P, =plt.plot(Ly1,Lx1,'*')
    plt.pause(1) # pause pour voir l'evolution
    plt.draw()
plt.show() #on le montre a la fin


    
    
    