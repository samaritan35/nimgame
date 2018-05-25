import random
import json

from pprint import pprint


if __name__ == '__main__':
    
    """ Setting up the heaps """
    print("Veuillez Entrer le nom du premier Joueur")
    player1 = input()
    print("Veuillez Entrer le nom du deuxième Joueur")
    player2 = input()

    number_of_heaps = random.randint(3, 7)
    heaps = {}
    for i in range(number_of_heaps):
        heaps [i] =  random.randint(5, 23)
    
    #open save file to get scores
    #data: is a dict to store our scores
    data = {}
    with open('save.json') as jsonFile:
        try:
            data = json.load(jsonFile)
        except ValueError:
            data = {}

    #initialize best score for both players
    last_best_score_1 = 0
    last_best_score_2 = 0
    
    #set score for both players
    if (player1 in data):
        last_best_score_1 = data[player1]
    else:
        data[player1] = 0
        with open('save.json', 'w') as jsonFile:
            json.dump(data, jsonFile)

    if (player2 in data):
        last_best_score_2 = data[player2]
    else:        
        data[player2] = 0
        with open('save.json', 'w') as jsonFile:
            json.dump(data, jsonFile)

    #begin the game
    print("Qui va jouer en premier?")
    premierTour = input()
    prochainTour =""
    #get the first player and set up tours
    if (premierTour == player1):
        prochainTour = player2
        premierTour = player1
    elif (premierTour == player2):
        prochainTour = player1
        premierTour = player2
    else:
        while (premierTour != player1 and premierTour != player2):
            print("Veuillez entrer le nom d'un des joueurs participants")
            premierTour = input()
    

    end = False
    
    score_player_1 = 0
    score_player_2 = 0

    winner = ""
    steps_player1 = 0
    steps_player2 = 0

    while (end==False):
        tour = premierTour
        print("Tour de ", tour)
        
        for k,v in heaps.items():
            print ("tas: ", k, "|\t", heaps[k] * '*', "| ", heaps[k])
        print("Veuillez entrer le numero de tas: ")
        
        heap = int(input())
        while (heap not in heaps):
            print("Veuillez entre le numéro exacte du tas")
            heap = int(input())

        if (heaps[heap] == 1):
            if (tour == player1):
                winner = player2
            else:
                winner = player1
            break

        print("Veuillez entrer le nombre de pièrres: ")
        stones = int(input())
        while (stones > heaps[heap]):
            print("Veuillez un nombre de pièrres inférieur à: ", heaps[heap])
            stones = int(input())

        if(tour == player1):
            steps_player1 = steps_player1 + 1
            print("inside1: ", steps_player1)
        else:
            steps_player2 = steps_player2 + 1
            print("inside2: ", steps_player2)

        heaps[heap] = heaps[heap] - stones
        premierTour = prochainTour
        prochainTour = tour

    if (winner == player1):
        for i in range(1, steps_player1+1):
            score_player_1 = score_player_1 + i*pow(10, i)
        data[player1] = score_player_1
        with open('save.json', 'w') as jsonFile:
            json.dump(data, jsonFile)
    else:
        for i in range(1, steps_player2):
            score_player_2 = score_player_2 + i*pow(10, i)
        data[player2] = score_player_2
        with open('save.json', 'w') as jsonFile:
            json.dump(data, jsonFile)
   
    for k,v in data.items():
        print("Les scores--")
        print(k, " : ", data[k])

    


    



    
