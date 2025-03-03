class toyRobot:

    DIRECTIONS = ["NORTH", "EAST", "SOUTH", "WEST"]

    MOVEMENTS = {
        "NORTH": (0, 1),
        "SOUTH": (0, -1),
        "EAST": (1, 0),
        "WEST": (-1, 0)
    }

    def __init__(self):
        self.x = 0
        self.y = 0
        self.facing = "NORTH"
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


    def move(self):
        if self.x is None or self.y is None or self.facing is None:
            return {"error": "Robot is not placed yet"}
        
        dx, dy = self.MOVEMENTS[self.facing]
        new_x = self.x + dx
        new_y = self.y + dy

        if self._is_within_bounds(new_x, new_y):
            self.x, self.y = new_x, new_y
            return {"message": f"Moved to {self.x},{self.y},{self.facing}"}
        return {"error": "MOVE command ignored. Robot would fall off the table"}


    def left(self):
        if self.facing:
             current_index = self.DIRECTIONS.index(self.facing)
             self.facing = self.DIRECTIONS[(current_index -1) % 4 ]
              

    def right(self):
        if self.facing:
            current_index = self.DIRECTIONS.index(self.facing)
            self.facing = self.DIRECTIONS[(current_index +1) % 4 ]
              

    def report

    def check command 

