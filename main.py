
from turtle import Screen, Turtle, penup, update
import time
from venv import create
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from wall import Wall





screen=Screen()
screen.bgcolor("cornflower blue")
screen.setup(width=600,height=600)
screen.title("=====Snake Game=====")
screen.tracer(0)

#setup walls
wall=Wall()
for _ in range (16):
    wall.horizontal_build_wall()
for i in range (16):
    wall.vertical_build_wall()
wall.set_path()
snake=Snake()
food=Food()
scoreboard=Scoreboard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")



game_is_on=True

while(game_is_on):
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect collision with food
    if snake.head.distance(food)<15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()
        
    #detect collision with wall
    if snake.head.xcor()>270 or snake.head.xcor()<-279 or snake.head.ycor()>279 or snake.head.ycor()<-270:
        snake.reset_snake()
        scoreboard.score=0
        scoreboard.update_scoreboard()

    #detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            snake.reset_snake()
            scoreboard.score=0
            scoreboard.update_scoreboard()
            
            











screen.exitonclick()