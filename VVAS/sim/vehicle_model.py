# sim/vehicle_model.py
import math

class Vehicle:
    def __init__(self, x=100, y=300):
        self.x = x
        self.y = y
        self.heading = 0.0
        self.speed = 0.0

        self.max_speed = 5.0
        self.max_steer = math.radians(25)

    def step(self, action):
        steer, throttle = action

        steer = max(-self.max_steer, min(self.max_steer, steer))
        self.speed += throttle
        self.speed = max(0.0, min(self.max_speed, self.speed))

        self.heading += steer
        self.x += self.speed * math.cos(self.heading)
        self.y += self.speed * math.sin(self.heading)
