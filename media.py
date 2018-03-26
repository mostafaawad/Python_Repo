import webbrowser

class Movie:
	
	#class variable
	VALID_RATINGS = ["G","PG","PG-13","R"]
	
	#constructor method
	def __init__(self, title, storyline, pstr_img, trailerURL):
		#instance variables
		self.title = title
		self.storyline = storyline
		self.pstr_img = pstr_img
		self.trailerURL = trailerURL
	
	#instance method
	def show_trailer(self):
		webbrowser.open(self.trailerURL)