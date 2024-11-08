
def get_word():
    while True:
        word = input("Please enter a word: ").strip().lower()
        if len(word) >= 2 and word.isalpha():
                return word
        else:
            print("Invalid input. Please enter a single word.")

def get_letter(pos_tries, neg_tries):
    while True:
        letter = input("Please enter a letter: ").strip().lower()
        if len(letter) == 1 and letter.isalpha():
            if letter not in pos_tries and letter not in neg_tries:
                return letter
            else:
                print("You aready guessed this letter. Please try again")
        else:
            print("Invalid input. Please enter a single letter.")

# Display the current state of the word with correctly guessed letters
def display_word(word, pos_tries):
    display = ""
    for letter in word:
        if letter in pos_tries:
            display += letter + " "
        else:
            display += "_ "
    print(display.strip())


# Define the stages of the hangman ASCII art
def print_hangman(incorrect_guesses):
    stages = [
            # Start:
            """






            ====
            """,
            # St
            # Stage 0: Post (upside-down "L")
            """
             +---+
             |   
             |   
             |   
             |   
             |   
            ====
            """,
            # Stage 1: Head (circle)
            """
             +---+
             |   |
             |   
             |   
             |   
             |   
            ====
            """,
            # Stage 1: Head (circle)
            """
             +---+
             |   |
             |   O
             |   
             |   
             |   
            ====
            """,
            # Stage 2: Back (straight line from the head downwards)
            """
             +---+
             |   |
             |   O
             |   I
             |   
             |   
            ====
            """,
            # Stage 3: One arm
            """
             +---+
             |   |
             |  \O
             |   I
             |   
             |   
            ====
            """,
            # Stage 4: Second arm
            """
             +---+
             |   |
             |  \O/
             |   I
             |   
             |   
            ====
            """,
            # Stage 5: One leg
            """
             +---+
             |   |
             |  \O/
             |   I
             |  /
             |   
            ====
            """,
            # Stage 6: Second leg
            """
             +---+
             |   |
             |  \O/
             |   I
             |  / \
             |   
            ====
            """
        ]
    # Print the current stage based on the number of incorrect guesses
    print(stages[min(incorrect_guesses, len(stages))])