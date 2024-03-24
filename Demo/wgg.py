import random

def word_choice():
    my_words = ["g","sy","game","tos"]
    word = random.choice(my_words).lower()
    return word

def guess_word(word, word_think):
    guess_word = ""
    for character in word:
        if character in word_think:
            guess_word = guess_word + character
        else:
            guess_word = guess_word + "*"
    return guess_word

def collect_alp(word):
    character_guess = []
    total_chances = int(len(word)+5)    
    print("The word you are guessing is " + str(len(word)) + " characters long")

    while True:
        if total_chances!=0:
            print(f"You are still left with {total_chances} chances")
            print("Word is : " + guess_word(word, character_guess))
            print("Letters guessed: " + str(character_guess))
            guessing = input("Guess is :").lower()[0]

            if guessing not in character_guess:
                character_guess.append(guessing)

            if guess_word(word, character_guess) == word:
                print("Hurray!!")
                print(f"Congrats You got the correct word and i.e {word}")   
                break
            else:
                total_chances = total_chances - 1
                if guessing in word:
                    print("You have entered the correct character" + guessing)
                else:
                    print(guessing + " is not in the word ") 

while True:
    word = word_choice()
    collect_alp(word)
    if input("Do you want to continue :").lower().startswith("n"):
        break