# control/authority_manager.py

class AuthorityManager:
    def __init__(self,
                 confidence_threshold=0.7,
                 emergency_stop=True):
        self.confidence_threshold = confidence_threshold
        self.emergency_stop = emergency_stop
        self.current_mode = "SAFETY"  # SAFETY or WAR

    def decide_authority(self, ml_confidence):
        """
        Decide who controls the vehicle.
        """

        if self.emergency_stop:
            return "STOP"

        if ml_confidence >= self.confidence_threshold:
            self.current_mode = "WAR"
            return "ML"

        self.current_mode = "SAFETY"
        return "SAFE_RULES"

    def get_mode(self):
        return self.current_mode
