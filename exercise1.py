'''
Name: Gloria Pappalardo
Date created: 9/18/20
Version of Python: 3.8
The input is a word, then indexing is ued the separate the word into two parts, capitalizing the start of each one.
Then concatenation is used to put the two capitalized parts back together.

'''

def capitalize_first_fourth(word):
# variables created to separate the argument into two parts
    x = word[0:3]
    y = word[3:len(word)]
# prints the sections concatenated and capitalized with the .capitalize() method
    print (x.capitalize() + y.capitalize())

capitalize_first_fourth('copernicus')
