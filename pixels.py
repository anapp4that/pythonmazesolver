#contains our code to get usable data from our maze image

#iterate through pixel values array
def build_maze( pixel_values, pixels ):
    x = 1
    string = ''

    for pixel_values in pixel_values:
        string += str(pixel_values)
        #maybe set 10 in the next line to value of width so it prints the string by the width of the mace
        temp = x%10
        if temp==0 and x!=0:
            #save the string to our pixel array
            pixels.append(string)
            #reset our string
            string = ''
        x+= 1

#find where we enter and exit the maze
def find_door( line ):
    return line.find('1')

#prints the values stored in our pixels list
def print_maze( pixel_list ):
    #if our pixel array contains stuff
    if len(pixel_list) > 0:
        for pixel_strings in pixel_list:
            print(pixel_strings)
    #if there are no pixels
    else:
     print("Pixel array is empty")
