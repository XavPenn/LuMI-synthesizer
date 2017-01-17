# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 22:11:08 2017

@author: Simon
"""

from __future__ import division
import numpy as np
import pyaudio   # python -m pip install pyaudio
taux = 44100

# Fonctionnement du programme :
# lecture d'une partition (liste de sons), par correspondance avec un répertoire,
# produisant un signal joué par la carte son.


####### CLASSES #######
class Son:
    """
    (Doc à écrire)
    Amélioration possible : ajouter une étape de convolution du son pour moduler l'attaque et l'évolution du son
    """  
    def __init__(self, debut, hauteur, timbre, enveloppe, duree=3):
        self.debut = debut*taux
        self.duree = duree*taux
        self.timbre = R[timbre].get
        self.spectre = np.concatenate((self.timbre[1000-np.floor(R[hauteur]):],np.zeros(self.duree-9000+np.floor(R[hauteur])))) 
        # Permet d'avoir un spectre comportant le timbre transposé, et qui soit de la longueur du signal final.
        self.enveloppe = Enveloppe(enveloppe,duree).get
        self.get = np.fft.ifft(self.spectre)*self.enveloppe
        
class Timbre:
    """
    Fréquences de 0 à 9999 Hz, avec la hauteur principale (note entendue) à 1000 Hz.
    """
    def __init__(self,largeur):
        self.get = np.exp(-(np.arange(10000)-999)**2/(2*largeur**2))
        # À ajouter : la possibilité d'asymétriser la courbe
        
    def harmoniques(self,coefs):
        for i,amplitude in enumerate(coefs):
            self.get[1000*(i+2)/(i+1)] += amplitude
        return self
            
    def passe_bas(self,frequence_coupure,largeur=200):
        self.get *= filtre(frequence_coupure,largeur,10000)[::-1]
        return self
        
    def passe_haut(self,frequence_coupure,largeur=200):
        self.get *= filtre(frequence_coupure,largeur,10000)
        return self
    
class Enveloppe:
    """
    (Doc à écrire)
    """
    def __init__(self,profil,duree):
        self.duree = duree*taux
        if profil=='sin':
            self.get = np.sin(np.pi*np.linspace(0,1,self.duree))
        elif profil=='lin':
            self.get = np.concatenate((np.linspace(0,1,self.duree/2),1-np.linspace(0,1,self.duree/2)))
    
    def vibrato(self, frequence,amplitude):
        self.get += amplitude*np.sin(2*np.pi*frequence*np.arange(self.duree))
        return self


####### FONCTIONS #######
def jouer(partition):
    """
    (Doc à écrire)
    """
    signal = np.array([])
    for son in partition:
        if len(signal)<son.debut+son.duree:
            signal = np.concatenate((signal,np.zeros(son.debut+son.duree-son.duree)))
        signal[son.debut:son.debut+len(son.get)] += son.get
# La syntaxe qui suit est tirée de davywybiral.blogspot.fr/2010/09/procedural-music-with-pyaudio-and-numpy.html
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32, channels=1, rate=taux, output=1)
    stream.write(signal.astype(np.float32).tostring())
    stream.close()
    p.terminate()
        
def filtre(coupure, largeur, taille):
    return np.concatenate((np.zeros(coupure-largeur),np.linspace(0,1,largeur),np.ones(taille-coupure)))
        
        
####### REPERTOIRE #######
R={'1':Timbre(10).harmoniques((0.5,0.2,0.2,0.1,0.04,0.06))}
R.update({'2':Timbre(70).harmoniques((0,0,0.2,0.1,0.5,0.6,0.4,0.2,0.1))})
for i,clef in enumerate(('a','z','e','r','t','y','u','i','o','p')):
    R.update({clef:261.63*2**(i/12)})




partition = (Son(0,'a', '1', 'sin'),Son(1,'a','2','lin',5),Son(3,'r','1','sin'))
jouer(partition)