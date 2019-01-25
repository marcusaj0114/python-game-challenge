import random
def replay_game():
    play_again = input("Would you like to play again? ")
    if "Yes".lower() in play_again:
        play_game()
        
    else:
        exit(0)
        
        
def play_game():
    words = open('myenv/words.txt').read().split()
    word = random.choice(words).upper()
    correct_guesses = 0
    wrong_letters = ""
    correct_letters = ""
    num_guesses = len(word) * 2 - 2
    secret_word = word
    word_letters = word
    word_guessed = []
    for letter in secret_word:
        word_guessed.append(" - ")
        
    
    while num_guesses > 0 and correct_guesses < len(word):
        print("Word:", word_guessed)
        print("Guesses left:", num_guesses)
        print("Incorrect letters:", wrong_letters)
        guess = input("Guess a letter: ")
        if len(guess) != 1:
            print("Your guess can't contain more than one letter!")
            
        elif guess.upper().isalpha() == False:
            print("Your supposed to guess a letter!") 
            
        elif guess.upper() in wrong_letters:
            print("You can't guess the same letter twice!")
            
        elif guess.upper() in correct_letters:
            print("You can't guess the same letter twice!")
            
        elif guess.upper() in word_letters:
            print("Correct!")
            
            for letter in range(len(secret_word)):
                if guess.upper() == secret_word[letter]:
                    word_guessed[letter] = guess.upper()
                    correct_guesses += 1
            if correct_letters == "":
                correct_letters = guess.upper()
                
            else:
                correct_letters += guess.upper()
            
        elif guess.upper() not in word_letters:
            print("Incorrect!")
            num_guesses -= 1
            if wrong_letters == "":
                wrong_letters = guess.upper()
                
            else:
                wrong_letters += ", " + guess.upper()
                
    if num_guesses <= 0:
        print("Too bad! The word was", word)
        replay_game()
        
    else:
        print("Word:", word_guessed)
        print("Nice job! The word was", word)
        replay_game()
            
            
            
print("""
Welcome to Hangman.
Would you like me to explain the rules?""")
    
hear_rules = input("Yes or No: ")
if "Yes".lower() in hear_rules:
    print(""" We're going to play a game of Hangman.
    I'll think up a word, and you have a limited
    number of guesses to figure out what it is.
    The number of guesses you have is proportional
    to the difficulty of the word. If you run out of
    guesses and the word isn't filled out, you lose.
    Both capital and lowercase guesses are valid.
    Good luck and have fun!""")
        
    play_game()
    
else:
    if "No".lower() in hear_rules:
        play_game()