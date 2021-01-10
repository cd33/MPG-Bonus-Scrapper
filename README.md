# MPG Bonus Scrapper Python

Récupérer le nombre de bonus restants de vos adversaires sur MPG (Mon Petit Gazon)

Je vous invite à découvrir le travail, bien plus complet de Behel, dont je me suis inspiré et dont j'ai pris les bases du code pour me focaliser uniquement sur les bonus.
Projet original de Behel : https://github.com/Behel/mpg-scrapper

Pour lancer MPG Bonus Scrapper : 
- Lancer la commande ``pip install -r requirements.txt``

Deux choix s'offre à vous :
- Découvrir les bonus restants d'une équipe en particulier :
  - Editez le fichier ``bonus.py`` et indiquez votre email & mot de passe de connexion MPG + l'identifiant de la ligue et le nom de la team recherchée.
  - (Facultatif) Si votre ligue est inférieur à 10 joueurs, vous devez changer les bonus en fonction dans le fichier ``bonus.py``.
  - Lancer la commande ``python3 bonus.py``
 
- Découvrir les bonus restants de tous les adversaires :
  - Editez le fichier ``bonus_all.py`` et indiquez votre email & mot de passe de connexion MPG + l'identifiant de la ligue.
  - (Facultatif) Si votre ligue est inférieur à 10 joueurs, vous devez changer les bonus en fonction dans le fichier ``bonus_all.py``.
  - Lancer la commande ``python3 bonus_all.py``

Ci dessous, le nombre de bonus en fonction du nombre de participant dans votre ligue (4, 6, 8 ou 10) :

    # ligue de 4
    bonus = [
        'Valise',
        'Uber Eats'
    ]

    # ligue de 6
    bonus = [
        'Valise',
        'Zahia',
        'Suarez',
        'Uber Eats',
        'Uber Eats',
        'Miroir'
    ]
    
    # ligue de 8
    bonus = [
        'Valise',
        'Zahia',
        'Suarez',
        'Uber Eats',
        'Uber Eats',
        'Uber Eats',
        'Miroir',
        'Chapron',
        'Pat Evra'
    ]

    # ligue de 10
    bonus = [
        'Valise',
        'Zahia',
        'Suarez',
        'Suarez',
        'Uber Eats',
        'Uber Eats',
        'Uber Eats',
        'Miroir',
        'Chapron',
        'Pat Evra'
    ]
