import time
from snake import Snake
from score import Score
from food import Food
from turtle import Screen

score_a = Score()
snake = Snake()

food = Food()
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True


while game_is_on :
    screen.update()
    time.sleep(0.14)
    snake.move()
    snake.check_head_tail_touch()
    if snake.head.distance(food) < 15:
        food.get_rand_position()
        score_a.update()
        snake.add_segment()
    elif snake.head_tail_touch:
        score_a.reset()
        score_a.update()
        snake.clear()
        # game_is_on = False
    elif snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        score_a.reset()
        score_a.update()
        snake.clear()
        # game_is_on = False
    else:
        pass




screen.exitonclick()

