def mask_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])


def is_word_guessed(word, guessed_letters):
    return all(letter in guessed_letters for letter in word)


def process_guess(word, guess, guessed_letters):
    if guess in guessed_letters:
        return False, "Already guessed"

    guessed_letters.add(guess)

    if guess in word:
        return True, "Correct"
    else:
        return False, "Incorrect"
