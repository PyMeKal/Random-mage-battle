from Root import Root
from state.StartScreen import StartScreen
from state.Game import Game
from state.DeathScreen import DeathScreen
from state.Credit import Credit

class StateManager:
    sys = StartScreen()
    last_state = 0

    @staticmethod
    def change_state():
        if Root.state != StateManager.last_state:
            if Root.state == 0:
                StateManager.sys = StartScreen()
                StateManager.sys.init()
                StateManager.last_state = 0
            elif Root.state == 1:
                StateManager.sys = Game()
                StateManager.sys.init()
                StateManager.last_state = 1
            elif Root.state == 2:
                StateManager.sys = DeathScreen()
                StateManager.sys.init()
                StateManager.last_state = 2
            else:
                StateManager.sys = Credit()
                StateManager.sys.init()
                StateManager.last_state = 3

    @staticmethod
    def tick():
        StateManager.sys.tick()
        StateManager.change_state()


