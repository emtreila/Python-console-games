# 👽 Alien
Two alien ships threaten to destroy Earth’s open source software! The player controls the planet’s defences, and during each turn attacks one square where an alien ship might be hiding.
At the start of the game, Earth’s surroundings are displayed:

## 📌 RULES
- The game takes place on a 7x7 grid with marked rows (1-7) and columns (A-G) having the Earth (E) at the centre. 
- Exactly 8 asteroids (marked with *) are randomly placed, so they do not overlap the Earth, no 2 asteroids are adjacent to each other on row, column or diagonal.
- Two alien ships (marked with X) are placed randomly at 3 squares distance from the Earth (first or last row, or column).
- They do not overlap each other or an asteroid. The player cannot see the alien ships. 

*Each turn is played as follows:*
- fire <coordinate> (e.g. fire G1) = the player attacks a square. If the square contains an asteroid, or was already fired upon, the program displays an error message and the user can try again.
If the square contains an alien ship, it is destroyed and the user informed. If both alien ships are destroyed the game is won.
The square is marked using a minus sign and alien ships can no longer move there.
- Each ship teleports to an empty square at the same distance (50% probability) or 1 square closer to Earth (50% probability).
- If at least 1 alien ship is adjacent to the Earth the game is lost 
- cheat. = displays the playing grid, with remaining alien ships revealed

