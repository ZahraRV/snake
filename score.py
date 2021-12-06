
from turtle import Turtle
font = ("Arial", 20, "normal")
align = "center"


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score_number = -1
        self.high_score=0
        self.penup()
        self.color("white")
        self.sety(250)
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.score_number += 1
        with open("high_score.txt", mode="r")as update_high_score:
            self.high_score = int(update_high_score.read())
        self.write(f"score: {self.score_number} ,high score: {self.high_score}", align=align, font=font)

    # def game_over(self):
    #     self.clear()
    #     self.goto(0, 0)
    #     self.write(f"game over\nscore:{self.score_number}", align=align, font=font)

    def reset(self):
        if self.score_number > self.high_score:
            self.high_score = self.score_number
            with open("high_score.txt", mode="w")as high_score_record:
                high_score_record.write(f"{self.high_score}")
        self.score_number = -1