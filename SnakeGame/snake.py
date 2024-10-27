from turtle import Turtle
Starting_Positions = [(0, 0), (-20, 0), (-40, 0)]
Move_Distance = 20


class Snake:
    def __init__(self):
        self.tur_list = []
        self.create_snake()
        self.move()

    def create_snake(self):
        x = 0
        y = 0
        for position in Starting_Positions:
            self.add_segment(position)

    def add_segment(self, position):
        tur = Turtle()
        tur.penup()
        tur.shape("square")
        tur.color("white")
        tur.speed("fastest")
        tur.goto(position)
        self.tur_list.append(tur)

    def extend(self):
        self.add_segment(self.tur_list[-1].position())

    def move(self):
        for seg_num in range(len(self.tur_list) - 1, 0, -1):
            new_x = self.tur_list[seg_num - 1].xcor()
            new_y = self.tur_list[seg_num - 1].ycor()
            self.tur_list[seg_num].goto(new_x, new_y)
        self.tur_list[0].forward(Move_Distance)

    def up(self):
        if self.tur_list[0].heading() != 270:
            self.tur_list[0].setheading(90)

    def down(self):
        if self.tur_list[0].heading() != 90:
            self.tur_list[0].setheading(270)

    def left(self):
        if self.tur_list[0].heading() != 0:
            self.tur_list[0].setheading(180)

    def right(self):
        if self.tur_list[0].heading() != 180:
            self.tur_list[0].setheading(0)

    def reset(self):
        for seg in self.tur_list:
            seg.goto(1000,1000)
        self.tur_list.clear()
        self.create_snake()


