from rest_framework.views import APIView
from rest_framework.response import Response
from .robot_logic import ToyRobot

class RobotCommandView(APIView):
    def post(self, request):
        command = request.data.get("command", "").strip().upper()
        if not command:
            return Response({"error": "Command is required"}, status=400)

        robot_state = request.session.get("robot_state", None)

        if robot_state is None:
            robot = ToyRobot()
        else:
            robot = ToyRobot()
            robot.x, robot.y, robot.facing = robot_state.get("x"), robot_state.get("y"), robot_state.get("facing")

        result = robot.execute_command(command)

        if command == "REPORT":
            request.session.flush()  

        if "error" not in result and command != "REPORT":
            request.session["robot_state"] = {
                "x": robot.x,
                "y": robot.y,
                "facing": robot.facing,
            }

        return Response(result)
