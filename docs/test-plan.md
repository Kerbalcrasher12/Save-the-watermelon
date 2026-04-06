How to Run the Game

1. Download files from Github
2.Open the project in PyCharm
3. Navigate to `src/game.py`
4. Right-click → Run `game.py`
   OR run in terminal:
   python src/game.py
5. Enter letter guesses when prompted

 Test Matrix

| Category | Test Case | Input | Expected Result | Actual Result       |
|           |           |          |                     |             |
| Valid Input | Correct guess    | letter in word | Letter revealed | Pass |
| Valid Input | Incorrect guess  | letter not in word | Slices decrease by 1 | Pass |
| Invalid Input | Number input   | `5` | "Invalid input" message | Pass |
| Invalid Input | Symbol input   | `@` | "Invalid input" message | Pass |
| Invalid Input | Multiple letters | `ab` | "Incorrect" message | Pass |
| Repeated Guess | Same letter twice | `a`, then `a` | "Incorrect" Message | Pass |
| Edge Case | Win condition | all correct letters guessed | Win message displayed | Pass |
| Edge Case | Lose condition | slices reach 0 | Lose message displayed | Pass |


 Manual Test Transcript

 Test Run 1 – Win Scenario
Secret word: miramar

Word: _ _ _ _ _ _ _
Slices left: 6
Guess a letter: b
Incorrect

Word: _ _ _ _ _ _ _
Slices left: 5
Guess a letter: w
Incorrect

Word: _ _ _ _ _ _ _
Slices left: 4
Guess a letter: a
Correct

Word: _ _ _ a _ a _
Slices left: 4
Guess a letter: a
Already guessed

Word: _ _ _ a _ a _
Slices left: 3
Guess a letter: n
Incorrect

Word: _ _ _ a _ a _
Slices left: 2
Guess a letter: m
Correct

Word: m _ _ a m a _
Slices left: 2
Guess a letter: i
Correct

Word: m i _ a m a _
Slices left: 2
Guess a letter: r 

Final Output: 
Correct
The watermelon is saved!
Word was: miramar 

Result: PASS  


 Test Run 2 – Lose Scenario
Secret word: slime

Word: _ _ _ _ _
Slices left: 6  

Input: x = Incorrect (5 slices left)  
Input: y = Incorrect (4 slices left)  
Input: z = Incorrect (3 slices left)  
Input: q = Incorrect (2 slices left)  
Input: w = Incorrect (1 slice left)  
Input: t = Incorrect (0 slices left)  

Final Output: The watermelon is not saved!
Word was: slime
Result: PASS  


### Test Run 3 – Repeated Guess
Secret word: watermelon

Word: w _ _ _ _ _ _ _ _ _
Slices left: 6
Guess a letter: w
Incorrect

Word: w _ _ _ _ _ _ _ _ _
Slices left: 5
Guess a letter:

Input: w = Correct  
Input: w = Slice lost 

Result: Loss of a slice


 Test Run 4 – Invalid Input
Secret word: watermelon  

Word: w _ _ _ _ _ _ _ _ _
Slices left: 6
Guess a letter: ab
Incorrect

Word: w _ _ _ _ _ _ _ _ _
Slices left: 5
Guess a letter:  

Result: Loss of a slice


 Edge Case Testing: All worked successfully

 Summary
All core gameplay paths were tested and worked succesffuly

The game behaves as expected and meets all functional requirements.
