from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score=0
        with open("data.txt", mode="r") as a:
            self.High_score=int(a.read())
        self.hideturtle()
        self.goto(0,270)
        self.color("white")
        self.write(f"Score : {self.score}    Previous High Score : {self.High_score}", align="center", font=("Arial", 15, "normal"))
    def increase(self):
        self.clear()
        self.score += 1
        self.write(f"Score : {self.score}     Previous High Score : {self.High_score}", align="center", font=("Arial", 15, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.color("white")
        self.write(f"Game Over", align="center", font=("Arial", 15, "normal"))

    def high_score(self):

        self.clear()
        if self.score> self.High_score:
            with open("data.txt",mode="w") as d:
                d.write(str(self.score))
            self.goto(0,230)
            self.write(f"New High Score!!!", align="center",font=("Arial", 15, "normal"))
        self.goto(0,270)
        self.write(f"Score : {self.score}   Previous High Score : {self.High_score}", align="center", font=("Arial", 15, "normal"))

