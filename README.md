# Higher Lower Game

Welcome to the Higher Lower Game! Test your knowledge of social media follower counts in this interactive guessing game. Compare two profiles, guess which one has a higher follower count, and see how many correct guesses you can make in a row.

## Author

This code is authored by Sakib Dalal.

## Features

- Interactive guessing game
- Compare social media profiles
- Randomly selected profiles for each round

## Usage

1. Run the `main.py` script.
2. Compare two profiles and guess which one has a higher follower count.
3. See if your guess is correct.
4. Continue playing and try to achieve the highest score.

## Art

The ASCII art logos enhance the visual appeal of the game and are stored in `art.py`.

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

The data for the profiles is stored in `gamedata.py`. Each profile includes the name, follower count, description, and country of origin.

```python
# gamedata.py
data = [
    # ... (list of profiles)
]
```


---

*This project is developed by Sakib Dalal. For more details, please visit the [GitHub repository](git@github.com:Sakib-Dalal/Higher_Lower_Game.git).*
