from turtle import Turtle

class Rule(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("#C04936")
        self.goto(0, -120)
        self.write("* Don't forget to change your keyboard language into English *", align="center", font=("Courier", 9, "normal"))
        self.goto(0, -150)
        self.write("left side: press 'w' and 's' to control the paddle", align="center", font=("Courier", 13, "normal"))
        self.goto(0, -170)
        self.write("Right side: press 'up' and 'down' to control the paddle", align="center", font=("Courier", 13, "normal"))