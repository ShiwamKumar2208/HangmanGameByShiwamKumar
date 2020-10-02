import pyttsx3
import random
import time

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Initial Steps to invite in the game:
def intro():
    print("\nWelcome to Hangman game by Shiwam Kumar\n")
    speak("Welcome to Hangman game by Shiwam Kumar")
    print("Hello, I am hangman of this game")
    speak("Hello, I am hangman of this game")
    speak("plz enter your name")
    name = input("Enter your name: ")
    print("Hello " + name + "! Best of Luck!")
    speak("hello " + name + "! best of luck!")
    time.sleep(2)
    print("The game is about to start!\n Let's play Hangman!")
    speak("The game is about to start!. Let's play Hangman!")
    time.sleep(3)


# The parameters we require to execute the game:
def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess = ["january","border","image","film","promise","kids","lungs","doll","rhyme","damage"
                   ,"plants"]
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ""

# A loop to re-execute the game when the first round ends:

def play_loop():
    global play_game
    play_game = input("Do You want to play again? y = yes, n = no \n")
    speak("do you want to play again")
    while play_game not in ["y", "n","Y","N"]:
        play_game = input("Do You want to play again? y = yes, n = no \n")
    if play_game == "y":
        main()
    elif play_game == "n":
        print("Thanks For Playing! We expect you back again!")
        speak("Thanks For Playing! We expect you back again!")
        exit()

# Initializing all the conditions required for the game:
def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 10
    guess = input("This is the Hangman Word: " + display + " Enter your guess: \n")
    speak("This is the Hangman Word Enter your guess")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid Input, Try a letter\n")
        speak("Invalid Input, Try a letter")
        hangman()


    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")

    elif guess in already_guessed:
        print("Try another letter.\n")
        speak("try another letter")

    else:
        count += 1

        if count == 1:
            time.sleep(1)
            print("  |  \n"
                  "__|__\n")
            print("The stand for hanging started building")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
            speak("Wrong guess, The stand for hanging started building")

        
        elif count == 2:
            time.sleep(1)
            print("  |  \n"
                  "  |  \n"
                  "  |  \n"
                  "__|__\n")
            print("The stand for hanging is getting ready")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
            speak("wrong guess, The stand for hanging is getting ready")

        elif count == 3:
            time.sleep(1)
            print("  |  \n"
                  "  |  \n"
                  "  |  \n"
                  "  |  \n"
                  "__|__\n")
            print("The stand for hanging is getting ready")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
            speak("wrong guess, The stand for hanging is getting ready")

        elif count == 4:
            time.sleep(1)
            print("  |  \n"
                  "  |  \n"
                  "  |  \n"
                  "  |  \n"
                  "  |  \n"
                  "__|__\n")
            print("The stand for hanging is getting ready")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
            speak("wrong guess, The stand for hanging is getting ready")

        elif count == 5:
            time.sleep(1)
            print("   __\n"
                  "  |  \n"
                  "  |  \n"
                  "  |  \n"
                  "  |  \n"
                  "  |  \n"
                  "  |  \n"
                  "__|__\n")
            print("The stand for hanging is getting ready")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
            speak("wrong guess, The stand for hanging is getting ready")


        elif count == 6:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
            speak("wrong guess, The stand for hanging is getting ready")

        elif count == 7:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
            speak("wrong guess, The stand for hanging is getting ready")

        elif count == 8:
           time.sleep(1)
           print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     | \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
           print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
           speak("wrong guess, The stand for hanging is getting ready")

        elif count == 9:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "__|____/_\___ \n")
            print("Wrong guess. You are just hanged")
            print("Wrong guess. " + str(limit - count) + " last guess remaining\n")
            speak("wrong guess, you are just hanged")

        elif count == 10:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "  |        s\n"
                  "__|________\n")
            print("Wrong guess. You are hanged!!!\n")
            print("The word was:",already_guessed,word)
            speak("wrong guess, you are hanged!!!")
            play_loop()

    if word == '_' * length:
        print("Congrats! You have guessed the word correctly!")
        speak("congrats, You have guessed the word correctly!")
        play_loop()

    elif count != limit:
        hangman()

if __name__ == "__main__":
    intro()
    main()
    hangman()