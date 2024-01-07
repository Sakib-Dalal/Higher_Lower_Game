# Higher Lower Game

Welcome to the Higher Lower Game! This Python script lets you guess which Instagram account has more followers between two randomly chosen profiles. The game displays information about each profile, and your goal is to determine which one has the higher number of followers.


## How to Play

1. Run the `main.py` script.
2. Compare two profiles presented to you.
3. Enter 'A' if you think the first profile has more followers, or 'B' if you think the second one has more.
4. The game will inform you if your guess is correct, and you can continue playing.

## Features

- Randomly selects Instagram profiles for comparison.
- Displays information about each profile, including name, description, and country of origin.
- Keeps track of your score as you play.

## Art

The ASCII art logos for the game and the versus comparison are stored in `art.py` and enhance the visual appeal of the game.

```python
# art.py
logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

```

## How to Run

1. Clone the repository to your local machine:

    ```bash
    git clone git@github.com:Sakib-Dalal/Higher_Lower_Game.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Higher_Lower_Game
    ```

3. Run the main script:

    ```bash
    python main.py
    ```

## Game Data

The data for Instagram profiles is stored in `gamedata.py`, containing information such as the name, follower count, description, and country of origin.


---

*This project is developed by Sakib Dalal. For more details, please visit the [GitHub repository](git@github.com:Sakib-Dalal/Higher_Lower_Game.git).*
