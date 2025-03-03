from django.urls import path
from .views import RobotCommandView

urlpatterns = [
    path("command/", RobotCommandView.as_view(), name="robot-command"),
]