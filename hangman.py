'''
Hangman Game
The user needs to be able to input letter guesses.
A limit should also be set on how many guesses they can use.
Keep notifying the user of the remaining turns.

Text File for input

'''
# TODO: make a graphic representation of handman
# TODO: Ask user to add word to list

import sys
import random

#read word from text-file
def get_word():
    f = open("word_master_list.txt", "r")

    if f.mode == "r":
        words = f.read()
        words = words.split(" ")
        index = generate_random_index(words);
        f.close()
        return words[index].lower()
        # TODO: add functionality to get word if its on the next line
    print("word not read")
    sys.exit()


# Generates a random index from 0 to the total number of words in the list
def generate_random_index(words):
    size = len(words)
    return random.randint(0, size - 1)



# Base Function for handling all logic of game
# keeps track of all parts drawn, letters ramaining, guessed and calls all helper functions
def start_game(word):
    parts_drawn = 0
    letters_remaining = len(word)
    letters_guessed = []

    count = count_letters_in_word(word)
    shown_word = "_ " * len(word)

    print(shown_word)

    # while loop till objects_drawn == 6 or letters_remaining ==
    while (parts_drawn != 6 and letters_remaining != 0):
        print("parts_drawn: ", parts_drawn)
        print("Letters Guessed: ", letters_guessed)



        # Ask user to enter letter
        letter = input("Guess a letter...")
        letter = letter.lower()

        # checks user input is acceptable
        validate_input(letter, letters_guessed)

        # evaluates what letter user entered - updates letters guessed, draws body part on hangman if wrong, updates shown word
        shown_word, letters_remaining, letters_guessed, parts_drawn = evaluate(letter, count, shown_word, word, letters_remaining, letters_guessed, parts_drawn)
        draw_hangman(parts_drawn)

        # display word
        print(shown_word)




    # end message - tells user if they won or lost and to play again
    end_message(parts_drawn, word)





'''
    Makes sure user's input is:
        1) A letter that's not been guessed before
        2) Is only a letter
        3) is only 1 character
'''
def validate_input(letter, letters_guessed):
    while letter in letters_guessed or not letter.isalpha() or len(letter) > 1:
        if letter in letters_guessed:
            print("That letter has been guessed")
        elif len(letter) > 1:
            print("Enter only 1 character!")
        else:
            print("Enter only a character")
        print("Letters Guessed: ", letters_guessed)
        letter = input("Try a new letter...")


# draws the hangman wrt how many wrong guesses user has made
def draw_hangman(parts_drawn):
    hangman = ''
    if parts_drawn == 1:
        hangman = ('''      
                        ---
                       |   |
                        ---
              ''')
        print(hangman)

    elif parts_drawn == 2:
        hangman = ('''
                        ---
                       |   |
                        ---
                         |
                         |
                    ''')
        print (hangman)
    elif parts_drawn == 3:
        hangman = ('''
                        ---
                       |   |
                        ---
                         |
                         |
                        / 
                       /   
                    ''')
        print(hangman)
    elif parts_drawn == 4:
        hangman = ('''
                        ---
                       |   |
                        ---
                         |
                         |
                        / \\
                       /   \\
                    ''')
        print(hangman)
    elif parts_drawn == 5:
        hangman = ('''
                        ---
                       |   |
                        ---
                         |---
                         |
                        / \\
                       /   \\
                    ''')
        print(hangman)
    elif parts_drawn == 6:
        hangman = ('''
                            ---
                           |   |
                            ---
                          ---|---
                             |
                            / \\
                           /   \\
                        ''')
        print(hangman)



# end message telling user if they won or lost
def end_message(parts_drawn, word):
    if parts_drawn == 6:
        print("You have lost...")
        print("Correct word was", word)
        play_again_message()
    else:
        print("You have won...")
        play_again_message()


# Invites user to play again or not
def play_again_message():
    ans = input("Play Again? y for Yes, n for No")
    if ans.lower().isalpha() and len(ans) == 1:
        if ans == "y":
            main()
        elif ans == 'n':
            sys.exit()
        else:
            print("Not valid response")
            sys.exit()




# creates a dictionary of how many times a letter is in the word
def count_letters_in_word(word):
    count = {}
    for l in word:
        if l in count:
            count[l] += 1
        else:
            count[l] = 1

    return count

# evaluates user response
def evaluate(letter, count, shown_word, word, letters_remaining, letters_guessed, parts_drawn):
    # if right
    if letter in count:
        # See how many times letter has repeated
        # fill in letters at those index
        occ = [pos for pos, char in enumerate(word) if char == letter]
        shown_word_list = list(shown_word)

        # checks the occurence list to see which index in shown word needs to be revealed
        for i in occ:
            shown_word_list[i * 2] = letter

        shown_word = ''.join(shown_word_list)
        print("Correct! " ,letter, " appears " ,len(occ), " times")
        # subtracts total blanks remaining from number of occurence of that letter
        letters_remaining -= len(occ)
        # adds letter to letters guessed
        letters_guessed.append(letter)
        return shown_word, letters_remaining, letters_guessed, parts_drawn

    # if wrong
    else:
        # Add a strike/draw an object on
        letters_guessed.append(letter)
        parts_drawn += 1
        print(letter, " was not in the word! Drawing a body part...")
        return shown_word, letters_remaining, letters_guessed, parts_drawn

def main():
    word = get_word()
    start_game(word)



if __name__=="__main__":
    main()