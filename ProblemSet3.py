# -*- coding: utf-8 -*-

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    x = list(secretWord)
    if set(x).issubset(lettersGuessed) == True:
        return True
    else:
        return False
            
--------------------------------------------------------------------------------------

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    m = []
    sel_word = list(secretWord)
    for l in sel_word:
        if l in lettersGuessed:
            m.append(l)
        else:
            m.append('_')
            m.append(' ')
    res = ''.join(m)        
    return res

---------------------------------------------------------------------------------------

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    sel_word = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 
    m = []
    for l in sel_word:
        if l not in lettersGuessed:
            m.append(l)
    res = ''.join(m)        
    return res
        
----------------------------------------------------------------------------------------

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long")
    lettersGuessed = []
    n = 8
    while n != 0:
        print("-----------")
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print("Congratulations, you won!")
            break
        print ("You have " + str(n) + " guesses left")
        print("Available Letters: " + str(getAvailableLetters(lettersGuessed)))
        x = str(input("Please guess a letter: "))
        if x not in getAvailableLetters(lettersGuessed):
            print("Oops! You've already guessed that letter: " + str(getGuessedWord(secretWord, lettersGuessed)))
            continue
        if x in secretWord:
            lettersGuessed.append(x)
            print("Good guess: " + str(getGuessedWord(secretWord, lettersGuessed)))
        else:
            print("Oops! That letter is not in my word: " + str(getGuessedWord(secretWord, lettersGuessed)))
            n -= 1  
            lettersGuessed.append(x)
        if n == 0:
            print("-----------")
            print("Sorry, you ran out of guesses. The word was " + str(secretWord) + '.')
            break


