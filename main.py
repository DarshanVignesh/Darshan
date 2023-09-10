from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

s=Screen()
s.title(titlestring="Welcome to snake game")
s.setup(width=600, height=600)
s.bgcolor("black")
s.listen()
s.tracer(0)
snake=Snake()

game=True
food=Food()
score=Score()
while game:
    s.update()
    time.sleep(0.1)

    snake.move_snake()
    s.onkey(snake.left,"a")
    s.onkey(snake.right,"d")
    s.onkey(snake.up,"w")
    s.onkey(snake.down,"s")
    if snake.segments[0].distance(food)<15:
        food.movingball()
        score.increase()
        score.high_score()
        snake.extend_snake()
    if snake.segments[0].xcor()>290 or snake.segments[0].ycor()>290 or snake.segments[0].xcor()<-310 or snake.segments[0].ycor()<-290:
        game=Falsew
        score.game_over()
    for i in snake.segments:
        if i==snake.segments[0]:
            pass
        elif snake.segments[0].distance(i)<10:
            game=False
            score.game_over()

s.exitonclick()