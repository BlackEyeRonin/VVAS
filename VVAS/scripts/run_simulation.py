# scripts/run_simulation.py

from sim.environment import Environment
from sim.vehicle_model import Vehicle
from sim.simulator import Simulator
from sim.scenario_generator import generate_obstacles

import random
import time

def main():
    # 1️⃣ Create environment
    obstacles = generate_obstacles(n=6)
    env = Environment(obstacles=obstacles)

    # 2️⃣ Create vehicle
    car = Vehicle(x=100, y=300)

    # 3️⃣ Create simulator
    sim = Simulator(env, car)

    step_count = 0

    print("🚗 VVAS Simulation Started (NO HARDWARE)")

    # 4️⃣ Run simulation loop
    while not sim.done and step_count < 200:
        # Random policy for now
        steer = random.uniform(-0.2, 0.2)
        throttle = random.uniform(0.0, 0.3)

        state, reward, done = sim.step((steer, throttle))

        print(
            f"Step {step_count} | "
            f"L:{state[0]:.1f} "
            f"C:{state[1]:.1f} "
            f"R:{state[2]:.1f} "
            f"Speed:{state[3]:.2f} "
            f"Reward:{reward}"
        )

        step_count += 1
        time.sleep(0.05)

    print("🛑 Simulation ended")

if __name__ == "__main__":
    main()
