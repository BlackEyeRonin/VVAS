# sim/simulator.py
from sim.environment import Environment
from sim.vehicle_model import Vehicle

class Simulator:
    def __init__(self, env: Environment, car: Vehicle):
        self.env = env
        self.car = car
        self.done = False

    def get_state(self):
        sensors = self.env.get_sensor_readings(self.car)
        return [
            sensors["left"],
            sensors["center"],
            sensors["right"],
            self.car.speed
        ]

    def step(self, action):
        if self.done:
            return self.get_state(), 0, True

        self.car.step(action)

        reward = 1.0  # survival reward

        if self.env.is_collision(self.car.x, self.car.y):
            reward = -100
            self.done = True

        return self.get_state(), reward, self.done
