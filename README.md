# TP DE CONCEPTION DE LOGICIEL
On peut séparer ce rendu de TP en deux parties :

## Partie Webservice :
Cette partie implémente un webservice.
Ce Webservice permet d'obtenir l'identifiant d'un deck :
Pour cela il faut faire un get sur http://127.0.0.1:8000/create_deck.
La réponse à cette requête est de la forme :
```json
{
    "deck_id": "3p40paa87x90"
}
```
Mais aussi de piocher des cartes de ce deck :
Pour cela il faut faire un post sur http://127.0.0.1:8000/draw_cards/{nbCards}.
La réponse à cette requête est de la forme :
```json
{
    "deck_id": "3p40paa87x90",
    "cards": "<<ListeDesCartes>>"
}
```
Où la liste des cartes est donnée dans le même format que celui de l'API DeckOfCards.
Si aucun deck n'a été créé au préalable, un deck est alors créé automatiquement.

### Pour lancer le webservice : 
- Depuis la racine :
    - ``` $ cd Webservice ```
- puis :
    - ``` $ pip3 install -r requirements.txt ```
    - Ou alors sous windows : ``` $ pip install -r requirements.txt ```
- et enfin :
    - ``` $ uvicorn main:app --reload ```


## Partie Client :
La partie client du code implémente un scénario typique de l'utilisation du webservice.
On commence par consruire un nouveau deck, duquel on affiche l'identifiant. Puis on pioche dix cartes. Et on fini par compter le nombre de cartes de chaque couleur.
### Pour lancer le scénario client : 
- Depuis la racine :
    - ``` $ cd Client ```
- puis :
    - ``` $ pip3 install -r requirements.txt ```
    - ``` $ python3 main.py ```
    - Ou alors sous windows : ``` $ pip install -r requirements.txt ```
    - et ``` $ python main.py ```

## Tests Unitaires
Le projet ne comporte qu'un seul test permettant de tester la fonction de comptage des cartes.
### Pour lancer le test :
- Depuis la racine :
    - ``` $ cd Client  ```
- puis, si ce n'est pas déjà fait :
    - ``` $ pip3 install -r requirements.txt ```
    - Ou alors sous windows : ``` $ pip install -r requirements.txt ```
- et enfin :
    - ``` $ python3 -m unittest tests/test_client.py  ```
    - Ou alors sous windows : ``` $ python -m unittest tests/test_client.py  ```

Et voilà ! Merci et à bientôt pour de nouveaux projets ;) !