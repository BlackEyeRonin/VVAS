# sim/scenario_generator.py
import random

def generate_obstacles(n=5, width=800, height=600):
    obstacles = []
    for _ in range(n):
        x = random.randint(200, width - 50)
        y = random.randint(50, height - 50)
        r = random.randint(15, 30)
        obstacles.append((x, y, r))
    return obstacles
