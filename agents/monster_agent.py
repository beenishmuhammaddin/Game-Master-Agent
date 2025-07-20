from tools.dice_roller import roll_dice

class MonsterAgent:
    def __init__(self, state):
        self.state = state

    def fight(self, monster):
        print(f"👹 A wild {monster['name']} appears!")
        player_roll = roll_dice()
        monster_roll = roll_dice()
        
        print(f"You rolled {player_roll}, Monster rolled {monster_roll}")
        if player_roll >= monster_roll:
            print("✅ You defeated the monster!")
        else:
            self.state.health -= monster["damage"]
            print(f"❌ You got hit! Health: {self.state.health}")
            if self.state.health <= 0:
                self.state.is_alive = False