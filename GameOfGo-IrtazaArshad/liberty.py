from piece import Piece

class liberties(object):
    Piece = Piece.NoPiece
    liberties = 0
    x = -1
    y = -1
    def __init__(self, Piece,x,y):  # a contstuctor initialising variables
        self.Piece = Piece
        self.liberties = 0
        self.x = x
        self.y = y
    def getPiece(self): # a methoad to return Piece
        return self.Piece
    def getLiberties(self): # return Liberties
        return self.liberties
    def setLiberties(self,liberties):   # set Liberties
        self.liberties =liberties
    def getup(self,boardArray):
        if self.y == 0:
            return None
        else :
            return boardArray[self.y-1][self.x] # move upwards
    def getright(self,boardArray):
        if self.x == 6:
            return None
        else :
            return boardArray[self.y][self.x+1] # move right
    def getleft(self,boardArray):
        if self.x == 0:
            return None
        else :
            return boardArray[self.y][self.x-1] # move  left
    def getdown(self,boardArray):
        if self.y == 6:
            return None
        else :
            return boardArray[self.y+1][self.x] # move  downwards


