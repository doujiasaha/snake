from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake():
    
    def __init__(self):
        self.snake_parts = []
        self.create_snake()
        self.head = self.snake_parts[0]    
            
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.snake = Turtle("square")
            self.snake.color("white")
            self.snake.penup()
            self.snake.goto(position)
            self.snake_parts.append(self.snake)        
            
    def move(self):
        for seg in range(len(self.snake_parts) -1 ,0, -1):
            new_x = self.snake_parts[seg -1].xcor()
            new_y = self.snake_parts[seg -1].ycor()
            self.snake_parts[seg].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)
        
    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)
        
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)
        
    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)        