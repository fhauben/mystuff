from sys import argv #lines -3 use argv to get a filename

script, filename = argv

txt = open(filename) #line 5 uses our new command, open

print "Here's your file %r:" % filename #line 7 prints a message 
print txt.read() 
#line 8 we have something new - 
# we call a function on txt named read; what you get back from open is a file, and it also has commands you can give it

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

