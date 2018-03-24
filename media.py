import webbrowser

class Movie:
	def __init__(self, title, storyline, pstr_img, trailerURL):
		self.title = title
		self.storyline = storyline
		self.pstr_img = pstr_img
		self.trailerURL = trailerURL

	def show_trailer(self):
		webbrowser.open(self.trailerURL)