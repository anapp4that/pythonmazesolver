#holds our current state for our maze solving
class state:
    #for this init function x and y will not be used when we dont have a parent
    def __init__( self,par, x, y ):
        #if no parent than it is the parent
        if par == None:
            self.x = x
            self.y = y
        #child node, copy previous state
        else:
            self.parent = par
            self.x = par.x
            self.y = par.y
