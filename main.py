import random
#declaration de variable
compteur_joueur = 0
compteur_ordi = 0
choix = ["p", "f", "c"]

#premier choix
choix_joueur = input("On joue à Pierre-feuille-ciseaux ? Pour jouer entre 'p' 'f' ou 'c'")
choix_ordinateur = random.choice(choix)


while compteur_joueur != 2 or compteur_ordi != 2:
    if choix_ordinateur == "p" and choix_joueur == "c" or choix_ordinateur == "f" and choix_joueur == "p" or choix_ordinateur == "c" and choix_joueur == "f":
        compteur_ordi = compteur_ordi + 1
        print("J'ai choisi "+choix_ordinateur)
        print("Un point pour moi !")
        print("Score: "+ str(compteur_joueur)+" joueur et " + str(compteur_ordi)+" ordinateur")
    elif choix_joueur == "p" and choix_ordinateur == "c" or choix_joueur == "f" and choix_ordinateur == "p" or choix_joueur == "c" and choix_ordinateur == "f":
        compteur_joueur = compteur_joueur + 1
        print("J'ai choisi " + choix_ordinateur)
        print("Un point pour toi !")
        print("Score: " + str(compteur_joueur) + " joueur et " + str(compteur_ordi) + " ordinateur")
    else:
        print("J'ai choisi " + choix_ordinateur)
        print("égalité !")
        print("Score: " + str(compteur_joueur) + " joueur et " + str(compteur_ordi) + " ordinateur")
    choix_ordinateur = random.choice(choix)
    choix_joueur = input("'p' 'f' ou 'c'? ")
if compteur_joueur == 3:
    print("Tu as gagné !")
else:
    print("Et bim !!! J'ai gagné !")

