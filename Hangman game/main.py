import random
from hangman_art import stages, logo
from hangman_words import word_list
#mathod that ask the player if he want a rematch
def rematch():
    again = True
    while again:
        option = int(input("1. Press 1 for reamtch\n2. Press 2 for exit"))
        if option == 1 or option == 2:
            if option == 1:
                return True
            else:
                print("Good bye")
                return False
        else:
            print("Please follow the orders!")        

start_game = True
while start_game:
    print(logo)
    game_is_finished = False
    lives = len(stages) - 1

    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)

    display = []
    for _ in range(word_length):
        display += "_"
    guess_list = []
    while not game_is_finished:
        guess_again = True
        while guess_again:
            guess = input("Guess a letter: ").lower()
            if len(guess) == 1:
                if ord(guess) > 122 or ord(guess) < 97:
                    print(f"This is not a leeter {guess}")
                elif guess in guess_list:
                    print(f"You've already guessed {guess}")
                else:    
                    guess_again = False
            else:
                print("Please enter only one letter!")    
        guess_list.append(guess)

        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
                print(f"{' '.join(display)}")

        if guess not in chosen_word:
            print(f"You guessed {guess}, that's not in the word. You lose a life.\n{' '.join(display)}")
            lives -= 1
            if lives == 0:
                game_is_finished = True
                print("You lose.")
                
    
        if not "_" in display:
            game_is_finished = True
            print("You win.")
            

        print(stages[lives])
        if game_is_finished:
            start_game = rematch()
