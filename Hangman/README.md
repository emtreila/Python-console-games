# 🎯 Hangman

This is a console-based version of the classic **Hangman** game with a twist: instead of guessing a single word, you must guess **entire sentences**, one letter at a time!

Each incorrect guess adds a letter to the word **"hangman"**, and the game ends when:
- You guess the sentence correctly ✅
- Or the word **hangman** is fully spelled ❌

## 📌 RULES 

### 1. 📝 Add Sentences
- Before starting a game, you can add new sentences to the database.
- Each sentence must:
  - Contain at least **1 word**
  - All words must have at least **3 letters**
  - **No duplicate sentences** allowed  
- Sentences are saved/loaded from `sentences.txt`  

### 2. ▶️ Start the Game
- The computer selects a **random** sentence from the list 
- Displays only the:
  - First and last letter of each word
  - All occurrences of those letters  
  **Example:**  
  For `"anna has apples"`  
  → `a _ _ a   h _ _   a _ _ _ _ s`  

### 3. 🎮 Play Rounds
- In each round, you guess a letter:
  - If the letter is in the sentence → it is revealed in all positions
  - If not → a letter is added to `"hangman"`  
- Already guessed letters count as incorrect
- Game continues until:
  - Sentence is complete (YOU WIN 🎉)
  - `"hangman"` is complete (YOU LOSE 💀)  


