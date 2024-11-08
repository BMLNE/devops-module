from hangman_functions import get_word, get_letter, print_hangman, display_word

if __name__ == '__main__':

    print("Welcome to play Hangman")
    print("First Player,")

    #set a word to play
    word = get_word()

    print("Thank you for the word!")
    print ("Second Player can now start guessing")

    #set wrong and positive guesses to 0
    pos_tries = ""
    neg_tries = ""

    #player two is now starting to guess the word
    while len(neg_tries) < 9 and not all(letter in pos_tries for letter in word):
        #get a letter as guess
        guess = get_letter(pos_tries, neg_tries)

        #check the guess
        if guess in word:
            pos_tries += guess
        else:
            neg_tries += guess

        display_word(word, pos_tries)

        # Display the number of wrong guesses
        print_hangman(len(neg_tries))
        #print("Number of wrong guesses: ", len(neg_tries))
        #print("Wrong guessed letters: ", neg_tries)

    #print the winner
    print("The Game is over:")
    if len(neg_tries) < 9:
        print("Player 1 won")
    else:
        print("Player 2 won and guessed the right word")
