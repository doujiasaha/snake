from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 18, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.score = 0
        
    def score_up(self):    
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)
        
    def erase(self):
        self.clear()
        
    def increase_score(self):
        self.score +=1
        
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)
        