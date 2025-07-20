class ItemAgent:
    def __init__(self, state):
        self.state = state

    def give_reward(self, item):
        print(f"🎁 You found a {item['name']}!")
        self.state.inventory.append(item)