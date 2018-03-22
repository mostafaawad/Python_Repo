import turtle

def draw_square(x_turtle):
    for i in range(1,5):
        x_turtle.forward(200)
        x_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor('grey')
    t = turtle.Turtle()
    t.shape('turtle')
    t.color('black')
    t.speed(-1)
    for i in range(1,73):
        t.circle(150)
        t.right(5)
    window.exitonclick()

draw_art()

