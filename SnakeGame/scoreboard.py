from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.count = 0
        with open("highscore.txt") as data:
            self.highscore = int(data.read())

    def display(self):
        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.goto(0, 281)


    def score(self):
        self.clear()
        self.write(f"Score: {self.count}", False, align="center", font=("calibre", 12, "italic"))
        self.write(f"\t\t\tHighscore: {self.highscore}", False, align="center", font=("calibre", 12, "italic"))

    def reset(self):
        if self.count > self.highscore:
            self.highscore = self.count
            with open("highscore.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.count = 0
        self.score()

