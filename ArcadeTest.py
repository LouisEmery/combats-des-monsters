import random
death = False
niveau_de_vie = 20
numero_adversaire = 0
regles_du_jeu = ("Vous entrez un dongeon, vous avez 20 vies. \nvous arrivez face a face avec de monstres avec un niveau de pouvoir aleatoire entre 1 et 5. \nsi vous voulez les batre, appuiez 1, si vous gagnez, vous gagnez un nombre de vies egales au nombre de pouvoir au monstre.\nsi vous perdez, vous perdez le nombre de vie egale au pouvoir du monstre. votre attaque est aleatoire entre 1 et 6. \nsi vous voulez le contourner, apuiez 2.vous allez perdre une vie et aller a un prochain monstre. \nsi vous voulez quitter la partie, apuiez 4.")
pdv = 0
force_adversaire = 0
choix = 0
vc = 0
#defenir la force de l'adversaire
def MONSTRE():
    global force_adversaire
    global vc
    #3 victoires consecutives
    if vc >= 3:
        force_adversaire = random.randint(7, 14)
    else:
        force_adversaire = random.randint(1, 10)
#definir choix du joueur
def choice():
    global death
    global niveau_de_vie
    global numero_adversaire
    global regles_du_jeu
    global pdv
    global choix
    global vc
    choix = int(input("Que voulez vous faire?\n1: Attacker le monstre\n2: Controuner cet adversaire(-1 vie)\n3: Afficher les regles du jeu\n4: Quitter la partie"))
    #choix 3, afficher les regles.
    if choix == 3:
        print(regles_du_jeu)
        #choix 1, attacker le monstre
    elif choix == 1:
        dice_roll1 = random.randint(1, 6)
        dice_roll2 = random.randint(1, 6)
        dice_roll = dice_roll1 + dice_roll2
        print("vous avez roule", dice_roll)
        if dice_roll <= force_adversaire:
            niveau_de_vie -= force_adversaire
            vc = 0
            #prendre les dégats s'il perd#
            if niveau_de_vie <= 0:
                print("vous etes mort apres", pdv, "monstres")
                death = True
            else:
                print("il vous reste", niveau_de_vie, "vies\n")

        else:
            niveau_de_vie += force_adversaire
            pdv += 1
            vc += 1
            print("vous avez reussi\n+1 point de victoire!\nil vous reste", niveau_de_vie, "vies\n")
#esquiver le monstre
    elif choix == 2:
        niveau_de_vie -= 1
        print("vous avez", niveau_de_vie, "vies\n")
        #morts
        if niveau_de_vie <= 0:
            print("vous etes mort apres", pdv, "monstres")
            death = True
            #mort(choix 4)
    elif choix == 4:
        death = True

    else:
        print("choix invalide.")
    return choix
#en autant que tu ne meurt pas, continue
while not death:

    if choix != 3:
        MONSTRE()
    print("Vous tombez face à face avec un adversaire de difficulté :", force_adversaire)
    numero_adversaire += 1
    choice()
