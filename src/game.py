from words import get_random_word
from logic import mask_word, word_guessed, process_guess

MAX_SLICES = 6

def play():
    word = get_random_word()
    guessed_letters = set()
    slices_left = MAX_SLICES
    print("Save the Watermelon!")

    while slices_left > 0:
        print("\nWord:", mask_word(word, guessed_letters))
        print(f"Slices left: {slices_left}")
        guess = input("Guess a letter: ").lower()
        correct, message = process_guess(word, guess, guessed_letters)
        print(message)
        if not correct:
            slices_left -= 1
        if word_guessed(word, guessed_letters):
            print("The watermelon is saved!")
            print("Word was:", word)
            return
    print("The watermelon is not saved!")
    print("Word was:", word)

if __name__ == "__main__":
    play()
