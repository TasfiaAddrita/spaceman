import random

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.

    Returns:
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.

    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns:
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed

    '''
    start:
        if placeholder text '_' is in user's guess,
            return false
        return true
    '''

    pass

def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.

    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns:
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet

    '''
    -----PSEUDOCODE-----
    start:
        loop through secret_word by index:
            if letters_guessed[len(letters_guessed)-1] == secret_word[index]:
                replace _ at index
                remove last letter from letters_guessed
                return letters_guessed
    '''

    pass


def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word

    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word

    Returns:
        bool: True if the guess is in the secret_word, False otherwise

    '''
    #TODO: check if the letter guess is in the secret word

    '''
    -----PSEUDOCODE-----
    start:
        if user's guess is in secret_word:
            return true
        else:
            return false
    '''

    pass




def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.

    Args:
      secret_word (string): the secret word to guess.
    '''

    #TODO: show the player information about the game according to the project spec
    #TODO: Ask the player to guess one letter per round and check that it is only one letter
    #TODO: Check if the guessed letter is in the secret or not and give the player feedback
    #TODO: show the guessed word so far
    #TODO: check if the game has been won or lost

    '''
    -----PSEUDOCODE-----
    start spaceman:
        welcome message
        list of user-letter-guesses, populate with '_'
        list/string of alphabet-letters
        create a variable to store user's decision to play
        while user wants to play:
            create a variable to store number-of-guesses available (either 0 or length of secret word)
            while number-of-guesses is less than the length secret word:
                get letter from user
                add letter user-letter-guesses
                remove letter from alphabet-letters
                FUNCTION: check if letter is in secret word
                    if true,
                        then print correct message
                        FUNCTION: update placeholder text # input: user-letter-guesses, returns list
                        FUNCTION: check if word is secret word:
                            if true, return winner message
                    if false,
                        then print incorrect message
                        decrement number of guesses available by 1
                    update letters available to guess
            return loser message
            ask user if user wants to play again
    '''




#These function calls that will start the game
# secret_word = load_word()
spaceman(load_word())
