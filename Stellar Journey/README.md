# 🚀 Stellar Journey – USS Endeavour Mission

**Stellar Journey** is a console-based space exploration game where the player controls the **USS Endeavour** on a mission to eliminate all **Blingon** enemy ships from a sector of the galaxy.

The game is played on an 8x8 grid and progresses in multiple turns.

## 📌 RULES

### 1. Sector Setup (at Game Start)

- The game board is an **8x8 grid**, with:
  - Columns labeled `1-8`
  - Rows labeled `A-H`  

- **10 stars (`*`)** are randomly placed on the board. Rules:
  - No two stars overlap
  - No two stars are adjacent (horizontally, vertically, or diagonally)  

- The **USS Endeavour** (`E`) is placed randomly in a square that:
  - Has no star
  - Is not adjacent to any star  

- **3 Blingon ships (`B`)** are randomly placed in **empty** squares, **not adjacent to each other**, stars, or the player's ship  

- The player can only see **ships adjacent** to the USS Endeavour  
 

##  GAMEPLAY COMMANDS

Each turn, the player enters a command:

### `warp <coordinate>`
- Moves the ship to the new coordinate (e.g., `warp G5`)
- The new position must be on the same **row, column, or diagonal**
- Cannot move through or onto a **star**
- If you try to warp onto a **Blingon ship**, the **game is lost**  
- Invalid or blocked moves display an error and do not move the ship  

### `fire <coordinate>`
- Attacks the specified coordinate (e.g., `fire B4`)
- Can only fire at **squares adjacent** to the ship
- Valid hits destroy Blingon ships  
- Invalid coordinates or non-adjacent attacks trigger an error  

### `cheat`
- Reveals the entire map including remaining Blingon ships  

### Enemy Behavior
- Every time a **Blingon ship is destroyed**, the remaining ships:
  - **Reposition randomly** to valid positions, preserving the initial constraints  

### Victory & Defeat

- The player **wins** if all 3 Blingon ships are destroyed  
- The player **loses** if:
  - The ship warps into a Blingon position
  - A command is invalid and results in destruction  
