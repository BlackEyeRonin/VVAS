# control/confidence_gate.py

import numpy as np

class ConfidenceGate:
    def __init__(self):
        pass

    def compute_confidence(self, action_probs):
        """
        action_probs: list or numpy array
        Example: [0.1, 0.2, 0.6, 0.1]
        """

        action_probs = np.array(action_probs)

        max_prob = np.max(action_probs)
        entropy = -np.sum(action_probs * np.log(action_probs + 1e-9))

        # Normalize entropy (lower entropy = more confidence)
        normalized_entropy = entropy / np.log(len(action_probs))

        confidence = max_prob * (1 - normalized_entropy)

        return round(float(confidence), 3)
