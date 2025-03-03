import sys
from robot.robot_logic import ToyRobot  


def run_cli():
    robot = ToyRobot()

    print("\n Welcome to the Toy Robot Simulator! \n")
    print("Instructions:")
    print("1- First, PLACE your robot on the board using ➜ PLACE X,Y,FACING (e.g., PLACE 0,0,NORTH)")
    print("2- Then, you can issue any of these commands ➜ MOVE  |  LEFT  |  RIGHT  |  REPORT")
    print("3- You can also reissue `PLACE` anytime to move your robot.")
    print("4- Type 'EXIT' to quit.\n")

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
