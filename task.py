import random
import string

print("Hi! Welcome to the Hangman! \n This is a game between two players. \n Player1 chooses the word, "
      "while Player2 tries to guess it.\n")

random_word_collection = ['dinosaur', 'coffee', 'coke', 'water', 'book']
number_of_lives = 5
word_to_be_guessed = list(input("Player 1: Type in the word to be guessed.\n For a random word, type 0.\n"))
if word_to_be_guessed[0]=='0':
    word_to_be_guessed = list(random.choice(random_word_collection))
placeholder = ""
previous_guesses = []
max_points = len(word_to_be_guessed)
for letter in word_to_be_guessed:
    placeholder+= "_"
player_points = 0

print(f"{placeholder}\n\n------\n |    |\n      |\n      |\n      |\n=========\n")

display = list(placeholder)

i = 0
while number_of_lives!=0:
    guess = input(f"Player 2: what is your guess? (Guess {i})\n").lower()

    while guess in previous_guesses:
        print("You cant repeat guesses. \n Please try again!")
        guess = input(f"Player 2: what is your guess? (Guess {i})\n").lower()

    if guess in word_to_be_guessed:
        player_points=player_points+1
        print(f"You got it! POINTS: {player_points} MAX_POINTS: {max_points}")

        for index, letter in enumerate(word_to_be_guessed):
            if letter == guess:
                display[index] = letter

        if player_points == max_points or "_" not in display:
            print("Congratulations! \n You win!\n")
            break
    else:
        number_of_lives=number_of_lives-1
        print(f"That's a miss... \n {number_of_lives} lives left.")
        if number_of_lives==4:
            print("------\n |    |\n O    |\n      |\n      |\n=========\n")
        elif number_of_lives==3:
            print("------\n |    |\n O    |\n |    |\n      |\n=========\n")
        elif number_of_lives == 2:
            print("------\n |    |\n O    |\n/|    |\n      |\n=========\n")
        elif number_of_lives==1:
            print("------\n |    |\n O    |\n/|\\   |\n      |\n=========\n")

    i=i+1
    print("".join(display))
    previous_guesses.append(guess)

if number_of_lives == 0:
    print(f"What a shame... \n {number_of_lives} lives left. \n You lost!")
    print("------\n |    |\n O    |\n/|\\   |\n/ \\   |\n=========")