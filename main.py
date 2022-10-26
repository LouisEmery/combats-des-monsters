import random
death = False
niveau_de_vie = 20
numero_adversaire = 0
regles_du_jeu = ("Vous entrez un dongeon, vous avez 20 vies. \nvous arrivez face a face avec de monstres avec un niveau de pouvoir aleatoire entre 1 et 5. \nsi vous voulez les batre, appuiez 1, si vous gagnez, vous gagnez un nombre de vies egales au nombre de pouvoir au monstre.\nsi vous perdez, vous perdez le nombre de vie egale au pouvoir du monstre. votre attaque est aleatoire entre 1 et 6. \nsi vous voulez le contourner, apuiez 2.vous allez perdre une vie et aller a un prochain monstre. \nsi vous voulez quitter la partie, apuiez 4.")
pdv = 0
force_adversaire = 0
choix = 0
def MONSTRE():
    global force_adversaire
    force_adversaire = random.randint(1, 5)
def choice():
    global death
    global niveau_de_vie
    global numero_adversaire
    global regles_du_jeu
    global pdv
    global choix
    choix = int(input("Que voulez vous faire?\n1: Attacker le monstre\n2: Controuner cet adversaire(-1 vie)\n3: Afficher les regles du jeu\n4: Quitter la partie"))
    if choix == 3:
        print(regles_du_jeu)
    elif choix == 1:
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
    elif choix == 4:
        death = True

    else:
        print("choix invalide.")
    return choix

while not death:

    if choix != 3:
        MONSTRE()
    print("Vous tombez face à face avec un adversaire de difficulté :", force_adversaire)
    numero_adversaire += 1
    choice()
