from turtle import Turtle


class Wall():

    def __init__(self):
        self.horeizontal_walls = []
        self.vertical_walls = []
        self.hxcor = -270
        self.uhycor = 290
        self.dhycor = -280
        self.dhxcor=-270
        self.lvxcor=-287
        self.lvycor=260
        self.rvxcor=282
        self.rvycor=260


    def horizontal_build_wall(self):
        wall = Turtle("square")
        wall.penup()
        wall.color("red")
        wall.shapesize(stretch_len=4)
        self.horeizontal_walls.append(wall)
    def vertical_build_wall(self):
        wall = Turtle("square")
        wall.penup()
        wall.color("red")
        wall.setheading(90)
        wall.shapesize(stretch_len=4)
        self.vertical_walls.append(wall)

    def set_path(self):
        for i in range(0,16):
            if i<8:
                self.horeizontal_walls[i].goto(self.hxcor,self.uhycor)
                self.hxcor+=85
            else:
                self.horeizontal_walls[i].goto(self.dhxcor,self.dhycor)
                self.dhxcor+=85
        for j in range(0,16):
            if j<8:
                self.vertical_walls[j].goto(self.lvxcor,self.lvycor)
                self.lvycor-=85
            else:
                self.vertical_walls[j].goto(self.rvxcor,self.rvycor)
                self.rvycor-=85
        
            
            

# wall=Wall()
# for _ in range (16):
#     wall.horizontal_build_wall()
# wall.set_path()
