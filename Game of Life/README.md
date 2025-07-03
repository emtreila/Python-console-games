# 🧬 Game of Life
The **Game of Life** is a cellular automaton developped by John Conway in 1970. This is a **zero-player game**, meaning that it is a simulation that given an initial configuration, runs by itself and requires no user input. 
One interacts with the game by creating a configuration and observing how it evolves. The simulation takes place on a 8x8 grid of cells, each of which is either alive **(an X)** or dead **(empty square)**

## 📌 RULES
At each step in time, the following transitions occur:
1. Any live cell with **fewer than 2 live neighbors** dies (under-population).
2. Any live cell with **2 or 3 live neighbors** survives.
3. Any live cell with **more than 3 live neighbors** dies (over-population).
4. Any dead cell with **exactly 3 live neighbors** becomes a live cell (reproduction).

❗ Neighbors include adjacent cells (row, column, diagonal). Each generation is created by applying the rules above simultaneously on every cell of the previous generation.

- When started, the program displays the initially empty grid of 8x8 cells.
- The program stores cell patterns in a read-only text-file. Any pattern can be added to the grid at any time.
Users can place a pattern using the following command: *place <pattern> <x>,<y>* (e.g. place blinker 2,2 places a blinker with upper left corner at position 2,2);  
a. This adds the shape on the board, with *<x,y>* specifying its upper left corner.  
b. Live cells from a pattern cannot be outside the board and cannot overlap other live cells.
- New generations are created using the *tick [n]* command (e.g. tick 99 advances the state with 99 generations).  
This updates the cell grid. *[n]* is an optional parameter with default value 1.
- The current simulation state can be saved to a file at any time using the *save filename* command. A simulation can be loaded from a previously saved file using the *load filename* command. After loading, the simulation can be continued.

