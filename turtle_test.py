import turtle

def test():
    window = turtle.Screen()
    window.bgcolor('grey')

    dan = turtle.Turtle()
    dan.shape('turtle')
    dan.color('black')
    dan.speed(1)
    for i in range(1,9):
        dan.forward(50)
        dan.right(45)
    window.exitonclick()
test()




