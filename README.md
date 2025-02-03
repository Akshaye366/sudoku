
# Sudoku Game

Welcome to the **Sudoku Game**! This is a fully-featured implementation of the classic Sudoku puzzle game built using **Python** and **Pygame**. The game includes a variety of features designed to enhance user experience, including a customizable difficulty system, a timer, hints, and a user statistics tracker.

### Features
- **Custom Difficulty Levels**: Choose from different difficulty levels that affect the initial puzzle setup and the number of clues.
- **Timer**: Keep track of your time while solving the puzzle. The timer resets at the beginning of each game and counts down to zero.
- **Hints**: Use a limited number of hints to reveal a random empty cell’s correct value if you're stuck.
- **Mistake Tracker**: The game tracks the number of mistakes you've made while filling in the puzzle.
- **Undo Functionality**: Mistaken entries can be undone, allowing for greater flexibility.
- **Pause Functionality**: You can pause the game at any time to take a break.
- **Statistics and Leaderboards**: Your performance is tracked across multiple games, including time taken, number of mistakes, and hints used. These statistics are stored in a database and can be accessed at any time.
- **Interactive Grid**: The game’s grid is drawn in the center of the screen, and you can navigate through the cells using keyboard arrow keys or `W`, `A`, `S`, `D`.
- **Graphing**: The game records and updates user data, generating stats like the number of easy solves and total hints used.

### How to Play
1. **Start a New Game**: Click on any empty cell and start filling it with numbers (1-9).
2. **Check your Work**: If a number is incorrect, it will be highlighted in red. If correct, it will turn green.
3. **Use Hints**: If you’re stuck, use one of your hints to reveal a correct number in an empty cell.
4. **Complete the Puzzle**: Complete the puzzle by correctly filling in all the cells. The game will display your time, mistakes, and other relevant stats once you've finished.

### Setup and Installation

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/Akshaye366/sudoku.git
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the game:
   ```bash
   python main.py
   ```

### Technologies Used
- **Python 3**: The game is written in Python 3, leveraging its powerful libraries.
- **Pygame**: Used for creating the graphical user interface and managing the game loop.

### Customization
You can customize game settings like theme, difficulty, and number of hints by editing the configuration file or interacting with the settings interface.

---

### Important Notes

- **Pause Functionality**: The ability to pause the game is planned but has not yet been implemented. This feature will allow users to temporarily stop the game and resume where they left off.
  
- **Undo Button**: The undo functionality has been outlined but is not yet available in this version. When implemented, players will be able to undo the last entered number, providing flexibility and reducing frustration when mistakes are made.

Please stay tuned for updates, as these features will be added in the near future!

---

**Enjoy the game and try to finish the puzzle with the fewest mistakes and in the shortest time!**