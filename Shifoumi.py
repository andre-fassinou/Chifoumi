#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## shi
## File description:
## foumi
##

import random
import sys
def shifoumi():
    print("\nJe vous propose, histoire de passé le temps ce Pierre, Feuille, Ciseaux !\n")
    a = 0
    nbr_tr = input("Quel nombre de tour voulez-vous ?: ")
    player_score = 0
    computer_score = 0
    while a == 0:
        try:
            nbr_tr = int(nbr_tr)
            my_list = ['Pierre', 'Feuille', 'Ciseaux']
            hasard = random.choice(my_list)
            print()
            print(', ou '.join(my_list), "?")
            select = input("\nVeuillez saisir choix (vous pouvez écrire le mot en entier ou choisir la lettre qui convient): ")
            player_choice = select.capitalize()
            print("\n",player_choice, "VS", hasard, "\n")
            if(player_choice == 'P' or player_choice == 'Pierre'):
                if (hasard == 'Feuille'):
                    computer_score = computer_score + 1
                    print("\nEt ce point est à moi!\n J'ai",computer_score, "point(s)\n")
                elif(hasard == 'Ciseaux'):
                    player_score = player_score + 1
                    print("Un coup de chance\n Vous avez",player_score, "point(s)\n")
                elif(hasard == 'Pierre'):
                    print("Tu as regardé avant que je ne joue!\n")
            elif(player_choice == 'F' or player_choice == 'Feuille'):
                if (hasard == 'Ciseaux'):
                    computer_score = computer_score + 1
                    print("\nBah oui! Je suis plus doué que toi!\n J'ai",computer_score, "point(s)\n")
                elif(hasard == 'Pierre'):
                    player_score = player_score + 1
                    print("\nJe t'ai juste laissé ce point histoire de faire genre!!\n Vous avez",player_score, "point(s)\n")
                elif(hasard == 'Feuille'):
                    print("\nEgalité\n")
            elif(player_choice == 'C' or player_choice == 'Ciseaux'):
                if (hasard == 'Pierre'):
                    computer_score = computer_score + 1
                    print("\nJ'ai été cchampion du monde 3 fois de suite dans ce jeu!\n J'ai",computer_score, "point(s)\n")
                elif(hasard == 'Feuille'):
                    player_score = player_score + 1
                    print("\nChance du débutant comme on dit!\n Vous avez",player_score, "point(s)\n")
                elif(hasard == 'Ciseaux'):
                    print("\nJ'ai un doute là! T'as vu mon coup avant de jouer\n")
            else:
                print("Non inh")
                continue
            nbr_tr = nbr_tr - 1
            print("Il nous reste", nbr_tr, "tour(s)")
            if (nbr_tr == 0):
                print("\nVotre score finale est de", player_score, "point(s)\n")
                print("Le mien est de",computer_score, "point(s)\n")
                if (player_score > computer_score):
                    print("Je gagnerai la prochaine fois!\n")
                elif(player_score < computer_score):
                    print("Vous n'avez pas démérité. J'étais simplement plus fort! Hahaha!\n")
                else:
                    print("Vous êtes un sérieux adversaire\n")
                sys.exit("Le patie est terminée")
        except ValueError:
            sys.exit("vous avez un caractère inapproprié")
shifoumi()