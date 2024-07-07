from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.speed("fastest")
        self.hideturtle()
        self.goto(0, 270)
        self.color("white")
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Verdana", 15, "normal"))

    def increment_score(self):
        self.score += 1
        self.display_score()

    def game_over(self):
        self.home()
        self.write("Game Over.", align="center", font=("Verdana", 15, "normal"))
