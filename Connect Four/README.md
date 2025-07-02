# 🔴🟡 Connect Four
Connect Four is a classic two-player game recreated in the Python console. You face off against the computer in a battle of strategy and positioning—drop your discs into columns, and try to connect four in a row before the computer does!

## 📌 RULES
- The game is played on a **6-row x 7-column** grid.
- You are player **1** (represented with 🟡), the computer is player **2** (represented with 🔴).
- Players take turns dropping one disc into any column that is not full.
- The disc falls to the **lowest available space** in the column.
- The first player to **connect four discs in a row** (horizontally, vertically, or diagonally) **wins the game** 🎉.
- If the board is completely filled and no one has won, the game ends in a **tie** ⚖️.

## 🖥️ COMPUTER STRATEGY
Each computer turn:
- Tries to win immediately by placing the fourth disc.
- If not possible, blocks the player's potential winning move.
- If no immediate threat, chooses a **random valid column** to move.
