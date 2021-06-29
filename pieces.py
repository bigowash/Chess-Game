class Piece():

    boardCoordinates = [(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(1,0),(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(2,0),(2,1),(2,2),(2,3),(2,4),(2,5),(2,6),(2,7),(3,0),(3,1),(3,2),(3,3),(3,4),(3,5),(3,6),(3,7),(4,0),(4,1),(4,2),(4,3),(4,4),(4,5),(4,6),(4,7),(5,0),(5,1),(5,2),(5,3),(5,4),(5,5),(5,6),(5,7),(6,0),(6,1),(6,2),(6,3),(6,4),(6,5),(6,6),(6,7),(7,0),(7,1),(7,2),(7,3),(7,4),(7,5),(7,6),(7,7)]

    def __init__(self):
        pass
        
    def getPlaces(self, here):
        pass

class Rook(Piece):
    def __init__(self, color):
        self.name = 'Rook'
        self.tag = 'R'
        self.color = color
        self.obstacles = True
        self.movement = 'horizontalvertical'
        self.kingDanger = True
        self.moved = False

        if color == 'b':
            self.tag = self.tag.lower()
    
    def getPlaces(self, here):
        '''Takes a tuple of location, reads piece, returns list of tuples of possibles positions for piece'''
        places = {'horizontal':[], 'vertical':[]}

        #adds each position in straight row/col as a tuple
        for i in range(8):

            #adding horizontal
            places['horizontal'].append((here[0],i))

            #adding vertical
            places['vertical'].append((i,here[1]))
        
        # #returns dictionary without (here) position
        # places['horizontal'] = [i for i in places['horizontal'] if i != here]
        # places['vertical'] = [i for i in places['vertical'] if i != here]

        return places

class Knight(Piece):
    def __init__(self, color):
        self.name = 'Knight'
        self.tag = 'N'
        self.color = color
        self.obstacles = False
        self.kingDanger = False

        if color == 'b':
            self.tag = self.tag.lower()

    def getPlaces(self, here):
        '''Takes a tuple of location, reads piece, returns dictionary of tuples of all possibles positions for piece'''

        row = here[0]
        col = here[1]

        places = [(row-1,col+2), (row-1,col-2), (row+1, col+2), (row+1, col-2), 
                  (row-2,col+1), (row-2,col-1), (row+2, col+1), (row+2, col-1)]

        returnedPlaces = {'knight-move':[here]}

        for place in places:
            if place in super().boardCoordinates:
                returnedPlaces['knight-move'].append(place)

        #returns dictionary
        return returnedPlaces

class Bishop(Piece):
    def __init__(self, color):
        self.name = 'Bishop'
        self.tag = 'B'
        self.color = color
        self.obstacles = True
        self.movement = 'diagonalUpdiagonalDown'
        self.kingDanger = True

        if color == 'b':
            self.tag = self.tag.lower()

    def getPlaces(self, here):
        '''Takes a tuple of location, reads piece, returns dictionary of tuples of possibles positions for piece'''

        diagonalUp = []
        diagonalDown = []

        totalUp = here[0]+here[1]
        totalDown = here[0]-here[1]

        for i in range(8):

            #adding diagonalUp
            diagonalUp.append((7-i,totalUp-7+i))

            #adding diagonalDown
            diagonalDown.append((i,i-totalDown))
        
        places = {'diagonalUp':[], 'diagonalDown':[]}

        #only adds positions on board   
        for place in diagonalUp:
            if place in super().boardCoordinates:
                places['diagonalUp'].append(place)
        for place in diagonalDown:
            if place in super().boardCoordinates:
                places['diagonalDown'].append(place)

        return places

class King(Piece):
    def __init__(self, color):
        self.name = 'King'
        self.tag = 'K'
        self.color = color
        self.obstacles = False
        self.kingDanger = False
        self.moved = False

        if color == 'b':
            self.tag = self.tag.lower()

    def getPlaces(self, here):
        '''Takes a tuple of location, reads piece, returns list of tuples of possibles positions for piece'''
        row = here[0]
        col = here[1]
        
        places = [(row-1,col-1), (row-1,col), (row-1, col+1),
                  (row,col-1),                (row,col+1),
                  (row+1,col-1), (row+1,col), (row+1,col+1)]
        
        returnedPlaces = {'king-move':[here]}
        
        #adds positions on board
        for place in places:
            if place in super().boardCoordinates:
                returnedPlaces['king-move'].append(place)

        #returns dictionary
        return returnedPlaces

class Queen(Piece):
    def __init__(self, color):
        self.name = 'Queen'
        self.tag = 'Q'
        self.color = color
        self.obstacles = True
        self.movement = 'verticalhorizontaldiagonalUpdiagonalDown'
        self.kingDanger = True

        if color == 'b':
            self.tag = self.tag.lower()

    def getPlaces(self, here):
        '''Takes a tuple of location, reads piece, returns dictionary of tuples of possibles positions for piece'''
        
        places = {'horizontal':[], 'vertical':[]}

        totalUp = here[0]+here[1]
        totalDown = here[0]-here[1]

        diagonalUp = []
        diagonalDown = []

        #finding diagonal values
        for i in range(8):

            #adding diagonalUp
            diagonalUp.append((7-i,totalUp-7+i))

            #adding diagonalDown
            diagonalDown.append((i,i-totalDown))

        #finding straight values
        for i in range(8):

            #adding horizontal
            places['horizontal'].append((here[0],i))

            #adding vertical
            places['vertical'].append((i,here[1]))

        places['diagonalUp'] = []
        places['diagonalDown'] = []

        #adds diagonal positions on board   
        for place in diagonalUp:
            if place in super().boardCoordinates:
                places['diagonalUp'].append(place)
        for place in diagonalDown:
            if place in super().boardCoordinates:
                places['diagonalDown'].append(place)

        # #removes 'here' positions from diagonals
        # places['diagonalUp'] = [i for i in places['diagonalUp'] if i != here]
        # places['diagonalDown'] = [i for i in places['diagonalDown'] if i != here]

        return places

class Pawn(Piece):
    def __init__(self, color):
        self.name = 'Pawn'
        self.tag = 'P'
        self.color = color
        self.diagonalPawnMove = False
        self.jump = False
        self.obstacles = True
        self.kingDanger = False
        self.jumped = 0.1
        self.enPassant = ''
        
        if color == 'b':
            self.tag = self.tag.lower()

    def getPlaces(self, here):
        '''Takes a tuple of location, reads piece, returns list of tuples of possibles positions for piece, DOES NOT ACCOUNT FOR DIAGONAL EATING'''
        
        row = here[0]
        col = here[1]
        
        if self.color == 'w':
            #account for 'jump'
            if here in [(6,0),(6,1),(6,2),(6,3),(6,4),(6,5),(6,6),(6,7)]:
                self.jump = True
                places = [(row-1,col),(row-2,col)]
            #no 'jump'
            else:
                places = [(row-1,col)]

        elif self.color == 'b':  
            #account for 'jump'
            if here in [(1,0),(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7)]:
                self.jump = True
                places = [(row+1,col),(row+2,col)]
            #no 'jump'
            else:
                places = [(row+1,col)]
        
        returnedPlaces = {'pawn-move':[here]}
        
        #adds positions on board
        for place in places:
            if place in super().boardCoordinates:
                returnedPlaces['pawn-move'].append(place)

        #returns list
        return returnedPlaces

class Empty(Piece):
    def __init__(self):
        self.name = 'Empty'
        self.tag = ' '
        self.color = ''
        self.kingDanger = False
