from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.goto(-200, 250)
        self.write(f"Player A : {self.l_score}", align="center", font=("Courier", 20, "normal"))
        self.goto(200, 250)
        self.write(f"Player B : {self.r_score}", align="center", font=("Courier", 20, "normal"))
        
    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()
        
    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()