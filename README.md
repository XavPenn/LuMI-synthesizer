# LuMI-synthesizer

Premier essai de synthèse additive et d'interfacage de la carte son : voir le fichier premier_essai.py
(pour installer pyaudio, en ligne de commande windows : python -m pip install pyaudio)


Premières idées de fonctionnalités à implémenter dans le programme :

· afficher le spectrogramme joué en direct ;

· commander par le clavier le changement de son. Par exemple, une lettre (a-z) déclenche le jeu d'une certaine hauteur de note ; un chiffre (0-9) déclenche le passage à un certain timbre (forme de spectre pré-définie, avec éventuellement une attaque et un release pré-définis aussi) ;

· moduler le son (pour lui donner de la distorsion, ou de la résonance… http://www.pianoweb.fr/filtres-analogiques.php) avec la molette de la souris ;

· faire une transition progressive d'une consigne à une autre (par exemple, extrapolation linéaire de chaque coefficient du spectre entre le son précédent et le son venant d'être commandé par le clavier), pour jouer en direct ;

…



Exemples glanés : https://github.com/Penguinum/python-synth ; https://github.com/belangeo/zyne ; https://mdoege.github.io/PySynth ; https://wiki.python.org/moin/PythonInMusic
