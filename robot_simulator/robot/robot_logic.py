class ToyRobot:

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
        
        # facing = facing.upper()
         
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
              

    def report(self):
        if self.x is not None and self.y is not None:
            return {"x": self.x, "y": self.y, "facing": self.facing}
        return {"error": "Robot is not placed yet"}





    def execute_command(self, command):
        try:
            command = command.strip().upper()  
            parts = command.split(" ", 1)  

            if parts[0] == "PLACE":
                if len(parts) < 2:
                     return {"error": "Invalid format! Use: PLACE X,Y,FACING"}

                params = parts[1].replace(" ", "")  
                values = params.split(",")
                
                if len(values) == 3:
                    return {"error": "Invalid format! Use: PLACE X,Y,FACING (e.g., PLACE 0,0,NORTH)"}

                try:
                
                    x, y = int(values[0]), int(values[1])
                    facing = values[2].upper()
                    
                    if facing not in self.DIRECTIONS:
                        return {"error": f"Invalid direction '{facing}'. Must be one of {self.DIRECTIONS}."}
                    
                    return self.place(x, y, facing)
                except ValueError:
                    return {"error": "Invalid input! X and Y must be integers."}


            elif command == "MOVE":
                return self.move()
            elif command == "LEFT":
                return self.left()
            elif command == "RIGHT":
                return self.right()
            elif command == "REPORT":
                return self.report()
            return {"error": f"Invalid command '{command}'"}

        except Exception as e:
            return {"error": f"Command error: {str(e)}"}
