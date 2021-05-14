# TP DE CONCEPTION DE LOGICIEL
On peut séparer ce rendu de TP en deux parties : <br>

## Partie Webservice :
Cette partie implémente un webservice.<br>
Ce Webservice permet d'obtenir l'identifiant d'un deck :<br>
Pour cela il faut faire un get sur http://127.0.0.1:8000/create_deck.<br>
La réponse à cette requête est de la forme :<br>
``` $ {``` <br>
``` $ "deck_id": "3p40paa87x90"``` <br>
``` $ }``` <br>
Mais aussi de piocher des cartes de ce deck :<br>
Pour cela il faut faire un post sur http://127.0.0.1:8000/draw_cards/{nbCards}".<br>
La réponse à cette requête est de la forme :<br>
``` $ {``` <br>
``` $ "deck_id": "3p40paa87x90",``` <br>
``` $ "cards": "<<ListeDesCartes>>"``` <br>
``` $ }``` <br>
La liste des cartes est donnée dans le même format que celui de l'API DeckOfCards.<br>
Si aucun deck n'a été créé au préalable, un deck est alors créé automatiquement.<br>

### Pour lancer le webservice : 
Depuis la racine : <br>
``` $ cd Webservice ``` <br>
puis :<br>
``` $ pip3 install -r requirements.txt ``` <br>
ou alors :<br>
``` $ pip install -r requirements.txt ``` <br>
et enfin :<br>
``` $ uvicorn main:app --reload ``` <br>


## Partie Client :
La partie client du code implémente un scénario typique de l'utilisation du webservice.<br>
On commence par consruire un nouveau deck, duquel on affiche l'identifiant. Puis on pioche dix cartes. Et on fini par compter le nombre de cartes de chaque couleur.
### Pour lancer le scénario client : 
Depuis la racine : <br>
``` $ cd Client ``` <br>
puis :<br>
``` $ pip3 install -r requirements.txt ``` <br>
``` $ python3 main.py ``` <br>
ou alors :<br>
``` $ pip install -r requirements.txt ``` <br>
``` $ python main.py ``` <br>

## Tests Unitaires
Le projet ne comporte qu'un seul test permettant de tester la fonction de comptage des cartes.<br>
### Pour lancer le test :
Depuis la racine :<br>
``` $cd Client  ``` <br>
puis, si ce n'est pas déjà fait :<br>
``` $pip3 install -r requirements.txt ``` <br>
ou alors :<br>
``` $pip install -r requirements.txt ``` <br>
et enfin :<br>
``` $python3 -m unittest tests/test_client.py  ``` <br>
ou alors<br>
``` $python -m unittest tests/test_client.py  ``` <br>

Et voilà ! Merci et à bientôt pour de nouveaux projets ;) !