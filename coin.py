import random

class Coin:

    # Set _side to none on creation
    def __init__(self):
        self._side: str = None

    # Randomly set _side based on two possible outcomes and return it
    def flip(self) -> str:
        outcomes = ["Heads", "Tails"]
        self.side = random.choice(outcomes)
        return self._side

    # Getter for _side
    @property
    def side(self):
        return self._side
    
    # Setter for _side that prevents it from being set to anything other than Heads or Tails
    @side.setter
    def side(self, side):
        if side == "Heads" or "Tails":
            self._side = side
        else:
            print("Invalid coin side. Coin must only have sides Heads and Tails.")