# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 17:03:46 2017

@author: Simon
"""

import numpy as np
import pyaudio

SR = 44100 #Hz (Sampling Rate)   

# Sinus de fréquence F et de durée T, échantillonné tous les 1/SR :
def sinus(f,t):
    return np.sin(2*np.pi*f*np.arange((t*SR))/SR)

# Génération d'une note, avec des harmoniques supérieurs :
def note(f,t):
    return (sinus(f,t) + 0.5*sinus(2*f,t) + 0.125*sinus(4*f,t))*0.2

F = 440 #Hz
T = 5 #s durée d'un son
n = 2 #nombre de sons
son1 = 0.7*note(F,T) + 0.5*note(3/2*F+2,T) + 0.4*note(5/4*F+1,T)
son2 = 0.4*note(F,T) + 0.2*note(1.2*F,T) + 0.6*note(1.4*F,T)

# Assemblage des éléments du son
son = np.concatenate((son1,son2))
volume = np.sin(2*np.pi*np.arange(n*T*SR)/(n*T*SR))
son = son*volume

# Jeu du son
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32, channels=1, rate=44100, output=1)
stream.write(son.astype(np.float32).tostring())
stream.close()
p.terminate()