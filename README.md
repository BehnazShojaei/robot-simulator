# Robot Simulator

## Understanding the Question

We have a toy robot on a tabletop, a 5x5 unit grid with no obstructions. We can issue commands to the robot to allow it to roam around while ensuring it does not fall off the grid.

### Commands

- `PLACE X,Y,FACING` - Places the robot at position (X, Y) facing `NORTH`, `SOUTH`, `EAST`, or `WEST`.
- `MOVE` - Moves the robot one unit forward in the direction it is currently facing.
- `LEFT` - Rotates the robot 90 degrees counterclockwise.
- `RIGHT` - Rotates the robot 90 degrees clockwise.
- `REPORT` - Outputs the robot's current position and facing direction.

### Constraints

- The first valid command must be `PLACE X,Y,FACING`.
- Any movement that would cause the robot to fall off the table is ignored.
- Input can be from a file or standard input.

---

## Breaking Down the Solution

### 1. **Designing the `ToyRobot` Class**

- **Properties**: `x`, `y`, `facing`
- **Methods**:
  - `place(x, y, facing)`: Places the robot at a valid position.
  - `move()`: Moves the robot forward if it's within bounds.
  - `left()`: Rotates the robot left.
  - `right()`: Rotates the robot right.
  - `report()`: Outputs the current position.
- Commands before a valid `PLACE` are ignored.
- The logic ensures the robot doesn’t fall off the grid.

### 2. **Input Handling**

- Accept commands via:
  - CLI input (`robot_cli.py`)
  - File input (`commands.txt`)
  - REST API (using Django + DRF)

### 3. **Unit Testing**

- Tests include:
  - Placing the toy robot at a valid origin point.
  - Ignoring commands before a valid `PLACE`.
  - Handling multiple `PLACE` commands.
  - Valid movement and preventing falls.
  - Handling incorrect inputs (e.g., `PLACE -1,-1,NORTH`).

---

## Project Structure

```
robot-simulator/
│── robot_simulator/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│── robot/
│   ├── __init__.py
│   ├── robot_logic.py  # Contains ToyRobot class and logic
│   ├── robot_cli.py    # CLI interaction
│   ├── tests.py        # Unit tests
│── staticfiles/
│── commands.txt        # Sample command file
│── db.sqlite3          # Database (not used in this project)
│── manage.py           # Django entry point
│── README.md
│── requirements.txt    # Dependencies
│── .env                # Environment variables
│── .gitignore
│── .python-version
│── Procfile
```

---

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/BehnazShojaei/robot-simulator.git
cd robot-simulator
code .
```

### 2. Create a Virtual Environment

#### On macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

#### On Windows:

```powershell
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

#### On macOS/Linux:

```bash
pip install -r requirements.txt
```

#### On Windows:

```powershell
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory (see [Project Files ](#project-files)) and add:

```env
DJANGO_DEBUG=True
SECRET_KEY='django-insecure-l^&*c*v14ltihoie00-1wszo26cx+^ukh^)*2v#0pmc&wbacw5'
DATABASE_URL= 'postgres://u61f3137lahc78:p1c2e77444b5a4481c8a05f6be3b61ba134de66bf46b959ba956e9b3fbe178d7d@c8lj070d5ubs83.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/d1f8gflokmsvao'
```

Please don't forget to save!

## Running the Application

### Running the CLI Version

To play the game via terminal:

```bash
python3 robot_cli.py
```

You will see:

```
Welcome to the Toy Robot Simulator!
Instructions:
1- First, PLACE your robot on the board using ➜ PLACE X,Y,FACING (e.g., PLACE 0,0,NORTH)
2- Then, you can issue any of these commands ➜ MOVE  |  LEFT  |  RIGHT  |  REPORT
3- You can also reissue `PLACE` anytime to move your robot.
4- Type 'EXIT' to quit.
```

Example input :

```bash
> PLACE 0,0,NORTH
> MOVE
> REPORT
Output: 0, 1, NORTH
```

Please feel free to start with any command! in lowercase or uppercase or some extra space!

### Running with a File Input

To run with a predefined set of commands:

```bash
python robot_cli.py commands.txt
```

Example Output:

```
{'message': 'Placed at 1,2,EAST'}
{'message': 'Moved to 2,2,EAST'}
{'message': 'Moved to 3,2,EAST'}
{'message': 'Turned Left. Now facing NORTH'}
{'message': 'Moved to 3,3,NORTH'}
{'message': 'Turned Right. Now facing EAST'}
{'x': 3, 'y': 3, 'facing': 'EAST'}
```

Please feel free to update commands.txt with commands of your choice and run the game again!

## Running the Tests

To run the unit tests:

```bash
cd robot_simulator
python manage.py test robot
```

Expected Output:

```
Found 6 test(s).
System check identified no issues (0 silenced).
......
----------------------------------------------------------------------
Ran 6 tests in 0.001s

OK
```

### Testing the API

The API has been tested using **Insomnia**, but you can also use **Postman** or `curl` to send requests. If you want to test it locally, please run:

```bash
python manage.py runserver
```

Then make a POST request to:

```
http://127.0.0.1:8000/command/
```

Alternatively, you can test it directly on the deployed API!

---

## Using the Deployed API

The API is deployed at:
[https://toy-robot-7bbe4d71b9be.herokuapp.com/command/](https://toy-robot-7bbe4d71b9be.herokuapp.com/command/)

### Example Requests

#### Place Robot

```json
{
  "command": "place 0,2,north"
}
```

#### Move Robot

```json
{
  "command": "move"
}
```

#### Rotate Left

```json
{
  "command": "left"
}
```

#### Report Position

```json
{
  "command": "report"
}
```

The API processes commands in a case-insensitive manner and responds in JSON format. With every report command the game will restart!

---

## Summary

- [x] CLI and file-based input support
- [x] REST API implementation using Django + DRF
- [x] Prevents robot from falling off
- [x] Unit tests included
- [x] Hosted API for easy testing

Hope you enjoy playing this game! I had so much fun making it!

---

## Notes

- Preferred languages were C#, Java, or Node, but the implementation was done in Python + Django + DRF due to familiarity within the given deadline.
- The project follows DRY principles and ensures simplicity while maintaining flexibility.
- Future improvements: Implementing this in C# or Java for better alignment with the coding activity.
