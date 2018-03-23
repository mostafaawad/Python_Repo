import turtle

def draw_square(turtle_in):
	for i in range(1,5):
		turtle_in.forward(200)
		turtle_in.right(90)


def drawShape():
	window = turtle.Screen()
	window.bgcolor("grey")

	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("black")
	brad.speed(-9)

	for i in range(1,91):
		draw_square(brad)
		brad.right(4)
	window.exitonclick()


	

#	dan = turtle.Turtle()
#	dan.shape("turtle")
#	dan.color("red")
#	dan.circle(100)
	

drawShape()