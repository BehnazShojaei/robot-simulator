import sys
from robot.robot_logic import ToyRobot  


def run_cli():
    robot = ToyRobot()
    print("Welcome to the Toy Robot Simulator!")
    print("Enter commands (PLACE X,Y,FACING and then MOVE, LEFT, RIGHT, REPORT), or type 'EXIT' to quit.")

    while True:
        command = input("Enter command: ").strip().upper()
        if command == "EXIT":
            print("Exiting...")
            break
        result = robot.execute_command(command)
        print(result)

# will define the file upload method

if __name__ == "__main__":
    
        run_cli()
