# LuMI-synthesizer

Écriture du projet séparée en plusieurs parties : 

· interface utilisateur (acquisition des consignes de l'utilisateur via le clavier, production de la "partition" correspondante) ;

· générateur de son (lecture de la "partition" et production subséquente d'un signal lu par la carte son) ;

· gestion du jeu en direct (aspect non encore traité).


Le générateur de son correspond au fichier generateur_de_son.py (il reste un bug pour qu'il puisse être lu directement).


Améliorations rêvables : 
afficher le spectrogramme joué en direct ; 
moduler le son (pour lui donner de la distorsion, ou de la résonance… http://www.pianoweb.fr/filtres-analogiques.php) en direct avec la molette de la souris ; 
créer des timbres à partir d'enregistrement audio d'instruments réels ; 
…
