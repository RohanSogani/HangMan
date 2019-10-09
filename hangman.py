import time
import json
import random

with open("Words.json") as wordFile:
    dataSource = json.load(wordFile)

name = input("What is your name? ")

print("Hello, " + name +" time to play new Hangman!!")

time.sleep(1);

print("Start Guessing....")
time.sleep(0.5)

play = 1;
while play == 1:
    word = random.choice(dataSource["data"])
    guesses = ""
    turns = 7
    while turns > 0:
        failed = 0
        for char in word:
            if char in guesses:
                print (char, end=" ")
            else:
                print ("_", end=" ")
                failed += 1
        if failed == 0:
            print("You Won")
            break

        print("You have", turns, "turns", end=" ")
        guess = input("Guess a character --> ")

        guesses += guess

        if(guess not in word):
            turns -= 1
            print("Wrong")
            print("You have ", +turns, " more guesses")
            if(turns == 0):
                print("You loose :'(")
                print("The word was", word)
                playKey = ''
                while 1:
                    playKey = input("Do you still want to continue? [Y/N]");
                    if playKey == 'Y' or playKey == 'y':
                        play = 1
                        break
                    elif playKey == 'N' or playKey == 'n':
                        play = 0
                        print("Bye")
                        break
                    else:
                        print("Invalid input")
