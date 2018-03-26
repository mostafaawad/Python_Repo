class parent:
	def __init__(self,lastName,eyeColor):
		print "parent constructor called"
		self.lastName = lastName
		self.eyeColor = eyeColor

class child(parent):
	def __init__(self,lastName,eyeColor,toysNumber):
		print "child constructor called"
		parent.__init__(self,lastName,eyeColor)
		self.toysNumber = toysNumber

dad = parent("cyrus","blue")
print dad.lastName

daughter = child("cyrus","blue",5)
print daughter.lastName
print daughter.toysNumber
