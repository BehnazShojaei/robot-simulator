import sys
from robot.robot_logic import ToyRobot  


def run_cli():
    robot = ToyRobot()

    print("\nWelcome to the Toy Robot Simulator! ")
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


def run_file_input(file_path):
    robot = ToyRobot()

    try:
        with open(file_path, "r") as file:
            for line in file:
                command = line.strip().upper()
                if command:  
                    result = robot.execute_command(command)
                    print(result)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")

    except Exception as e:
        print(f"An error occurred: {e}")

        
if __name__ == "__main__":
    
    if len(sys.argv) > 1:
        file_path = sys.argv[1]  
        run_file_input(file_path)
    else:
        run_cli()
        
