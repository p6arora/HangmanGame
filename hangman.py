'''
Hangman Game
The user needs to be able to input letter guesses.
A limit should also be set on how many guesses they can use.
Keep notifying the user of the remaining turns.

Text File for input

'''
# TODO: make a graphic representation of handman

# TODO: graphic blanks too close and not being overwritten

import sys

#read word from text-file
def get_word():
    f = open("word_master_list.txt", "r")

    if f.mode == "r":
        words = f.read()
        words = words.split(" ")
        return words[0]
        # TODO: add functionality to get word if it is a space as delimmiter or its next line
        # TODO: make it a random word
    return "DNE"



# TODO: need to break start_game into smaller functions
def start_game(word):
    parts_drawn = 0
    letters_remaining = len(word)
    letters_guessed = []

    count = count_letters_in_word(word)
    shown_word = " _ " * len(word)

    display_word(shown_word)

    # while loop till objects_drawn == 6 or letters_remaining == 0
    while (parts_drawn != 6 or letters_remaining == 0):
    # TODO: have to break out of letters_remaining max
    # TODO: not exiting game when you win

        # Ask user to enter letter
        letter = input("Guess a letter...")
        # TODO: put both letter and word in lowercase

        while letter in letters_guessed:
            letter = input("That letter has already been guessed. Try a new letter...")
            print("Letters Guessed: ", letters_guessed)

        # if right
        if letter in count:
            # See how many times letter has repeated
            # fill in letters at those index
            occ = [pos for pos, char in enumerate(word) if char == letter]
            shown_word_list = list(shown_word)

            for i in occ:
                shown_word_list[i] = letter

            shown_word = ''.join(shown_word_list)
            letters_remaining -= len(occ)
            letters_guessed.append(letter)
        # if wrong
        else:
            # Add a strike/draw an object on
            letters_guessed.append(letter)
            parts_drawn += 1
            print(letter, " was not in the word! Drawing a body part...")




        # display word
        display_word(shown_word)

    print("Game Over")
    sys.exit()


def display_word(shown_word):
    print (shown_word)

def count_letters_in_word(word):
    count = {}
    for l in word:
        if l in count:
            count[l] += 1
        else:
            count[l] = 1

    return count

def main():
    word = get_word()
    start_game(word)



if __name__=="__main__":
    main()