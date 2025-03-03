from rest_framework.views import APIView
from rest_framework.response import Response
from .robot_logic import ToyRobot

robot = ToyRobot() 

class RobotCommandView(APIView):
    def post(self, request):
        command = request.data.get("command", "").strip().upper()
        if not command:
            return Response({"error": "Command is required"}, status=400)
        result = robot.execute_command(command)
        return Response(result)