## Control Layer

The control layer manages authority, safety, and action translation.

### Responsibilities
- Evaluate ML confidence
- Decide autonomy level (Safety vs War mode)
- Translate decisions into vehicle commands

### Design Philosophy
ML never directly controls hardware.
All actions pass through a safety-aware authority gate.
