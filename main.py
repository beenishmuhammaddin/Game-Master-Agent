
from agents.narrator_agent import NarratorAgent
from game_state import GameState

def main():
    game_state = GameState()
    narrator = NarratorAgent(game_state)
    narrator.start_game()

if __name__ == "__main__":
    main()