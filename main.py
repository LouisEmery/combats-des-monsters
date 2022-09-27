import random
death = False
niveau_de_vie = 20
numero_adversaire = 0
regles_du_jeu = ("hfjhfdj")
pdv = 0


def choice():
    choix = int(input("Que voulez vous faire?\n1: Attacker le monstre\n2: Controuner cet adversaire(-1 vie)\n3: Afficher les regles du jeu\n4: Quitter la partie"))
    if choix == 1:
        dice_roll = random.randint(1, 6)
    elif choix == 2:
        niveau_de_vie -= 1
        print(niveau_de_vie)
    elif choix == 3:
        print(regles_du_jeu)
    elif choix == 4:
        death = True
    else:
        print("choix invalide.")
while death != True:
    force_adversaire = random.randint(1, 5)
    print("Vous tombez face à face avec un adversaire de difficulté :", force_adversaire)
    numero_adversaire += 1
    choice()


