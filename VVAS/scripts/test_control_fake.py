from control.authority_manager import AuthorityManager
from control.decision_mapper import DecisionMapper
import random
import time

authority = AuthorityManager()
decision = DecisionMapper()

while True:
    distances = [
        round(random.uniform(0.3, 2.5), 2),
        round(random.uniform(0.3, 2.5), 2),
        round(random.uniform(0.3, 2.5), 2),
    ]

    auth_state = authority.step(distances)
    control = decision.map_decision(distances, auth_state)

    print("\n[FAKE SENSOR]", distances)
    print("[AUTHORITY]", auth_state)
    print("[CONTROL]", control)

    time.sleep(1)
