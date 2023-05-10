import random
import hangman_art, hangman_words

word_list = hangman_words.word_list
chosen_word = random.choice(word_list)

print(hangman_art.logo)

# Just for testing ...
print(f"The word is {chosen_word}")

display = ["_" for _ in chosen_word]
print(display)

lives = 6

guessed_letters = []

keep_playing = True

while keep_playing:
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print(f"You already guessed '{guess}'. Try again...")
        continue

    guessed_letters += guess

    if guess in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess
        if "_" not in display:
            keep_playing = False
            print("".join(display))
            print("You win")
    else:
        print(f"Your guess '{guess}' is not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            print("You lose")
            keep_playing = False

    print(hangman_art.stages[lives])
    print(display)



