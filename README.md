# PyStarcraft

Python Wrapper for the Starcraft 2 API.

Dependencies: 'requests' Python module.

Usage Example:
```
from PyStarcraft import PySC2

game_api_key = "my_api_key"
my_user_token = "my_token"
sc2 = PySC2(game_api_key, token=my_user_token)

# Examples

userLadder = sc2.get_matches(3767888, 'Lazerhawk')
sc2_rewards = sc2.get_rewards()
sc2_achievements =  sc2.get_achievements

# Must have a Token:
seasonLadderInfo = sc2.get_ladderData(30)
ladderInfo = sc2.get_ladder(201490)
```
To register for an API key visit dev.battle.net

If you need a token use the API Docs for Community OAuth Profile API