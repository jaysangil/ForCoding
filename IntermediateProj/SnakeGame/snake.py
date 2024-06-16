from turtle import Turtle

# Constants for initial positions and movement parameters
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0 
LEFT = 180

class Snake:
    def __init__(self):
        self.segments = []  # List to hold the segments of the snake
        self.create_snake()  # Initial creation of the snake
        self.head = self.segments[0]  # The first segment is always the head

    def create_snake(self):
        """Creates the initial snake with specified starting positions."""
        for position in STARTING_POSITIONS:
            self.add_segment(position)
           
            
    def add_segment(self, position):
            new_segment = Turtle("square")  # Create a new turtle shaped like a square
            new_segment.color("#39FF14")  # Set the segment color to neon green
            new_segment.penup()  # Lift the pen to avoid drawing lines
            new_segment.goto(position)  # Move the segment to the starting position
            self.segments.append(new_segment)  # Add the segment to the snake's body  
            
    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segment.clear()     
        self.create_snake()
        self.head = self.segments[0]
            
    def extend(self):
        self.add_segment(self.segments[-1].position())#add new segment to the snake.

    def move(self):
        """Move the snake forward by moving each segment to the position of the previous segment."""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()  # Get the x-coordinate of the previous segment
            new_y = self.segments[seg_num - 1].ycor()  # Get the y-coordinate of the previous segment
            self.segments[seg_num].goto(new_x, new_y)  # Set the current segment's position
        self.head.forward(MOVE_DISTANCE)  # Move the head forward

    def up(self):
        """Change the direction of the snake to up unless it's moving down."""
        if self.head.heading() != DOWN:  # Prevent reversing the snake
            self.head.setheading(UP)  # Set the head's direction to UP

    def down(self):
        """Change the direction of the snake to down unless it's moving up."""
        if self.head.heading() != UP:  # Prevent reversing the snake
            self.head.setheading(DOWN)  # Set the head's direction to DOWN

    def left(self):
        """Change the direction of the snake to left unless it's moving right."""
        if self.head.heading() != RIGHT:  # Prevent reversing the snake
            self.head.setheading(LEFT)  # Set the head's direction to LEFT

    def right(self):
        """Change the direction of the snake to right unless it's moving left."""
        if self.head.heading() != LEFT:  # Prevent reversing the snake
            self.head.setheading(RIGHT)  # Set the head's direction to RIGHT
