class parent:
    def __init__(self, lastName, eyeColor):
        print "parent constructor called"
        self.lastName = lastName
        self.eyeColor = eyeColor

    def show_info(self):
        print "Lastname is: " + self.lastName
        print "Eye color is: " + self.eyeColor

class child(parent):
    def __init__(self, lastName, eyeColor, toysNumber):
        print "child constructor called"
        parent.__init__(self, lastName, eyeColor)
        self.toysNumber = toysNumber

#Overriding parent method
    def show_info(self):
        print "Lastname is: " + self.lastName
        print "Eye color is: " + self.eyeColor
        print "Number of toys are: " + str(self.toysNumber)

dad = parent("cyrus", "blue")
#print dad.lastName

#dad.show_info()

daughter = child("cyrus", "blue", 5)
daughter.show_info()
#print daughter.lastName
#print daughter.toysNumber
