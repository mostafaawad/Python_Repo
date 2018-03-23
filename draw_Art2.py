import turtle

def drawDiammond(turtle_in):
	for i in range(4):
		turtle_in.forward(100)
		turtle_in.right(-45)
		if i % 2 == 0:
			turtle_in.right(-90)


def drawShape():
	window = turtle.Screen()
	window.bgcolor("grey")

	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("black")
	brad.speed(-1)
	flag = False
	forw = 0

	for i in range(1,91):
		if flag:
			forw = 200
			flag = False		
		else:
			forw = 250
			flag = True
		drawDiammond(brad)
		brad.right(4)
		brad.circle(100)
		brad.right(4)
	



	window.exitonclick()


	

#	dan = turtle.Turtle()
#	dan.shape("turtle")
#	dan.color("red")
#	dan.circle(100)
	

drawShape()