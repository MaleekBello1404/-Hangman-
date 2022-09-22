import random
from replit import clear

from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#Imported the logo from hangman_art.py and print it at the start of the game.
from hangman_art import logo, stages

print(logo)

#Create blanks
display = []
for _ in range(word_length):
    display.append("_")

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()

    # If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You've already guessed {guess}")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        # If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        if guess not in chosen_word:
            print(
                f"You guessed {guess}, That's not in the word. You lose a life."
            )
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You lose. The right answer is {chosen_word}")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # Import the stages from hangman_art.py and make this error go away.
    print(stages[lives])
