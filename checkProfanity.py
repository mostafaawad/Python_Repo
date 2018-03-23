import urllib

def read_text():
	
	file = open("E:\Developing\Workspaces\Python Workspace\movie_quotes.txt")
	content = file.read()
	#print content
	file.close()
	check_profanity(content)

def check_profanity(txt):
	con = urllib.urlopen("http://www.wdylike.appspot.com/?q="+txt)
	resp = con.read()
	#print resp
	con.close()

	if "true" in resp:
		print "Profanity Alert!!"
	elif "false" in resp:
		print "This document has no curse words!"
	else:
		print "Couldn't scan the document properly."


read_text()