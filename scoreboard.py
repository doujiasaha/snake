from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0,280)
        self.hideturtle()
        
    def score(self):    
        self.write("Score: ", False, align="center", font=("Arial", 12, "normal"))
        
    def erase(self):
        self.clear()
        