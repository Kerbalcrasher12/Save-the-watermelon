# Problem Statement & Target Audience
This game is a simple word guessing game where the player tries to guess a hidden word one letter at a time. Each incorrect guess removes a slice of the watermelon. It is designed for casual players who enjoy quick puzzle games.

 Game Rules & Win/Lose Conditions
 The player starts with 6 slices
 A random word is selected from a list
 The word is displayed as underscores, with each letter representing an underscore
 The player guesses one letter at a time
 If the guess is correct, any instance of the letter is revealed
 If the guess is incorrect, the player loses one slice

 Win condition: All letters are revealed before slices reach 0  
 Lose condition: Slices reach 0 before the word is guessed

# Core Features 
 Randomly select a word from the list
 Masked word shown to player
 Player guesses letters; correct guesses reveal letters
 Incorrect guesses make player lose slices
 When all slices are lost, the player loses
 When player guesses the word with more than 0 slices, they win

# Stretch Goals
 ASCII art stages
 Difficulty levels
 Hints
 Word categories
 Scoreboard

# Basic Flow
 start → loop guess → win/lose

 # Data Design
 word (string): the secret word, selected at random
 guessed_letters (set): letters the player has guessed
 slices_left (int): remaining lives
 MAX_SLICES (int): starting number of lives

# Modules / Function Responsiiblities
 words.py: provides random word
 logic.py: contains all rules and calculations, defines various functions
 mask_word(): shows current progress
 process_guess(): checks correctness
 word_guessed(): checks win condition
 game.py: runs the game loop and handles input/output
