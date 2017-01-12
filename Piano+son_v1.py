# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 17:02:55 2017

@author: Zazou
"""

import sys

from functools import partial
import pyaudio
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import numpy as np



SR = 44100 #Hz (Sampling Rate)
# Sinus de fréquence F et de durée T, échantillonné tous les 1/SR :
def sinus(f,t):
    return np.sin(2*np.pi*f*np.arange((t*SR))/SR)

# Génération d'une note, avec des harmoniques supérieurs :
def note(f,t,a,b,c):
    return (a*sinus(f,t) + b* sinus(2*f,t) + c*sinus(6*f,t))
        
class Clavier(QWidget):
    def __init__(self):
        
        QWidget.__init__(self)
        
        #titre de la fenetre
        self.setWindowTitle('Clavier')
        
        #on définit un grid comme layout
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        
        #setspacing permet de gerer l'espace prédéfini entre les différents widget
        # 0 en argument = pas d'espace
        self.grid.setSpacing(0)
        
        self.bouton = QPushButton('JOUER')
        self.grid.addWidget(self.bouton,0,0)
        self.bouton.clicked.connect(self.jouer)
        
        
        self.sl = QSlider(Qt.Horizontal)
        self.sl.setMinimum(0)
        self.sl.setMaximum(200) 
        self.sl.setValue(100)
        self.sl.setTickPosition(QSlider.TicksBelow)
        self.sl.setTickInterval(10)    
        self.sl.setMinimumWidth(200)
        label0 = QLabel("coefficient harmonique ")
        self.grid.addWidget(label0,13,12)
        self.grid.addWidget(self.sl,13,13)
        
        self.sl.valueChanged.connect(self.jouer)
        
        self.coeff_harm1 = QSlider(Qt.Horizontal)
        self.coeff_harm1.setMinimum(0)
        self.coeff_harm1.setMaximum(200)        
        self.coeff_harm1.setValue(100)
        self.coeff_harm1.setTickPosition(QSlider.TicksBelow)
        self.coeff_harm1.setTickInterval(10)
        label1 = QLabel("coefficient harmonique 1")
        self.grid.addWidget(label1,14,12)
        self.grid.addWidget(self.coeff_harm1,14,13)
        
        self.coeff_harm1.valueChanged.connect(self.jouer)

        self.coeff_harm2 = QSlider(Qt.Horizontal)
        self.coeff_harm2.setMinimum(0)
        self.coeff_harm2.setMaximum(200)        
        self.coeff_harm2.setValue(100)
        self.coeff_harm2.setTickPosition(QSlider.TicksBelow)
        self.coeff_harm2.setTickInterval(10)
        label2 = QLabel("coefficient harmonique 2")
        self.grid.addWidget(label2,15,12)
        self.grid.addWidget(self.coeff_harm2,15,13)
        
        self.coeff_harm2.valueChanged.connect(self.jouer)
        
        self.show()


        
    def jouer(self):
        
        abcisses  = np.arange(2,13,1)
        y = 1
        liste_notes = ['c','c#','d','d#','e','f','f#','g','g#','a','a#','b']
        liste_frequence = [262,277,294,311,330,349,370,392,415,440,466,494]
           
        for i,j,x in zip(liste_notes,liste_frequence,abcisses) :

            if i.find('#') == 1:
                self.i  = QPushButton(i)                
                self.i.setStyleSheet("background-color: black")
                #défini la taille du bouton
                self.i.setFixedSize(50,300)                
            else:
                self.i  = QPushButton(i)
                self.i.setFixedSize(101,300)
            #ajoute le bouton a la fenetre
            self.grid.addWidget(self.i,y,x)
            coeff2 = self.coeff_harm2.value()/100.
            coeff1 = self.coeff_harm1.value()/100.
            coeff0 = self.sl.value()/100.
            self.i.clicked.connect(partial(self.sortie,j,coeff0,coeff1,coeff2))

    def sortie(self,F,coeff_fonda,coeff_harm1,coeff_harm2):
              
        T=1
        n=1
        son = note(F,T,coeff_fonda,coeff_harm1,coeff_harm2)
        volume = np.sin(2*np.pi*np.arange(n*T*SR)/(n*T*SR))
        son = son*volume        
        #jeu du son
        p = pyaudio.PyAudio()
        stream = p.open(format=pyaudio.paFloat32, channels=1, rate=44100, output=1)
        stream.write(son.astype(np.float32).tostring())
        stream.close()
        p.terminate()
        
app = QApplication.instance() 
if not app:
    app = QApplication(sys.argv)
        
fen = Clavier()
app.exec_()


#https://www.tutorialspoint.com/pyqt/pyqt_qslider_widget_signal.htm
