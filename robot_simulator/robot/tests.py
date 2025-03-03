import unittest
from robot.robot_logic import ToyRobot

# core unit test
class TestToyRobot(unittest.TestCase):

    def setUp(self):
        self.robot = ToyRobot()

    def test_valid_place_command(self):
        result = self.robot.execute_command("PLACE 0,0,NORTH")
        self.assertEqual(result, {"message": "Placed at 0,0,NORTH"})

    def test_place_command_with_lowercase_and_spaces(self):
        result = self.robot.execute_command("place 0 , 0 , north")
        self.assertEqual(result, {"message": "Placed at 0,0,NORTH"})

    def test_move_within_bounds(self):
        self.robot.execute_command("PLACE 0,0,NORTH")
        result = self.robot.execute_command("MOVE")
        self.assertEqual(result, {"message": "Moved to 0,1,NORTH"})

    def test_prevent_falling(self):
        self.robot.execute_command("PLACE 0,0,SOUTH")
        result = self.robot.execute_command("MOVE")
        self.assertEqual(result, {"error": "MOVE command ignored. Robot would fall off the table"})

    def test_turn_left(self):
        self.robot.execute_command("PLACE 0,0,NORTH")
        result = self.robot.execute_command("LEFT")
        self.assertEqual(result, {"message": "Turned Left. Now facing WEST"})

    def test_turn_right(self):
        self.robot.execute_command("PLACE 0,0,NORTH")
        result = self.robot.execute_command("RIGHT")
        self.assertEqual(result, {"message": "Turned Right. Now facing EAST"})

# test for api will be added here