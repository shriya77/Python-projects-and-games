import turtle

wn = turtle.Screen()
wn.title("Cheese Clicker by @Shriya77")
wn.bgcolor("black")

wn.register_shape("cheese.gif")

cheese = turtle.Turtle()
cheese.shape("cheese.gif")
cheese.speed(0)

clicks = 0

pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(0, 400)
pen.write(f"Clicks: {clicks}", align="center", font=("Courier New", 32, "normal"))

def clicked(x, y):
    global clicks
    clicks += 1
    pen.clear()
    pen.write(f"Clicks: {clicks}", align="center", font=("Courier New", 32, "normal"))
    
cheese.onclick(clicked)

wn.mainloop()
