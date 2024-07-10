from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.speed("fastest")
        self.hideturtle()
        self.goto(0, 270)
        self.color("white")
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.high_score}", align="center", font=("Verdana", 15, "normal"))

    def increment_score(self):
        self.score += 1
        self.display_score()

    def game_over(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.display_score()
