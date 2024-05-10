from turtle import Turtle

class Line(Turtle):
    
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.left(90)
        self.forward(300)
        self.left(180)
        self.forward(600)
        self.penup()
        self.hideturtle()
        self.goto(0, 0)
        self.pendown()
        self.left(90)
        self.forward(5)
        self.left(180)
        self.forward(10)
        
    