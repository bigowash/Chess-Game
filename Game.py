class Piece(object):

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

class Board(object):

    coordinates = ['-',
        'a1','a2','a3','a4','a5','a6','a7','a8','b1','b2','b3','b4','b5','b6','b7','b8','c1','c2','c3','c4','c5','c6','c7','c8','d1','d2','d3','d4','d5','d6','d7','d8','e1','e2','e3','e4','e5','e6','e7','e8','f1','f2','f3','f4','f5','f6','f7','f8','g1','g2','g3','g4','g5','g6','g7','g8','h1','h2','h3','h4','h5','h6','h7','h8']
    boardCoordinates = [(0,0),
        (0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(1,0),(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(2,0),(2,1),(2,2),(2,3),(2,4),(2,5),(2,6),(2,7),(3,0),(3,1),(3,2),(3,3),(3,4),(3,5),(3,6),(3,7),(4,0),(4,1),(4,2),(4,3),(4,4),(4,5),(4,6),(4,7),(5,0),(5,1),(5,2),(5,3),(5,4),(5,5),(5,6),(5,7),(6,0),(6,1),(6,2),(6,3),(6,4),(6,5),(6,6),(6,7),(7,0),(7,1),(7,2),(7,3),(7,4),(7,5),(7,6),(7,7)]

    def __init__(self):

        # self.board = [
        #     [Empty(),   Empty(),    Empty(),    Empty(),    Empty(),    Empty(),    Empty(),    Empty()],
        #     [Empty(),   Empty(),    Empty(),    Empty(),    Empty(),    Empty(),    Empty(),    Empty()],
        #     [Empty(),   Empty(),    Empty(),    Empty(),    Empty(),    Empty(),    Empty(),    Empty()],
        #     [Empty(),   Empty(),    Empty(),    Empty(),    Empty(),    Empty(),    Empty(),    Empty()],
        #     [Empty(),   Empty(),    Empty(),    Empty(),    Empty(),    Empty(),    Empty(),    Empty()],
        #     [Empty(),   Empty(),    Queen('w'),    Empty(),    Empty(),    Empty(),    Empty(),    Empty()],
        #     [Empty(),   Empty(),    Empty(),    Empty(),    Empty(),    Empty(),    Empty(),    Empty()],
        #     [King('b'),   Empty(),    Empty(),    Empty(),    Empty(),    Empty(),    Empty(),    Empty()],
        # ]
        
        #make a board
        self.board = [
            [Rook('b'),Knight('b'),Bishop('b'),Queen('b'),King('b'),Bishop('b'),Knight('b'),Rook('b')],
            [Pawn('b'), Pawn('b'), Pawn('b'), Pawn('b'), Pawn('b'), Pawn('b'), Pawn('b'), Pawn('b')],
            [Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty()],
            [Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty()],
            [Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty()],
            [Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty()],
            [Pawn('w'),Pawn('w'),Pawn('w'),Pawn('w'),Pawn('w'),Pawn('w'),Pawn('w'),Pawn('w'),Pawn('w')],
            [Rook('w'),Knight('w'),Bishop('w'),Queen('w'),King('w'),Bishop('w'),Knight('w'),Rook('w')]
        ]

        self.whiteKingPosition = (7,4)
        self.blackKingPosition = (0,4)

        # whitePiecesPositions = {'p1':(0,1),'p2':(1,1),'p3':(2,1),'p4':(3,1),'p5':(4,1),'p6':(5,1),'p7':(6,1),'p8':(7,1),'r1':(0,0),'n1':(1,0),'b1':(2,0),'q':(3,0),'k':(4,0),'b2':(5,0),'n2':(6,0),'r2':(7,0)}
        # blackPiecesPositions = {'p8':(0,6),'p7':(1,6),'p6':(2,6),'p5':(3,6),'p4':(4,6),'p3':(5,6),'p2':(6,6),'p1':(7,6),'r2':(0,7),'n2':(1,7),'b2':(2,7),'k':(3,7),'q':(4,7),'b1':(5,7),'n1':(6,7),'r1':(7,7)}

        self.whitePiecesPositions = {(6,0):'p8',(6,1):'p7',(6,2):'p6',(6,3):'p5',(6,4):'p4',(6,5):'p3',(6,6):'p2',(6,7):'p1',(7,0):'r2',(7,1):'n2',(7,2):'b2',(7,3):'q',(7,4):'k',(7,5):'b1',(7,6):'n1',(7,7):'r1'}
        self.blackPiecesPositions = {(1,0):'p1',(1,1):'p2',(1,2):'p3',(1,3):'p4',(1,4):'p5',(1,5):'p6',(1,6):'p7',(1,7):'p8',(0,0):'r1',(0,1):'n1',(0,2):'b1',(0,3):'q',(0,4):'k',(0,5):'b2',(0,6):'n2',(0,7):'r2'}

        #prints board
        self.print(True)

        # self.printWithCords()
        # self.printWithValues()

    def coordToRowAndCol(self, coord):
        '''takes letter coordinates and returns tuple of (row,col)'''
        coordiates = {'-':'-','a8':(0,0), 'a7':(1,0), 'a6':(2,0), 'a5':(3,0), 'a4':(4,0), 'a3':(5,0), 'a2':(6,0), 'a1':(7,0), 'b8':(0,1), 'b7':(1,1), 'b6':(2,1), 'b5':(3,1), 'b4':(4,1), 'b3':(5,1), 'b2':(6,1), 'b1':(7,1), 'c8':(0,2), 'c7':(1,2), 'c6':(2,2), 'c5':(3,2), 'c4':(4,2), 'c3':(5,2), 'c2':(6,2), 'c1':(7,2), 'd8':(0,3), 'd7':(1,3), 'd6':(2,3), 'd5':(3,3), 'd4':(4,3), 'd3':(5,3), 'd2':(6,3), 'd1':(7,3), 'e8':(0,4), 'e7':(1,4), 'e6':(2,4), 'e5':(3,4), 'e4':(4,4), 'e3':(5,4), 'e2':(6,4), 'e1':(7,4), 'f8':(0,5), 'f7':(1,5), 'f6':(2,5), 'f5':(3,5), 'f4':(4,5), 'f3':(5,5), 'f2':(6,5), 'f1':(7,5), 'g8':(0,6), 'g7':(1,6), 'g6':(2,6), 'g5':(3,6), 'g4':(4,6), 'g3':(5,6), 'g2':(6,6), 'g1':(7,6), 'h8':(0,7), 'h7':(1,7), 'h6':(2,7), 'h5':(3,7), 'h4':(4,7), 'h3':(5,7), 'h2':(6,7), 'h1':(7,7)}
        return coordiates[coord]

    def rowAndColToPiece(self, here):
        '''takes tuple of (row,col), returns piece(obj)'''
        #returns piece
        return self.board[here[0]][here[1]]

    def print(self, whiteTurn):
        '''prints the board facing whoevers turn it is (whiteTurn)'''
        #initialize markers
        letters = ['a','b','c','d','e','f','g','h']
        rows = ['8','7','6','5','4','3','2','1']
        
        if whiteTurn == True:

            #header
            print('\nWHITE TURN\n')
            print('    ', end='')
            for letter in letters:
                print(letter, end='   ')
            print()

            #rows
            for row in range(8):
                #row number
                print('  |___|___|___|___|___|___|___|___|')
                print(rows[row]+''+' |',end='')

                #cols
                for col in range(8):
                    print(' '+self.board[row][col].tag+' |', end='')
                #row number
                print(' '+rows[row])

            #bottom
            print('  |___|___|___|___|___|___|___|___|')
            print('  ', end='')
            for letter in letters:
                print(' ',letter, end=' ')
            print('\n')
        else:
            #header
            print('\nBLACK TURN\n')
            print('    ', end='')
            for letter in reversed(letters):
                print(''+letter, end='   ')
            print()

            #rows
            for row in reversed(range(8)):
                #row number
                print('  |___|___|___|___|___|___|___|___|')
                print(rows[row]+''+' |',end='')

                #cols
                for col in reversed(range(8)):
                    print(' '+self.board[row][col].tag+' |', end='')
                #row number
                print(' '+rows[row])

            #bottom
            print('  |___|___|___|___|___|___|___|___|')
            print('  ', end='')
            for letter in reversed(letters):
                print(' ',letter, end=' ')
            print('\n')

    def movePiece(self, piece, here, there, whiteTurn):
        '''takes piece (obj), here, there (tuple)s, whiteTurn (bool)
        Moves piece from here to there, printing the board facing the next player
        '''

        pieceThere = self.board[there[0]][there[1]]

        #updating the piece's positions
        self.board[there[0]][there[1]] = piece
        self.board[here[0]][here[1]] = Empty()

        if piece.name == 'Pawn':

            #for en passant
            if pieceThere.name == 'Empty' and here[1] != there[1]:            
                pieceThere = self.board[there[0]][there[1]]
                self.board[here[0]][there[1]] = Empty() #this removes the eaten piece
                
                if piece.color == 'w':

                    #updates positions of pieces
                    self.whitePiecesPositions[there] = self.whitePiecesPositions[here]
                    self.whitePiecesPositions.pop(here)

                    #removes position of eaten piece from dictionary
                    self.blackPiecesPositions.pop((here[0],there[1]))

                else:

                    #updates positions of pieces
                    self.blackPiecesPositions[there] = self.blackPiecesPositions[here]
                    self.blackPiecesPositions.pop(here)

                    #removes position of eaten piece from dictionary
                    self.whitePiecesPositions.pop((here[0],there[1]))

                #prints board ready for next player
                self.print(not whiteTurn)

                return pieceThere
            
            #check if pawn reaches end
            elif whiteTurn and there[0] == 0 or not whiteTurn and there[0] == 7:
                done = False
                while not done:
                    print('\nPlease select a piece:')
                    newPiece = input('queen (q), knight (k), bishop (b), rook (r): ')
                    if newPiece == 'q':
                        if whiteTurn:
                            self.board[there[0]][there[1]] = Queen('w')
                        else:
                            self.board[there[0]][there[1]] = Queen('b')
                        done = True
                    elif newPiece == 'b':
                        if whiteTurn:
                            self.board[there[0]][there[1]] = Bishop('w')
                        else:
                            self.board[there[0]][there[1]] = Bishop('b')
                        done = True
                    elif newPiece == 'k':
                        if whiteTurn:
                            self.board[there[0]][there[1]] = Knight('w')
                        else:
                            self.board[there[0]][there[1]] = Knight('b')
                        done = True
                    elif newPiece == 'r':
                        if whiteTurn:
                            self.board[there[0]][there[1]] = Rook('w')
                        else:
                            self.board[there[0]][there[1]] = Rook('b')
                        done = True
                        

        #castle
        if piece.name == 'King' and abs(here[1]-there[1])>1:
            small = abs(here[1]-there[1]) == 2

            if small:
                rook = self.board[here[0]][7]
                rook.moved = True

                self.board[here[0]][5] = rook
                self.board[here[0]][7] = Empty()

                if whiteTurn:
                    self.whitePiecesPositions[(7,5)] = self.whitePiecesPositions[(7,7)]
                    self.whitePiecesPositions.pop((7,7))
                
                else:
                    self.blackPiecesPositions[(0,5)] = self.blackPiecesPositions[(0,7)]
                    self.blackPiecesPositions.pop((0,7))
            
            else:
                rook = self.board[here[0]][0]
                rook.moved = True

                self.board[here[0]][2] = rook
                self.board[here[0]][0] = Empty()

                if whiteTurn:
                    self.whitePiecesPositions[(7,2)] = self.whitePiecesPositions[(7,0)]
                    self.whitePiecesPositions.pop((7,0))
                
                else:
                    self.blackPiecesPositions[(0,2)] = self.blackPiecesPositions[(0,0)]
                    self.blackPiecesPositions.pop((0,0))

        #prints board ready for next player
        self.print(not whiteTurn)

        #updates pieces' new position
        if piece.color == 'w':
            if piece.name == 'King':
                self.whiteKingPosition = there
            
            #updates positions of pieces
            self.whitePiecesPositions[there] = self.whitePiecesPositions[here]
            self.whitePiecesPositions.pop(here)

            #update for eaten pieces
            if pieceThere.color == 'b':
                self.blackPiecesPositions.pop(there)

        else:
            if piece.name == 'King':
                self.blackKingPosition = there
            
            #updates positions of pieces
            self.blackPiecesPositions[there] = self.blackPiecesPositions[here]
            self.blackPiecesPositions.pop(here)

            #update for eaten pieces
            if pieceThere.color == 'w':
                self.whitePiecesPositions.pop(there)
        
        #update fact that piece has moved if either king or rook
        try:
            piece.moved = True
        except Exception:
            pass

        #to update game variables
        return pieceThere

    def hasObstacles(self, piece, here, there, movement, whiteTurn):
        '''Takes piece (obj), here (tuple), there (tuple), movement (str), whiteTurn
        Assumes that the here and there work corresponding to piece
        returns True if it HAS an obstacle (BAD)
        reutns False if it does not have an obstacle (GOOD)
        '''
        # print(self.board)
        pieceThere = self.board[there[0]][there[1]]

        #checks end piece color (if eating own piece)
        if (whiteTurn and pieceThere.color != 'w') or (not whiteTurn and pieceThere.color != 'b'):

            #checks if not Knight or King
            if piece.obstacles:
                if movement == 'horizontal':
                    row = here[0]
                    start = here[1]
                    end = there[1]

                    #switches variables
                    if start > end:
                        start, end = end, start

                    #iterates through middle pieces
                    for col in range(start+1, end):
                        
                        #checks for obstacles
                        if self.board[row][col].name != 'Empty':
                            return True
                    return False

                elif movement == 'vertical':
                    col = here[1]
                    start = here[0]
                    end = there[0]

                    #switches variables
                    if start > end:
                        start, end = end, start

                    #iterates through middle pieces
                    for row in range(start+1, end):
                        
                        if self.board[row][col].name != 'Empty':
                            return True
                    return False

                elif movement == 'diagonalUp': 
                    total = here[0] + here[1]
                    
                    #considering rows
                    start = here[0]
                    end = there[0]

                    #switches variables
                    if start > end:
                        start, end = end, start

                    #iterates through middle pieces
                    for row in range(start+1, end):

                        col = total - row

                        #checks for obstacles
                        if self.board[row][col].name != 'Empty':
                            return True
                    return False

                elif movement == 'diagonalDown': 
                    total = here[0] - here[1]

                    #considering rows
                    start = here[0]
                    end = there[0]

                    #switches variables
                    if start > end:
                        start, end = end, start

                    #iterates through middle pieces
                    for row in range(start+1, end):
                        
                        col = row - total

                        #checks for obstacles
                        if self.board[row][col].name != 'Empty':
                            return True
                    return False
             
                elif movement == 'pawn-move':

                    #checks if it jumps over a piece
                    if piece.jump: 
                        middle = (here[0]+there[0])/2
                        if middle%1 == 0:
                            if self.board[int(middle)][here[1]].name != 'Empty':
                                return True
                                    
                    #checks diagonal movement is justified by eating
                    elif piece.diagonalPawnMove and ((whiteTurn and pieceThere.color != 'b') or (not whiteTurn and pieceThere.color != 'w')):
                        return True
                    
                    #check if moving forward
                    if not piece.diagonalPawnMove and pieceThere.color == '':
                        return False
                    return True
            
            return False
        return True

    def orderPositions(self, place, listOfPlaces):
        '''takes a position and a list, returns dictionary of list split in two where place was
        removes place i think
        farthest to closest i think'''
        #returns a dictionary
        #seperate into two lists with 

        left = []
        right = []
        half = False

        for position in listOfPlaces:
            if position == place:
                half = True
                #makes sure that here position is not taken
                continue

            if half:
                right.append(position)
            else:
                left.append(position)

        #only returns the lists containing positions 
        if left == []:
            dictionary = {'right':right[::-1]}
        elif right == []:
            dictionary = {'left':left}
        
        else:
            dictionary = {'left':left,'right':right[::-1]}

        return dictionary

    def checkLines(self, kingPosition, movement, line, whiteTurn, here = None):
        '''takes a line of positions and a direction
        
        returns boolean of whether or not piece straying from line endangers king
        true = bad
        false = good'''       

        #gets dictionary of left and right sides
        placesDict = self.orderPositions(kingPosition, line)

        #in case there is no here (because were just checking 
        #if kingIsChecked not if moving piece (can move))
        if here != None:

            for listOfPlaces in placesDict.values():
                #keeps only the side with the moved piece
                if here in listOfPlaces:
                    break
                
            #makes list go from closest to farthest
            listOfPlaces.reverse()

            #gets list of positions after moved piece
            afterPiecePlaces = []
            keep = False
            for i in listOfPlaces:
                if i == here:
                    keep = True
                    continue
                if keep:
                    afterPiecePlaces.append(i)
                else:
                    #checks if in between piece and king there is a piece, in which case
                    #king is already checked (function kingCheckedMoved gived a list of possible actions)
                    #or king will stay unchecked regardless of movement of piece
                    if self.rowAndColToPiece(i).name != 'Empty':
                        return False  

            listOfPlaces = afterPiecePlaces

            #iterates through positions after moved piece
            #checks if piece in that position threatens the king
            for place in listOfPlaces:
                piece = self.rowAndColToPiece(place)
                
                #makes sure place is not empty or is occupied by pawn, king, knight
                if piece.kingDanger:
                    #if piece of same color: king is safe
                    if whiteTurn and piece.color == 'w' or not whiteTurn and piece.color == 'b':
                        break #out of this line
                    
                    #if pieceThere can move in this direction 
                    #ie threaten the king from that line
                    if movement in piece.movement:
                        return True
            
                #this is the issue?
                elif whiteTurn and piece.color == 'w' or not whiteTurn and piece.color == 'b':
                    break


        #no here, check both directions
        else:
            for listOfPlaces in placesDict.values():

                #makes list go from closest to farthest
                listOfPlaces.reverse()  

                #iterates through positions after moved piece
                #checks if piece in that position threatens the king
                for place in listOfPlaces:
                    piece = self.rowAndColToPiece(place)
                    
                    #makes sure place is not empty or is occupied by pawn, king, knight
                    if piece.kingDanger:
                        #if piece of same color: king is safe
                        if whiteTurn and piece.color == 'w' or not whiteTurn and piece.color == 'b':
                            break #out of this line
                        
                        #if pieceThere can move in this direction 
                        #ie threaten the king from that line
                        if movement in piece.movement:
                            return True
                        break
                
                    #occupied by pawn, king, knight, empty
                    elif whiteTurn and piece.color == 'w' or not whiteTurn and piece.color == 'b':
                        break
                    elif piece.name != 'Empty':
                        break


        return False     

    def getDiagonals(self, here):
        '''returns dictionary {'diagonalUp':[list of tuples], 'diagonalDown':[list of tuples]}'''
        totalUp = here[0]+here[1]
        totalDown = here[0]-here[1]

        lines = {'diagonalUp':[],
                'diagonalDown':[]}
            
        diagonalUp = []
        diagonalDown = []

        for i in range(8):

            #adding diagonalUp
            diagonalUp.append((7-i,totalUp-7+i))

            #adding diagonalDown
            diagonalDown.append((i,i-totalDown))

        #make sure that the list does not exceed the limits of the board
        for place in diagonalUp:
            if place in Board.boardCoordinates:
                lines['diagonalUp'].append(place)
        for place in diagonalDown:
            if place in Board.boardCoordinates:
                lines['diagonalDown'].append(place)
        
        return lines

    def sameLine(self, kingPosition, here):
        '''returns a string of a type of line:
        horizontal, vertical, diagonalUp, diagonalDown, or empty str '''
        
        totalUp = kingPosition[0]+kingPosition[1]
        totalDown = kingPosition[0]-kingPosition[1]
        
        if here[1] == kingPosition[1]:
            movement = 'vertical'
        elif here[0] == kingPosition[0]:
            movement = 'horizontal'
        elif here[0]+here[1] == totalUp:
            movement = 'diagonalUp'
        elif here[0]-here[1] == totalDown:          
            movement = 'diagonalDown'
        else:
            movement = ''
        return movement

    def isKingChecked(self, kingPosition, whiteTurn, here = None, direction = None):
        '''returns true = bad
            false = good'''

        #might also check the kings position    

        lines = {
            'horizontal':[(kingPosition[0],0),(kingPosition[0],1),(kingPosition[0],2),(kingPosition[0],3),(kingPosition[0],4),(kingPosition[0],5),(kingPosition[0],6),(kingPosition[0],7)],
            'vertical':[(0,kingPosition[1]),(1,kingPosition[1]),(2,kingPosition[1]),(3,kingPosition[1]),(4,kingPosition[1]),(5,kingPosition[1]),(6,kingPosition[1]),(7,kingPosition[1])]}
         
        diagonalLines = self.getDiagonals(kingPosition)

        lines['diagonalUp'] = diagonalLines['diagonalUp']
        lines['diagonalDown'] = diagonalLines['diagonalDown']

        #check every lines, every direction
        #return if king is ENDANGERED
        if here == None:

            for direction in lines:
                #check if danger
                if self.checkLines(kingPosition, direction, lines[direction], whiteTurn):
                    return True

            #check for pawns and knights
            if not self.checkKnight(kingPosition, whiteTurn) and not self.checkPawn(kingPosition, whiteTurn):
                return False

            else:
                return True
                    
        else:
            #check if piece on line threatens king
            return self.checkLines(kingPosition, direction, lines[direction], whiteTurn, here)

    def checkKnight(self, kingPosition, whiteTurn):
        
        row, col = kingPosition[0], kingPosition[1]
                    
        knights = [(row-1,col+2), (row-1,col-2), (row+1, col+2), (row+1, col-2), 
                    (row-2,col+1), (row-2,col-1), (row+2, col+1), (row+2, col-1)]

        for position in knights:

            #check if on board
            if position in Board.boardCoordinates:
                piece = self.rowAndColToPiece(position)

                #checks if opposite colored knight piece
                if piece.name == 'Knight' and (whiteTurn and piece.color == 'b' or not whiteTurn and piece.color == 'w'):
                    return True
        return False

    def checkPawn(self, kingPosition, whiteTurn):
        
        row, col = kingPosition[0], kingPosition[1]
                    
        if whiteTurn:
            pawns = [(row-1,col-1), (row-1, col+1)]
        else:
            pawns = [(row+1,col-1), (row+1, col+1)]
        
        for position in pawns:
            
            #check if on board
            if position in Board.boardCoordinates:
                piece = self.rowAndColToPiece(position)

                #checks if opposite colored pawn piece
                if piece.name == 'Pawn' and (whiteTurn and piece.color == 'b' or not whiteTurn and piece.color == 'w'):
                    return True
        return False

    def straysFromLine(self, kingPosition, there, direction):
        '''returns true if strays from line, false otherwise
        ie True might endanger king'''

        totalUp = kingPosition[0]+kingPosition[1]
        totalDown = kingPosition[0]-kingPosition[1]

        if there[1] == kingPosition[1] and direction == 'vertical':
                return False
        if there[0] == kingPosition[0] and direction == 'horizontal':
                return False
        if there[0]+there[1] == totalUp and direction == 'diagonalUp':
                return False
        if there[0]-there[1] == totalDown and direction == 'diagonalDown':
                return False
        return True

    def canMove(self, here, turnCount = 0.0):
        '''takes location (row,col), checks if the possibilities for moves is not empty, returns list of possible coords'''
        #Iterate through all the places on the board and keeps the valid positions

        #get moved piece
        piece = self.rowAndColToPiece(here)

        #gets dictionary of all possible places ON BOARD + own position 
        #without checking for obstacles
        places = piece.getPlaces(here)

        #turns dictionary into list
        returnedListOfPlaces = []
        listOfPlaces = []

        #removes places that have obstacles
        for movement in places.keys():
            
            #checks for bishop, rook, queen, and pawn
            if piece.obstacles:

                #changes the order of tuples from farthest to closest
                #and removes the here position
                directionList = self.orderPositions(here, places[movement])
                #ie {'left':[(list) (of) (tuples)], 'right':[list of tuples]}

                #direction is a list of positions
                for direction in directionList.values():

                    obstacle = True
                    for index in range(len(direction)):
                        
                        #checks for obstacles in path
                        if not self.hasObstacles(piece, here, direction[index], movement, piece.color == 'w'):
                            obstacle = False
                            break
                        
                    #adds rest of list but only if it has found an obstacle
                    if not obstacle:
                        listOfPlaces += direction[index:]
            #for knight, king
            else:
                for direction in places[movement]:
                        if not self.hasObstacles(piece, here, direction, movement, piece.color == 'w'):
                            listOfPlaces.append(direction)

        #additional checks for pawns (diagonals)
        if piece.name == 'Pawn':

            #for en passant
            leftSide = (here[0],here[1]-1)
            rightSide = (here[0],here[1]+1)

            #checking color of piece for direction
            if piece.color == 'w':
                
                left = (here[0]-1,here[1]-1)
                right = (here[0]-1,here[1]+1)

                #checks for an opponent on left diagonal
                if left in self.boardCoordinates and self.board[left[0]][left[1]].color == 'b':
                    listOfPlaces.append(left)
                
                #checks for an opponent on right diagonal
                if right in self.boardCoordinates and self.board[right[0]][right[1]].color == 'b':
                    listOfPlaces.append(right)

                #for en passant
                enPassantPiece = self.board[leftSide[0]][leftSide[1]]
                if enPassantPiece.name == 'Pawn' and leftSide in self.boardCoordinates and enPassantPiece.jumped == turnCount-0.5:
                    listOfPlaces.append(left)

                enPassantPiece = self.board[rightSide[0]][rightSide[1]]
                if enPassantPiece.name == 'Pawn' and rightSide in self.boardCoordinates and enPassantPiece.jumped == turnCount-0.5:
                    listOfPlaces.append(right)

            else:

                left = (here[0]+1,here[1]-1)
                right = (here[0]+1,here[1]+1)
                
                #checks for an opponent on left diagonal
                if left in self.boardCoordinates and self.board[left[0]][left[1]].color == 'w':
                    listOfPlaces.append(left)
                
                #checks for an opponent on right diagonal
                if right in self.boardCoordinates and self.board[right[0]][right[1]].color == 'w':
                    listOfPlaces.append(right)

                #for en passant: Checks if there is a piece to the left/right
                if leftSide in self.boardCoordinates:
                    enPassantPiece = self.board[leftSide[0]][leftSide[1]]
                    if enPassantPiece.name == 'Pawn' and leftSide in self.boardCoordinates and enPassantPiece.jumped == turnCount-0.5:
                        listOfPlaces.append(left)

                if rightSide in self.boardCoordinates:
                    enPassantPiece = self.board[rightSide[0]][rightSide[1]]
                    if enPassantPiece.name == 'Pawn' and rightSide in self.boardCoordinates and enPassantPiece.jumped == turnCount-0.5:
                        listOfPlaces.append(right)

        #gets position of king to check if moved piece is on the same line:
        kingPosition = self.blackKingPosition
        if piece.color == 'w':
            kingPosition = self.whiteKingPosition

        if piece.name != 'King':
            direction = self.sameLine(kingPosition, here)

            if direction != '':
                for position in listOfPlaces:
                    #checks if 1) piece is not knight or if piece could endanget king
                    if piece.name == 'Knight' or self.straysFromLine(kingPosition, position, direction):
                        
                        #move will automatically endangers king
                        if not self.isKingChecked(kingPosition, piece.color == 'w', here, direction):
                            returnedListOfPlaces.append(position)
            
                    #movement in line is safe
                    else:
                        returnedListOfPlaces.append(position)
                        
            else:
                returnedListOfPlaces += listOfPlaces
        
        #king
        else:
    
            #check for castle: if king has moved
            if not piece.moved:

                #check horizontal lines if empty
                line = {
                    'small':[(here[0],5),(here[0],6)],
                    'big':[(here[0],3),(here[0],2),(here[0],1)]}

                for side in line.values():
                    cant = False
                    for pos in side:
                        if self.rowAndColToPiece(pos).name != 'Empty':
                            cant = True
                            break #from this line
                        
                        #check if king would be endangered
                        if pos != (here[0],1) and self.isKingChecked(pos, piece.color == 'w'):
                            cant = True
                            break
                    
                    #check that nothing blocked castle and that rook hasnt been touched
                    if not cant:
                        if side == line['big'] and self.rowAndColToPiece((here[0],0)).name == 'Rook' and not self.rowAndColToPiece((here[0],0)).moved:
                            returnedListOfPlaces.append((here[0],2))
                        if side == line['small'] and self.rowAndColToPiece((here[0],7)).name == 'Rook' and not self.rowAndColToPiece((here[0],7)).moved:    
                            returnedListOfPlaces.append((here[0],6))                     
        
            #cant move to a place that endangers himself
            for position in listOfPlaces:

                #check if king in that position is dangerous
                if not self.isKingChecked(position, piece.color == 'w'):
                    returnedListOfPlaces.append(position)

        #return list of places
        return returnedListOfPlaces

    def rowAndColToCoord(self, here):
        '''takes tuple of (row,col) returns letter grid position'''
        coordinates = {(0,0):'a8',(0,1):'b8',(0,2):'c8',(0,3):'d8',(0,4):'e8',(0,5):'f8',(0,6):'g8',(0,7):'h8',(1,0):'a7',(1,1):'b7',(1,2):'c7',(1,3):'d7',(1,4):'e7',(1,5):'f7',(1,6):'g7',(1,7):'h7',(2,0):'a6',(2,1):'b6',(2,2):'c6',(2,3):'d6',(2,4):'e6',(2,5):'f6',(2,6):'g6',(2,7):'h6',(3,0):'a5',(3,1):'b5',(3,2):'c5',(3,3):'d5',(3,4):'e5',(3,5):'f5',(3,6):'g5',(3,7):'h5',(4,0):'a4',(4,1):'b4',(4,2):'c4',(4,3):'d4',(4,4):'e4',(4,5):'f4',(4,6):'g4',(4,7):'h4',(5,0):'a3',(5,1):'b3',(5,2):'c3',(5,3):'d3',(5,4):'e3',(5,5):'f3',(5,6):'g3',(5,7):'h3',(6,0):'a2',(6,1):'b2',(6,2):'c2',(6,3):'d2',(6,4):'e2',(6,5):'f2',(6,6):'g2',(6,7):'h2',(7,0):'a1',(7,1):'b1',(7,2):'c1',(7,3):'d1',(7,4):'e1',(7,5):'f1',(7,6):'g1',(7,7):'h1'}
        return coordinates[here]         
            
    #functions for making
    def printWithCords(self):
        #initialize markers
        letters = ['0','1','2','3','4','5','6','7']
        rows = ['0','1','2','3','4','5','6','7']
        
        #header
        print()
        print('    ', end='')
        for letter in letters:
            print(''+letter, end='   ')
        print()

        #rows
        for row in range(8):
            #row number
            print('  |___|___|___|___|___|___|___|___|')
            print(rows[row]+''+' |',end='')

            #cols
            for col in range(8):
                print(' '+self.board[row][col].tag+' |', end='')
            #row number
            print(' '+rows[row])

        #bottom
        print('  |___|___|___|___|___|___|___|___|')
        print('  ', end='')
        for letter in letters:
            print(' ',letter, end=' ')
        print('\n')

    def printWithValues(self):
        #initialize markers
        letters = ['0','1','2','3','4','5','6','7']
        rows = ['0','1','2','3','4','5','6','7']
        
        #header
        print()
        print('    ', end='')
        for letter in letters:
            print(''+letter, end='   ')
        print()

        #rows
        for row in range(8):
            #row number
            print('  |___|___|___|___|___|___|___|___|')
            print(rows[row]+''+' |',end='')

            #cols
            for col in range(8):
                print(' '+str(row-col)+' |', end='')
            #row number
            print(' '+rows[row])

        #bottom
        print('  |___|___|___|___|___|___|___|___|')
        print('  ', end='')
        for letter in letters:
            print(' ',letter, end=' ')
        print('\n')

class Game(object):

    points = {
        'Rook':5,
        'Knight':3,
        'Bishop':3,
        'Queen':9,
        'Pawn':1
    }

    def __init__(self):
        
        print('\nWelcome to Chess')

        playAgain = True
        while playAgain:

            #setup board
            self.board = Board()
 
            #setup player's turn
            self.whiteTurn = True

            self.coordinates = ''

            self.gotChecked = False
            self.blackKingChecked = False
            self.whiteKingChecked = False

            #setup game variables
            self.whiteAte = []
            self.blackAte = []

            self.whitePoints = 0
            self.blackPoints = 0

            self.turnCount = 0

            self.moves = []
            self.whiteMoves = []
            self.blackMoves = []

            self.input = []

            checkmate = False

            #setup recurring rounds
            gameOver = False
            while not gameOver: #can change this to while board.gameNotOver() function call
                
                #take HERE coordinate from user and transforms into row/col tuple
                #this function updates the class attribute self.hereCoordinates
                self.getHereCoordinates(self.whiteTurn, self.board)

                #master hack to move any piece to another location without checks
                if self.hereCoordinates == '-':
                    self.masterhack()
                    continue

                #returns a list of positions that here piece can take
                if self.gotChecked:
                    positions = self.checkedCanMove(self.hereCoordinates)
                else:
                    positions = self.board.canMove(self.hereCoordinates, self.turnCount)

                #checks that chosen piece has options 
                while positions == []:

                    print('\nYou have chosen a piece with no moves, please choose again!\n')
                    self.getHereCoordinates(self.whiteTurn, self.board)

                    if self.hereCoordinates != '-':
                        if self.gotChecked:
                            positions = self.checkedCanMove(self.hereCoordinates)
                        else:
                            positions = self.board.canMove(self.hereCoordinates, self.turnCount)
                    else:
                        print('Master Hack not available')

                #get moved piece
                self.piece = self.board.rowAndColToPiece(self.hereCoordinates)

                #shows available positions
                print('\nAvailable positions: ', end='')
                for coord in positions:
                    # print(positions)
                    print(self.board.rowAndColToCoord(coord)+', ', end='')
                print('\nTo choose another piece enter: '+self.board.rowAndColToCoord(self.hereCoordinates)+'\n')

                #gets there input
                self.getThereCoordinates(self.board)

                #lets user go back by choosing original coordinates, restarts turn
                if self.thereCoordinates == self.hereCoordinates:
                    print('\nPlease select a piece:')
                    continue

                #makes sure that there is valid
                while self.thereCoordinates != self.hereCoordinates:
                    if self.thereCoordinates not in positions:
                        print('\nPlease choose a position available to the piece.\n')
                        self.getThereCoordinates(self.board)
                    else:
                        break

                #lets user go back by choosing original coordinates, restarts turn
                if self.thereCoordinates == self.hereCoordinates:
                    print('\nPlease select a piece:')
                    continue

                #Checks for possible en passant 
                if self.piece.name == 'Pawn' and self.thereCoordinates[0]-self.hereCoordinates[0] == 2 or self.thereCoordinates[0]-self.hereCoordinates[0] == -2:
                    self.piece.jumped = self.turnCount
                    
                #moves pieces and prints out board (for next person)
                pieceThere = self.board.movePiece(self.piece, self.hereCoordinates, self.thereCoordinates, self.whiteTurn)

                #update game variables
                if pieceThere.name != 'Empty':
                    if self.whiteTurn:
                        self.whiteAte.append(pieceThere)
                        self.whitePoints += Game.points[pieceThere.name]
                    else:
                        self.blackAte.append(pieceThere)
                        self.blackPoints += Game.points[pieceThere.name]

                self.blackKingChecked, self.whiteKingChecked = False, False

                #check if a king has been checked
                if self.whiteTurn:
                    self.blackKingChecked = self.board.isKingChecked(self.board.blackKingPosition, False)
                else:
                    self.whiteKingChecked = self.board.isKingChecked(self.board.whiteKingPosition, True)

                if self.blackKingChecked or self.whiteKingChecked:
                    self.gotChecked = True
                else:
                    self.gotChecked = False

                #check if game over
                if self.gotChecked:

                    print('\nCheck!\n')

                    gameOver = self.isGameOver(self.whiteTurn)
                    
                    if gameOver:
                        print("\nCheckmate!\n")
                        checkmate = True

                    #undoes the switch of players done in isGameOver()
                    self.whiteTurn = not self.whiteTurn
                
                #stalemate: player has no more options
                else:
                    if self.getAllMoves(not self.whiteTurn, True):
                        print('\nStalemate!\n')
                        self.stats()
                        gameOver = True

                #get moves
                move = (self.hereCoordinates, self.thereCoordinates)
                self.moves.append(move)
                
                #adds moves and checks for threefold stalemate
                if self.whiteTurn:
                    self.whiteMoves.append(move)

                    if len(self.moves) >= 10:
                        lastFive = self.whiteMoves[-5:]
                        if lastFive[0] == lastFive[2] and lastFive[0] == lastFive[4]:
                            lastFive = self.blackMoves[-5:]
                            if lastFive[0] == lastFive[2] and lastFive[0] == lastFive[4]:
                                print('\nLast three moves repeated, Threefold Stalemate!')
                                gameOver = True
                else:
                    self.blackMoves.append(move)

                    if len(self.moves) >= 10:
                        lastFive = self.blackMoves[-5:]
                        if lastFive[0] == lastFive[2] and lastFive[0] == lastFive[4]:
                            lastFive = self.whiteMoves[-5:]
                            if lastFive[0] == lastFive[2] and lastFive[0] == lastFive[4]:
                                print('\nLast three moves repeated, Threefold Stalemate!\n')
                                gameOver = True

                #switch players
                self.whiteTurn = not self.whiteTurn

                #update turn count
                self.turnCount += 0.5

                for i in self.input:
                    print(i)
                print()

            #stalemate: 50 moves without eating
            if self.turnCount == 50.0 and self.blackPoints == 0 and self.whitePoints == 0:
                print('\n50 moves made, no piece eaten, stalemate!')
                gameOver = True

            self.stats(checkmate) #prints out the game statistics
            playAgain = self.playAgain()

    def stats(self, checkmate):
        '''prints out the stats at the end of the game'''
        if checkmate:    
            if self.whiteTurn:
                winner = 'Black'
                loser = 'White'
            else:
                winner = 'White'
                loser = 'Black'

            print(f'\n{winner} won!\n\nWhite had {self.whitePoints} point(s)\nBlack had {self.blackPoints} point(s)\n')
        else:
            print(f'\nWhite had {self.whitePoints} point(s)\nBlack had {self.blackPoints} point(s)\n')

    def playAgain(self):
        if input('would you like to play again?: \n').lower() in ['y','yes','ye','ya']:
            return True
        return False

    def normalize(self, coordinates):
        if coordinates != '-':
            newCoords = ''
            if coordinates[0].isalpha():
                newCoords += coordinates[0].lower()
                newCoords += coordinates[1]
            else:
                newCoords += coordinates[1].lower()
                newCoords += coordinates[0]
            return newCoords
        return '-'

    def notValidHereCoordinates(self, whiteTurn, input, board):
                       
        #check for valid coordinate
        if self.coordinates in board.coordinates:

            if self.coordinates != '-':

                #creates tuple of row and column 
                rowcol = board.coordToRowAndCol(self.coordinates)
    
                #takes piece and color of coordinate
                piece = board.rowAndColToPiece(rowcol)

                #checks for valid piece
                if piece.name != 'Empty':
                    if (whiteTurn and piece.color == 'w') or (not whiteTurn and piece.color == 'b'):
                        return False
                    else:
                        print('\nPlease select your own piece.\n')
                else:
                    print('\nPlease select coordinates containing piece.\n')
            else:
                return False
        else:
            print('\nPlease submit coordinates on the board\n')
        return True    

    def getHereCoordinates(self, whiteTurn, board):
        '''gets input from user (certain to be a piece that belongs to user)
            updates self.thereCoordinates into a tuple of (row,col)
        '''
        
        #choose valid coordinates
        wrongChoice = True
        while wrongChoice:

            self.coordinates = input('What piece would you like to move? (letter+number):\n') 
            
            self.input.append(self.coordinates)
            
            self.coordinates = self.normalize(self.coordinates)
            
            wrongChoice = self.notValidHereCoordinates(whiteTurn, self.coordinates, board)

        #update class attribute of coordinates
        self.hereCoordinates = board.coordToRowAndCol(self.coordinates)

    def getThereCoordinates(self, board): 
        '''gets input from user (certain to be a piece that belongs to user)
            updates self.thereCoordinates into a tuple of (row,col)
        '''

        def notValidThereCoordinates(board):
            self.coordinates = input('To where would you like to move? (letter+number):\n')

            self.input.append(self.coordinates)

            self.coordinates = self.normalize(self.coordinates)

            #check for valid coordinate
            if self.coordinates in board.coordinates:
                return False

            print('Please submit valid coordinates\n')
            return True    

        #choose valid coordinates
        while notValidThereCoordinates(board):
            pass

        #update class attribute of coordinates
        self.thereCoordinates = board.coordToRowAndCol(self.coordinates)

    def checkedCanMove(self, here):
        '''takes a piece, checks if piece, can move, and if in those moves, can defend king or not
        
        returns positions of possible places

        True means can move (good)
        False means cant move (bad)'''

        part = self.board.rowAndColToPiece(here)
        
        #cant castle is checked
        king = False
        if part.name == 'King':
            king = True
            part.moved = True

        positions = self.board.canMove(here, self.turnCount)

        if king:
            part.moved = False

        #has moves
        if positions != []:
            if not king:    
                returnedPositions = []
                for pos in positions:

                    piece = self.board.rowAndColToPiece(pos)

                    if self.whiteTurn:
                        
                        self.board.board[pos[0]][pos[1]] = Pawn('w')
                        result = self.board.isKingChecked(self.board.whiteKingPosition, self.whiteTurn)

                    else:
                        self.board.board[pos[0]][pos[1]] = Pawn('b')
                        result = self.board.isKingChecked(self.board.blackKingPosition, self.whiteTurn)
                    
                    #revert changes
                    self.board.board[pos[0]][pos[1]] = piece

                    if not result:
                        returnedPositions.append(pos)
            
            #piece chosen is king
            else:
                returnedPositions = []
                for pos in positions:

                    piece = self.board.rowAndColToPiece(pos)

                    if self.whiteTurn:
                        
                        #changes the king's position
                        self.board.board[self.board.whiteKingPosition[0]][self.board.whiteKingPosition[1]] = Empty()
                        self.board.board[pos[0]][pos[1]] = King('w')
                        result = self.board.isKingChecked(pos, self.whiteTurn)

                        #revert changes
                        self.board.board[self.board.whiteKingPosition[0]][self.board.whiteKingPosition[1]] = King('w')
                    else:

                        #changes the king's position
                        self.board.board[self.board.blackKingPosition[0]][self.board.blackKingPosition[1]] = Empty()
                        self.board.board[pos[0]][pos[1]] = King('b')
                        result = self.board.isKingChecked(pos, self.whiteTurn)

                        #revert changes
                        self.board.board[self.board.blackKingPosition[0]][self.board.blackKingPosition[1]] = King('b')

                    #revert changes
                    self.board.board[pos[0]][pos[1]] = piece

                    #if king not checked with move
                    if not result:
                        returnedPositions.append(pos)

        else:
            return positions
        return returnedPositions

    def isGameOver(self, whiteTurn):
        '''True = checkmate
        False = game is not over'''

        if whiteTurn:
            kingPosition = self.board.blackKingPosition
            
            # check if something on the diagonal 

        else:
            kingPosition = self.board.whiteKingPosition

        #maybe then cancel it and redo
        self.whiteTurn = not self.whiteTurn

        #checks if the king can move out of danger first
        if self.checkedCanMove(kingPosition) == []:
            
            lines = {
                'horizontal':[(kingPosition[0],0),(kingPosition[0],1),(kingPosition[0],2),(kingPosition[0],3),(kingPosition[0],4),(kingPosition[0],5),(kingPosition[0],6),(kingPosition[0],7)],
                'vertical':[(0,kingPosition[1]),(1,kingPosition[1]),(2,kingPosition[1]),(3,kingPosition[1]),(4,kingPosition[1]),(5,kingPosition[1]),(6,kingPosition[1]),(7,kingPosition[1])]}
         
            diagonalLines = self.board.getDiagonals(kingPosition)

            lines['diagonalUp'] = diagonalLines['diagonalUp']
            lines['diagonalDown'] = diagonalLines['diagonalDown']

            danger = []

            #check for attacks by rook, bishop and queen
            for direction in lines:

                #gets dictionary of left and right sides of king
                placesDict = self.board.orderPositions(kingPosition, lines[direction])

                #makes list go from closest to farthest
                for listOfPlaces in placesDict.values():
                    listOfPlaces.reverse()  

                    #iterates through positions
                    #checks if piece in that position threatens the king
                    for place in listOfPlaces:
                        piece = self.board.rowAndColToPiece(place)
                        
                        #makes sure place is not empty or is occupied by pawn, king, knight
                        if piece.kingDanger:
                            #if piece of same color: king is safe
                            if self.whiteTurn and piece.color == 'w' or not self.whiteTurn and piece.color == 'b':
                                break #out of this line
                            
                            #if pieceThere can move in this direction 
                            #ie threaten the king from that line
                            if direction in piece.movement:
                                danger.append((piece, place, listOfPlaces))
                                break
                
                        #if on that line, piece protects, change lines
                        elif self.whiteTurn and piece.color == 'w' or not self.whiteTurn and piece.color == 'b':
                            break
            
            #check for attacks by knight
            row, col = kingPosition[0], kingPosition[1]
                    
            knights = [(row-1,col+2), (row-1,col-2), (row+1, col+2), (row+1, col-2), 
                        (row-2,col+1), (row-2,col-1), (row+2, col+1), (row+2, col-1)]

            for position in knights:

                #check if on board
                if position in Board.boardCoordinates:
                    piece = self.board.rowAndColToPiece(position)

                    #checks if opposite colored knight piece
                    if piece.name == 'Knight' and (whiteTurn and piece.color == 'b' or not whiteTurn and piece.color == 'w'):
                        danger.append((piece, position, []))
            
            #checks for attacks by pawn
            if whiteTurn:
                pawns = [(row-1,col-1), (row-1, col+1)]
            else:
                pawns = [(row+1,col-1), (row+1, col+1)]
            
            for position in pawns:
                
                #check if on board
                if position in Board.boardCoordinates:
                    piece = self.board.rowAndColToPiece(position)

                    #checks if opposite colored pawn piece
                    if piece.name == 'Pawn' and (whiteTurn and piece.color == 'b' or not whiteTurn and piece.color == 'w'):
                        danger.append((piece, position, []))

        #iterate through the different attacks on king
        #danger = [(dangerPiece, dangerPosition, dangerLine), etc]
        
            notBlocked = len(danger)
            
            for attack in danger:
            #if you cant defend from ALL attacks, GG

                #dictionary of keys = positions / values = pieces that can go there
                placesICanGo = self.getAllMoves(self.whiteTurn)

                #check if player can block threat
                if attack[0].name != 'Knight':
                    
                    #gets list of positions in between king and threat (excluding extremities)
                    dangerLine = []
                    for temp in attack[2]:
                        if attack[1] == temp:
                            break
                        else:
                            dangerLine.append(temp)
                    
                    #if i can block attack then 
                    for place in dangerLine:
                        if place in placesICanGo.keys():
                            notBlocked -= 1
                            break #out of this attack
                    
                if notBlocked != 0:
                    #check if one can eat piece
                    if attack[1] in placesICanGo.keys():
                        notBlocked -=1
                        break #out of this attack

            if notBlocked == 0:
                return False
            return True
        return False

    def getAllMoves(self, whiteTurn, stalemate = False):
        '''returns a dictionary of 
        keys = positions
        values = pieces that can go there
        
        only to be used to check for checkmate because using function call 
        checked canmove (more rigourous than can move)
        
        also used for stalemate, checks for one option then returns bool'''
        
        moves = {}
        
        #gets list of piece positions
        if whiteTurn:
            places = self.board.whitePiecesPositions.keys()
        else:
            places = self.board.blackPiecesPositions.keys()
        
        #place is tuple coords of starting piece
        for place in places:

            #positions is a list of possible moves starting piece can go to
            positions = self.checkedCanMove(place)

            #check if player has at least one move
            if stalemate and positions != []:
                return False

            #i is there coord
            for i in positions:
                if i not in moves:
                    moves[i] = [self.board.rowAndColToPiece(place)]
                else:
                    moves[i].append(self.board.rowAndColToPiece(place))
        
        #check if no moves 
        if stalemate and moves == {}:
            return True

        return moves

    def getNumberOfRounds(self):
        '''returns the number of rounds'''
        return int(self.turnCount)

    def masterhack(self):
        here = input('master coordinates: enter here: ')
        there = input('master coordinates: enter there: ')

        here = self.board.coordToRowAndCol(here)
        there = self.board.coordToRowAndCol(there)

        self.piece = self.board.rowAndColToPiece(here)

        if input('switch turns: y or n: ') == 'y':
            self.whiteTurn = not self.whiteTurn

        self.board.movePiece(self.piece, here, there, not self.whiteTurn)

    def options(self):
        print('\nWhat would you like to do?\n\n')

game = Game()
 
#TO DO:

    #take inputs by clicking on the box
    #take game options by clicking on the options
