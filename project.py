from PIL import Image
from pprint import pprint
maze = Image.open('tiny.png')
width, height = maze.size
#values of all pixels stored in arraylist one after another
pixel_values = list(maze.getdata())

x = 1
string = ''
length = len(pixel_values)

#iterate through pixel values array
# for pixel_values in pixel_values:
#     string += str(pixel_values)
        #maybe set 10 in the next line to value of width so it prints the string by the width of the mace
#     temp = x%10
#     if temp==0 and x!=0:
#         print string
#         string = ''
#     x+= 1


def breadthfirst():

class state:
    #for this init function x and y will not be used when we
    def __init__(self,par, x, y):
        #if no parent than it is the parent
        if par = None:
            self.x = x
            self.y = y
        #child node, copy previous state
        else:
            self.parent = par
            self.x = par.x
            self.y = par.y
        
