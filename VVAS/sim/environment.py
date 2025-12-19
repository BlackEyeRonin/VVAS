# sim/environment.py
import math

class Environment:
    def __init__(self, width=800, height=600, obstacles=None):
        self.width = width
        self.height = height
        self.obstacles = obstacles if obstacles else []

    def is_collision(self, x, y, radius=10):
        for ox, oy, r in self.obstacles:
            if math.hypot(x - ox, y - oy) <= (r + radius):
                return True
        return False

    def ray_distance(self, x, y, angle, max_dist=200):
        step = 5
        for d in range(0, max_dist, step):
            rx = x + d * math.cos(angle)
            ry = y + d * math.sin(angle)

            if rx < 0 or rx > self.width or ry < 0 or ry > self.height:
                return d

            for ox, oy, r in self.obstacles:
                if math.hypot(rx - ox, ry - oy) <= r:
                    return d

        return max_dist

    def get_sensor_readings(self, car):
        angles = {
            "left": car.heading + math.radians(30),
            "center": car.heading,
            "right": car.heading - math.radians(30),
        }

        return {
            k: self.ray_distance(car.x, car.y, a)
            for k, a in angles.items()
        }
