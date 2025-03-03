import sys
from robot.robot_logic import ToyRobot  


def run_cli():
    robot = ToyRobot()

    print("\n Ready for the game?! \n")
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

    print("\nWelcome to the Toy Robot Simulator! ")
    mode = input("Choose input method: Type 'console' for interactive mode or 'file' to load commands from a file: ").strip().lower()

    if mode == "file":
        file_path = input("Enter the file name (e.g., commands.txt): ").strip()
        run_file_input(file_path)
        
    else:
        run_cli()
        
