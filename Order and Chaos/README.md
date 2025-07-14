# ⚔️ Order and Chaos 

This is a console-based implementation of the pen-and-paper strategy game **Order and Chaos**, played on a **6×6 board**.

Two players compete:
-  **Order** (computer): tries to create a line of 5 identical symbols (X or O)
-  **Chaos** (human): tries to prevent this until the board is full

Unlike traditional games, players **choose which symbol** (X or O) to place on each move.


## 📌 RULES 

### 1. Objective
- **Order wins** if 5 identical symbols (X or O) appear consecutively in a **row, column, or diagonal**
- **Chaos wins** if the entire board is filled and no such line exists

### 2. Turn-based Logic
- The board starts empty and is displayed when the game begins
- **Order (AI) always starts first**
- Players alternate turns, placing either X or O on any empty cell

##  AI Strategy (Order Player)
The computer uses the following decision logic:
a.  Always plays **valid moves**  
b.  If it can win with the next move, it will do so **[1.5p]**  
c.  Otherwise, it:
   - Picks the symbol (**X or O**) that appears **most frequently** on the board  
   - Chooses the position that has the **highest number of same-symbol neighbors**

##  Game End Conditions

- **Order Wins:** 5 symbols in a row, column or diagonal (after **any** move, including chaos') ✅  
- **Chaos Wins:** Board is **full** and no winning line exists ❌  


