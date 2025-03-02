class toyRobot:

    DIRECTIONS = ["NORTH", "EAST", "SOUTH", "WEST"]

    MOVEMENTS = {
        "NORTH": (0, 1),
        "SOUTH": (0, -1),
        "EAST": (1, 0),
        "WEST": (-1, 0)
    }

    def __init__(self):
        self.x = None
        self.y = None
        self.facing = None
        self.table_size = 5
    
    def _is_within_bounds(self,x,y):
        return 0 <= x < self.table_size and 0 <= y < self.table_size
    
    def place

    def move

    def left

    def right
    
    def report

    def check command 
