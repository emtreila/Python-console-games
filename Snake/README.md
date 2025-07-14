# 🐍 Snake

A console-based implementation of the classic Snake game. The game is played on a square grid, where the player controls the snake and aims to eat apples to grow longer, avoiding collisions with itself or the walls.

## 📌 GAME MECHANICS

### 1. Game Initialization
- The game is played on an **N x N** board (read from a settings file).
- The board includes:
  - A snake: 
    - Head = `*`  
    - Body segments = `+`
  - Apples = `a`
- The snake starts in the middle of the board (length = 3: 1 head + 2 body).
- Apples are placed randomly with the following rules:
  - No apple overlaps the snake
  - No two apples are adjacent vertically or horizontally
- The number of apples is also read from the settings file

### 2. Commands & Gameplay
The player can use the following commands:

#### ➤ `move [n]`
- Moves the snake forward `n` steps in its current direction
- If `n` is omitted, the snake moves 1 step  

#### ➤ `up | down | left | right`
- Changes the snake’s direction
- Snake **cannot reverse 180°** (e.g. up → down)  
 

### 3. Eating Apples
- If the snake's head reaches an apple:
  - The snake **grows by 1 segment**
  - A new apple is added elsewhere (respecting placement rules)  

### 4. Game Over
The game ends if:
- The snake hits the edge of the board
- The snake collides with itself  

