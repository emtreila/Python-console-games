# 🔀 Scramble – Letter Swapping Puzzle Game

**Scramble** is a console-based game where the goal is to **unscramble words in a sentence** by swapping the positions of letters - one pair at a time. The first and last letter of each word remain fixed, while the inner letters are shuffled randomly at the beginning.

## 📌 RULES 

### 1. Start a New Game
- A sentence or word is randomly selected from an input file
- Each word is scrambled by:
  - Keeping the **first and last letter** in place
  - Shuffling the **inner letters** (including across words)
- The initial **score** is the number of letters (excluding spaces)  
- The scrambled sentence is shown to the player 

 Example:  
Original: Dream without fear
Scrambled: Doahm wueirtt fear
Score: 16


### 2. Swap Letters

Use the command: swap <word1> <letter1> - <word2> <letter2>
- This swaps two letters at the specified positions
- After each swap:
  - The updated sentence is printed 
  - The score decreases by 1 
- Invalid commands or out-of-range indices show an error 
 Example:  
swap 0 1 - 0 3  
Swaps 2nd and 4th letters of the first word (`salc**m**bre → sclambre`)

### 3. Undo Swap
- You can undo the **last swap operation**
- This does **not affect the score** 

### 4. Game End Conditions
The game ends when:
- All words are restored to their **original form** (**Victory!**)   
- The score reaches **0** (**Defeat**)    
