import random, time
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game!")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()
score = 0


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")    
    
    
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    #collision
    if snake.head.distance(food) < 15:
        food.refresh()
        score += 1
        scoreboard.erase()
        scoreboard.write(f"Score: {score}", False, align="center", font=("Arial", 12, "normal"))

        
    
        




screen.exitonclick()