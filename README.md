# robot-simulator

### Understaing the question:

- A grid of 5x5 units tabletop
- Issue command to a toy robot to roam around
- No obstructions
- Robot must not fall off the grid

### Breaking Down the Solution

1. **Design a ToyRobot class**

- Properties: x, y, facing
- Methods: place(), move(), left(), right(), report()
- Discard commands before a valid PLACE.
- Handles edge cases to prevent falls

2. **Input Handling**

Two choices:

- Read commands from a file (robot.py)
- Accept input via a REST API

3. **Unit Testing**

- Placing the toy robot at origin point
- Ignoring commands before a valid PLACE
- Handling multiple PLACE commands
- Valid movement and prevent falls
- Handle incorrect inputs. e.g. reject PLACE -1,-1,NORTH
