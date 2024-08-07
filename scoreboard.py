from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.speed("fastest")
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=265)
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", move=False, align='center', font=('Arial', 18, 'normal'))

    def print_game_over(self):
        self.goto(x=0, y=0)
        self.write(arg="Game Over!", move=False, align='center', font=('Arial', 24, 'normal'))

    def increase_score(self):
        self.score += 1
