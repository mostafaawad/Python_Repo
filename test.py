#s = ''
#print ('a' + s)[1:]
##print s[0] + s[1:]
#print s + ''
#print s[0:]
#------------------------------------------------
# Given the variables s and t defined as:
s = 'udacity'
t = 'bodacious'
# write Python code that prints out udacious
# without using any quote characters in
# your code.
print s[0] + t[t.find(s[1:4]):]