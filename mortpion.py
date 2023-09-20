#test projet fin de semestre 

import os
import sys

nul = False
victoir = False
emplacement1 = " "
emplacement2 = " "
emplacement3 = " "
emplacement4 = " "
emplacement5 = " "
emplacement6 = " "
emplacement7 = " "
emplacement8 = " "
emplacement9 = " "

espace = """



"""


#os.system('cls')
def grille():
    grille = f"""
    {emplacement1}¹| {emplacement2}²| {emplacement3}³  
    ---------
    {emplacement4}⁴| {emplacement5}⁵| {emplacement6}⁶  
    ---------
    {emplacement7}⁷| {emplacement8}⁸| {emplacement9}⁹ 
    """
    print(grille)

def conditionVictoir():
    global emplacement1, emplacement2, emplacement3, emplacement4, emplacement5, emplacement6, emplacement7, emplacement8, emplacement9, victoir
    lignes = [(emplacement1, emplacement2, emplacement3), (emplacement4, emplacement5, emplacement6), (emplacement7, emplacement8, emplacement9),
            (emplacement1, emplacement4, emplacement7), (emplacement2, emplacement5, emplacement8), (emplacement3, emplacement6, emplacement9),
            (emplacement7, emplacement5, emplacement3), (emplacement1, emplacement5, emplacement9)]
    for lignes in lignes:
        if lignes[0] == lignes[1] == lignes[2] and lignes [0] != " ":
            victoir = True

def conditionNul():
    global emplacement1, emplacement2, emplacement3, emplacement4, emplacement5, emplacement6, emplacement7, emplacement8, emplacement9, nul
    if emplacement1== " " or emplacement2== " " or emplacement3== " " or emplacement4== " " or emplacement5== " " or emplacement6== " " or emplacement7== " " or emplacement8== " " or emplacement9== " ":
        nul = True
    else:
        nul = False
    
def reinitialisation():
    global emplacement1, emplacement2, emplacement3, emplacement4, emplacement5, emplacement6, emplacement7, emplacement8, emplacement9, victoir, nul
    nul = False
    victoir = False
    emplacement1 = " "
    emplacement2 = " "
    emplacement3 = " "
    emplacement4 = " "
    emplacement5 = " "
    emplacement6 = " "
    emplacement7 = " "
    emplacement8 = " "
    emplacement9 = " "

def entrée():
    global emplacement1, emplacement2, emplacement3, emplacement4, emplacement5, emplacement6, emplacement7, emplacement8, emplacement9, victoir, nul
    while True:
        while True:
            conditionNul()
            if nul:
                os.system('cls')
                grille()
                try:
                    entrée = int(input("joueur 1, jouez: "))
                    if 1 <= int(entrée) <= 9:
                        entrée2 = "emplacement" + str(entrée)
                        if entrée2 != "O" and entrée2 != "X" and globals()[entrée2] == " ":
                            os.system('cls')
                            globals()[entrée2] = "X"
                            conditionVictoir()
                            if victoir:
                                grille()
                                print(espace)
                                print("Félicitation, vous avez gagner joueur 1.")
                                input("Appuyez sur Entrée pour revenir au menu principal...")
                                Main()
                            break
                        else:
                            print("Case déja ocupé, veuillez choisire une autre case.")
                            input()
                    else:
                        print("Saisie invalide, veuillez entrer un nombre valide.")
                        input()
                except ValueError:
                    print("Saisie invalide, veuillez entrer un nombre valide.")
                    input()
            else:
                grille()
                print(espace)
                print("matche nul")
                input("Appuyez sur Entrée pour revenir au menu principal...")
                Main()

        while True:
            conditionNul()
            if nul:
                os.system('cls')
                grille()
                try:
                    entrée = int(input("joueur 2, jouez: "))
                    if 1 <= int(entrée) <= 9:
                        entrée2 = "emplacement" + str(entrée)
                        if entrée2 != "O" and entrée2 != "X" and globals()[entrée2] == " ":
                            os.system('cls')
                            globals()[entrée2] = "O"
                            conditionVictoir()
                            if victoir:
                                grille()
                                print(espace)
                                print("Félicitation, vous avez gagner joueur 2.")
                                input("Appuyez sur Entrée pour revenir au menu principal...")
                                Main()
                            break
                        else:
                            print("Case déja ocupé, veuillez choisire une autre case.")
                            input()
                    else:
                        print("Saisie invalide, veuillez entrer un nombre valide.")
                        input()
                except ValueError:
                    print("Saisie invalide, veuillez entrer un nombre valide.")
                    input()
            else:
                grille()
                print(espace)
                print("matche nul")
                input("Appuyez sur Entrée pour revenir au menu principal...")
                Main()


def Main():
    reinitialisation()
    while True:
        titre = """
         __  __  _____  ____  ____  ____  ____  _____  _  _ 
        (  \/  )(  _  )(  _ \(_  _)(  _ \(_  _)(  _  )( \( )
         )    (  )(_)(  )   /  )(   )___/ _)(_  )(_)(  )  ( 
        (_/\/\_)(_____)(_)\_) (__) (__)  (____)(_____)(_)\_)

        


        1) Jouer
        2) Maj log
        3) Quitter

                            
        version 1.2.7
        """
        os.system('cls')
        print(titre)
        choix = input("Sélectionnez une option : ")
        if choix == "1":
            print("                           Bon jeu")
            entrée()
        elif choix == "2":
            os.system('cls')
            #add maj log avec model suivant
            """
            Version x.x
                correctif de...
                ajout de...

            """
            maj_log = """
            Version actuelle : 1.2.7

            Version 0.0.1
                - Ajout du menu principal

            Version 0.0.2
                - Ajout de la grille
                - Correctif du menu

             Version 0.0.4
                - Modification d'interface
                - Correctif de bugs

            Version 0.0.5
                - Ajout du journal des mises à jour (maj log)
                - Modification du menu
                - Début de développement du mode Joueur vs Joueur (PvP)
                - Correctif de bugs

            Version 0.1.5
                - Correctif de bug
                - Optimisation géneral
                - Début des testes du mode PVP

            Version 0.1.6
                - Correctif de jouabilité
                - Correctif de bug

            Version 1.1.6
                - Ajout de condition de victoir
                - Ajour de condition de match nul
                - Optimisation du mode PvP
            
            Version 1.2.6
                - Correctif des conditions
                - Optimisations des fonctions condition
                - Ajout d'un retour au menu en fin de partie

            Version 1.2.7
                - Correctif de bug liée a la 1.2.6
                - Réinitialisation des variables après chaque partie

                
                """
            print(maj_log)
            input("...")
            print(maj_log)
        elif choix == "3":
            print("aurevoir.")
            sys.exit()

Main()
"""
⁰
¹
²
³
⁴
⁵
⁶
⁷
⁸
⁹
                 
"""