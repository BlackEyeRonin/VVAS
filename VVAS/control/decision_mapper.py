# control/decision_mapper.py

class DecisionMapper:
    def __init__(self):
        # Limits for RC car
        self.max_steer = 1.0
        self.max_throttle = 1.0

    def map_action(self, action):
        """
        action: string
        """

        if action == "FORWARD":
            return {"steer": 0.0, "throttle": 0.8}

        if action == "LEFT":
            return {"steer": -0.6, "throttle": 0.6}

        if action == "RIGHT":
            return {"steer": 0.6, "throttle": 0.6}

        if action == "BRAKE":
            return {"steer": 0.0, "throttle": 0.0}

        # Default safe action
        return {"steer": 0.0, "throttle": 0.0}
