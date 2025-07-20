import random

def generate_event():
    events = [
        {"type": "monster", "description": "A shadow beast blocks your path!", "monster": {"name": "Shadow Beast", "damage": 20}},
        {"type": "item", "description": "You see a glowing chest!", "item": {"name": "Healing Potion"}},
        {"type": "story", "description": "You arrive at an ancient temple..."},
    ]
    return random.choice(events)