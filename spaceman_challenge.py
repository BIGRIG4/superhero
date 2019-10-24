import random

def load_word():
        f = open('words.txt', 'r')
        words_list = f.readlines()
        f.close()

        words_list = words_list[0].split(' ')
        secret_word = random.choice(words_list)
        return secret_word

def is_word_guessed(secret_word, letters_guessed):

    for letter in secret_word:
        if letter not in letters_guessed:
            return False

    return True




def get_guessed_word(secret_word, letters_guessed):

    for letter in secret_word:
        if letter in letters_guessed :
            display += (letter+ " ")
        else:
            display += "_ "

    return display



def is_guess_in_word(guess, secret_word):

    if guess in secret_word:
        print ('GREAT! That is correct')
        is_guess_in_word = True
    else:
        print ('That is WRONG! try again')
        is_guess_in_word = False
    return is_guess_in_word





def spaceman(secret_word):

    letters_guessed = list()
    numberofguess = 7


    print((f'Welcome to Spaceman bruhhhh! I am thinking of a word that is {len(secret_word)} letters long.'))

    running = True
    while running:
        print(f'You have {numberofguess} guesses left')
        print(get_guessed_word(secret_word, letters_guessed))
        guess=(input('Please guess a letter: '))
        guess = guess.lower()

        if guess in letters_guessed:
            print('Letter has already been guessed, guess a new letter')
        else:
            if is_guess_in_word(guess,secret_word) is False: #Have to place the parenthesis anytime you're calling a function
                numberofguess -= 1
                print('result came back false')
            else:

                print('result came back true')
                print(numberofguess)
                letters_guessed.append(guess)


        is_guess_in_word(guess, secret_word)
        print (get_guessed_word(secret_word,letters_guessed))

        result = is_word_guessed(secret_word, letters_guessed)
        if result == True:
            print('YOU WON!')
            break
        if numberofguess == 0:
            print('GAME OVER!The word was', secret_word)
            break

def play_again():
    guess=(input('Play Again?(Y/N'))
    guess = guess.lower()
    if guess == 'y':
        return True
    else:
        return False

if  __name__== '__main__':
    secret_word = load_word()
    print(secret_word)
    spaceman(secret_word)

    while play_again():
        secret_word = load_word()
        print(secret_word)
        spaceman(secret_word)
