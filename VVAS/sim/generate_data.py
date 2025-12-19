# sim/generate_data.py
import csv

def log_step(writer, state, action, reward):
    writer.writerow({
        "left": state[0],
        "center": state[1],
        "right": state[2],
        "speed": state[3],
        "steer": action[0],
        "throttle": action[1],
        "reward": reward
    })
