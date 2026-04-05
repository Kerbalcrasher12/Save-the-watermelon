FUNCTION main_game_loop
    word ← get_random_word()
    guessed_letters ← ∅
    slices ← MAX_SLICES

    WHILE slices > 0 AND word is not fully guessed
        DISPLAY hidden version of word
        DISPLAY remaining slices
        guess ← ask user for input        
        IF guess already in guessed_letters THEN
            DISPLAY "Already guessed"
            CONTINUE
        ENDIF
        ADD guess to guessed_letters
        IF guess is in word THEN
            DISPLAY "Correct"
        ELSE
            slices = slices - 1
            DISPLAY "Incorrect"
        ENDIF
    ENDWHILE

    IF word is fully guessed THEN
        DISPLAY "The watermelon is saved!"
    ELSE
        DISPLAY "The watermelon is not saved!"
    ENDIF
END FUNCTION
