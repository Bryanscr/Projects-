# Word Guessing Game 
import matplotlib.pyplot as plt
import pandas as pd 

secret_word= ["random", "car", "ice"]
player_1 = "Player 1"
player_2 = "Player 2"
players = [player_1, player_2] # Defines a list of players
scores = {player_1: 0, player_2: 0} # Initializes an empty dictionary to store scores

max_guess_attempted = 3  
wrong_guesses = {player_1: 0, player_2: 0} # A dictionary to store wrong guess count for each player 
word_guessed = False # Initializes a boolean variable to track if a word is guessed 
guessed_letters = set() # Initializes an empty set to store guessed letters

print("Welcome to the Word Guessing Game!\n")

while player_1 and player_2 and not word_guessed: # Ensures that the loop continues as long as both players have not reached the maximum wrong guesses.
    for player in players:
        if word_guessed:  # If the word is guessed exit the loop
            break
        print(f"Guess a letter, {player}: ") # Tells players to guess a letter 
        guess = input().lower() # Capture the player's input and converts it to lowercase 

        if len(guess) == 1:  # If the guess is a single letter
            if guess in '' .join(secret_word).lower(): # Joins the words in secret_word and converts them to lowercase
                count = '' .join (secret_word).lower().count(guess) # Counts how many occurences of that letter are in the secret word anrd convert it to lowercase
                print(f"Good job, that letter '{guess}' appears {count} times!")
                guessed_letters.add(guess) # Adds the guessed letters to the set of guessed letters 
                scores[player] += 1 # Increment the score for the player 
            else: 
                print("Wrong guess")
                wrong_guesses[player] += 1
        else: # If the guess is a word
            if guess.lower() in secret_word:
                print(f"{player} guessed the word '{guess}'!")
                word_guessed = True # Set word_guessed to True to end the game
                scores[player] += 5
                break
            else:
                print("Wrong guess")
                wrong_guesses[player] += 1

        if guessed_letters == set(''.join(secret_word).lower()):  # Check if all letters have been guessed
            print(f"{player} guessed the word!") 
            word_guessed = True  # Set word_guessed to True to end the game

        if wrong_guesses[player] >= max_guess_attempted:
            print(f"{player} reached {max_guess_attempted} wrong guesses. Game Over!")
            if player == player_1:
                player_1 = False # Set player 1 to false to indicate game over for player 1 
            else:
                player_2 = False # Set player 2 to false to indicate game over for player 2
   

print("Final Scores:")
for player, score in scores.items():
    print(f"{player}: {score}")

winner = max(scores, key = scores.get) 
print(f"{winner} wins!") # Annouces the winner

players = list(scores.keys())
scores_values = list(scores.values())

plt.bar(players, scores_values)
plt.xlabel('Players')
plt.ylabel('Scores')
plt.title('Final Scores of Word Guessing Gane')
plt.show()

game_stats = pd.DataFrame(columns = ['Players', 'Scores', 'Wrong Guesses']) # Create DataFrame to store game statistics 
game_stats.to_csv('game_statistics.csv', index = False ) # Save the game statistics to a CSV file



