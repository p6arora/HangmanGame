'''
Hangman Game
The user needs to be able to input letter guesses.
A limit should also be set on how many guesses they can use.
Keep notifying the user of the remaining turns.

Text File for input

'''

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



def start_game(word):
    parts_drawn = 0
    letters_remaining = len(word)
    letters_guessed = []

    count = count_letters_in_word()

    display_word()

    # while loop till objects_drawn == 6 or letters_remaining == 0
    while (parts_drawn != 6 or letters_remaining == 0):

        # Ask user to enter letter
        letter = input("Guess a letter..."
        # TODO: put both letter and word in lowercase

        while letter in letters_guessed:
            letter = input("That letter has already been guessed. Try a new letter...")
            print("Letters Guessed: ", letters_guessed)

        # if right
        if letter in count:
            # See how many times letter has repeated
            # fill in letters at those index
            word.find(letter)

            letters_guessed.append(letter)
        # if wrong
        else:
            # Add a strike/draw an object on
            letters_guessed.append(letter)
            parts_drawn += 1
            print(letter, " was not in the word! Drawing a body part...")




        # display word
        display_word()

def display_word():
    print("filler")

def count_letters_in_word(word):
    print("filler")
    count = {}

    return count

def main():
    word = get_word()
    start_game(word)



if __name__=="__main__":
    main()