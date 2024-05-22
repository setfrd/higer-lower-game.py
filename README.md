# Higher Lower Game

This is a console-based implementation of the Higher Lower Game. The objective of the game is to guess which account has more followers on social media. The game continues until the player makes an incorrect guess.

## How to Play

1. The game will display two accounts and their details (name, description, and country).
2. The player is prompted to guess which account has more followers by typing 'A' or 'B'.
3. The game provides feedback on whether the guess was correct and displays the current score.
4. The game continues with the second account becoming the new first account, and a new second account is randomly selected.
5. The game repeats until the player guesses incorrectly.
6. The final score is displayed when the game ends.

## Getting Started

### Prerequisites

- Python 3.x
- `art.py` and `game_data.py` files in the same directory as `main.py`.

### Installing

1. Clone the repository or download the source code files.
2. Ensure you have the `art.py` and `game_data.py` files with the following content:

   **art.py:**

   ```python
   logo = """
     __  __
    |  \/  | __ _ _ __   __ _  ___
    | |\/| |/ _` | '_ \ / _` |/ _ \\
    | |  | | (_| | | | | (_| |  __/
    |_|  |_|\__,_|_| |_|\__, |\___|
                          |___/
   """

   vs = """
    _    __
   | |  / /____
   | | / / ___/
   | |/ (__  )
   |___/____(_)
   """
   ```
