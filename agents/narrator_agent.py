from tools.event_generator import generate_event
from agents.monster_agent import MonsterAgent
from agents.item_agent import ItemAgent

class NarratorAgent:
    def __init__(self, game_state):
        self.state = game_state

    def start_game(self):
        print("🧙 Welcome to the Realm of Shadows!")
        while self.state.is_alive:
            event = generate_event()
            print(f"\n{event['description']}")
            choice = input("What do you want to do? ").lower()
            
            if event["type"] == "monster":
                monster = MonsterAgent(self.state)
                monster.fight(event["monster"])
            elif event["type"] == "item":
                item = ItemAgent(self.state)
                item.give_reward(event["item"])