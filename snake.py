from turtle import Turtle,Screen
tp=[(0,0),(-20,0),(-40,0)]
s=Screen()
class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.move_snake()
    def create_snake(self):
        for i in tp:
            self.add_snake(i)
    def add_snake(self,i):
        t1 = Turtle()
        t1.shape("square")
        t1.color("white")
        t1.penup()
        t1.goto(i)
        self.segments.append(t1)
    def extend_snake(self):
        self.add_snake(self.segments[-1].position())
    def move_snake(self):
        for i in range(len(self.segments)-1,0,-1):
           x=self.segments[i-1].xcor()
           y=self.segments[i-1].ycor()
           self.segments[i].goto(x,y)
        self.segments[0].forward(20)


    def right(self):
        if self.segments[0].heading()!=180:
            self.segments[0].setheading(0)
    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)
    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)
    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)


