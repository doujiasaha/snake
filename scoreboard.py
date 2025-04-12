from turtle import Turtle

with open("score.txt", "r+") as file:
    highscore = file.read()
    if len(highscore) == 0:
        file.write("0")
        file.seek(0)
        highscore = file.read()



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
        self.high_score = int(highscore)
        self.score_up()
        
    def score_up(self):    
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.high_score}", False, align=ALIGNMENT, font=FONT)
        
    def increase_score(self):
        self.score +=1
        self.score_up()
        
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open("score.txt", "w") as file:
            file.write(f"{self.high_score}")
        self.score = 0
        self.score_up()
