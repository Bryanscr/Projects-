# Dice Game

import os 

import random

def dice_rolls(): # rolls dice 3 times 
   rolls = [] # Empty list to store the results of dice rolls
   counter = 0 # A counter variable to track the number of rolls
   die_faces = (1, 2, 3, 4, 5, 6) # Define the faces of the die 
   while counter < 3: # Loop to 3 dice rolls 
       rolls.append(random.choice(die_faces)) # Randomize dice rolls 
       counter += 1 # Increment the counter to track the number of rolls
   return rolls # Return the list

def tupled_out(dice):
    return len(set(dice)) == 1 # Checks if the 3 dice have the same value

def fixed(dice):
    return len(set(dice)) == 2 # Checks if the two dice have the same value 

players = ["Player 1", "Player 2"]

def game(players, certain_score = 50):
    player_scores = {player: 0 for player in players}
    for player in players:
        print(f"Welcome to Tuple Out Dice Game\n{player}'s turn:")
        player_points = 0 
        rolls = 0 
        tupled_out_flag = False  # Flag to indicate if the player has tupled out
        while rolls < 3 and not tupled_out_flag:
            dice = dice_rolls()
            print(f"{player} rolled: {dice}")

            if tupled_out(dice):
                print("Tupled out!")
                tupled_out_flag = True
                break

            if fixed(dice):
                print("Your dice is fixed, you cannot re-roll")
                break
           
            players_answer = input("Do you want roll again? (yes/no): ")
            if players_answer.lower() == "no":
                break # End the loop if the player doesn't want to roll again

        if not tupled_out_flag:
            player_points += sum(dice)
            rolls += 1 

        player_scores[player] += player_points
        print(f"{player}'s turn ended. Total score: {player_scores[player]}")

    max_score = max(player_scores.values())
    winners = [player for player, score in player_scores.items() if score == max_score]
    if len(winners) == 1:
        print(f"{winners[0]} wins with a score of {max_score}!")    

game(players)

   
