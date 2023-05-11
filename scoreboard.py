from turtle import Turtle

ALIGNMENT = "center"
FONT = "Arial"
FONT_SIZE = 24
FONT_STYLE = "normal"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}", font=(FONT, FONT_SIZE, FONT_STYLE), align=ALIGNMENT)

    def increase_score(self):
        self.score += 1
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", font=(FONT, FONT_SIZE, FONT_STYLE), align=ALIGNMENT)
