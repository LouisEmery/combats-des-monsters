import random

death = False
niveau_de_vie = 20
numero_adversaire = 0
pdv = 0
regles_du_jeu = ("Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.  Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire. Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire.  Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire. La partie se termine lorsque les points de vie de l’usager tombent sous 0. L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie.")


def choice():
    global death
    global niveau_de_vie
    global numero_adversaire
    global regles_du_jeu
    global pdv
    choix = int(input("Que voulez vous faire?\n1: Attacker le monstre\n2: Controuner cet adversaire(-1 vie)\n3: Afficher les regles du jeu\n4: Quitter la partie"))
    if choix == 1:
        dice_roll = random.randint(1, 6)
        print("vous avez roule", dice_roll)
        if dice_roll <= force_adversaire:
            niveau_de_vie -= force_adversaire
            if niveau_de_vie <= 0:
                print("vous etes mort apres", pdv, "monstres")
                death = True
            else:
                print("il vous reste", niveau_de_vie, "vies\n")

        else:
            niveau_de_vie += force_adversaire
            pdv += 1
            print("vous avez reussi\n+1 point de victoire!\nil vous reste", niveau_de_vie, "vies\n")

    elif choix == 2:
        niveau_de_vie -= 1
        print("vous avez", niveau_de_vie, "vies\n")
        if niveau_de_vie <= 0:
            print("vous etes mort apres", pdv, "monstres")
            death = True
    elif choix == 3:
        print(regles_du_jeu)
    elif choix == 4:
        death = True

    else:
        print("choix invalide.")

while not death:

    force_adversaire = random.randint(1, 5)
    print("Vous tombez face à face avec un adversaire de difficulté :", force_adversaire)
    numero_adversaire += 1
    choice()