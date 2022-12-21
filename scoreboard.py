
from turtle import Turtle
from snake import Snake
ALIGNMENT="center"
FONT=("Courier",20,"normal")


class Scoreboard(Turtle):


    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt") as file:
            self.high_score=file.read()
        self.color("black")
        self.penup()
        self.goto(x=0,y=250)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        if self.score>int(self.high_score):
            self.high_score=self.score
            with open("high_score.txt",'w') as f:
                f.write(str(self.score))
        self.write(arg=f"SCORE:{self.score} HIGH SCORE: {self.high_score}",align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score+=1
        self.update_scoreboard()
    
        
        