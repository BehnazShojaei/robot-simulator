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
    
    def _is_within_bounds(self, x, y):
         return 0 <= x < self.table_size and 0 <= y < self.table_size
    

    def place(self, x, y, facing):
        
        facing = facing.upper()
         
        if not self._is_within_bounds(x, y):
            return {"error": f"Invalid position ({x},{y}). Must be within (0-{self.table_size-1}, 0-{self.table_size-1})."}
        
        if facing not in self.DIRECTIONS:
            return {"error": f"Invalid direction '{facing}'. Must be one of {self.DIRECTIONS}."}
        
        self.x, self.y, self.facing = x, y, facing

        return {"message": f"Placed at {x},{y},{facing}"}


    def move

    def left

    def right
    
    def report

    def check command 

    def check origin point