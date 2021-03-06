from PIL import Image
from pprint import pprint
#import our State class
from state import *
#import our search class
from search import *
#import our pixel class
from pixels import *

#our pixel variables
maze = Image.open( 'tiny.png' )
width, height = maze.size
#values of all pixels stored in arraylist one after another
pixel_values = list( maze.getdata() )
#global vars
length = len( pixel_values )
pixels = list()

#entry and exit variables set to -9999 for place holder
entry = -99999
exit  = -99999

#main method
def main():
    #get our maze from the image
    build_maze( pixel_values, pixels )
    #print( "Maze" )
    #print_maze( pixels )

    #find the entry on the first line
    entry = find_door( pixels[0] )
    #print( "Maze entrence is at 0," + str(entry) )

    #find the exit on the last line
    exit = find_door( pixels[-1] )
    #print( "Maze exit is at " + str(len(pixels)) + "," + str(exit) )

    #begin state
    begin= state( None, 0, entry)
    #print( "Begin state X: " + str(begin.x) + " Begin state Y: " + str(begin.y) )




#execute the main method
main()
