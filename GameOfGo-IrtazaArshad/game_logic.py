from piece import Piece
from liberty import liberties


class GameLogic():

    print("Game Logic Object Created")
    # TODO add code here to manage the logic of your game
    turn = Piece.White
    xPosition = 0
    yPosition = 0
    boardArray = 0
    whitetaken = 0
    blacktaken = 0
    whiteterritories = 0
    blackterritories = 0


    def updateparams(self,boardArray,xpos,ypos):
        # update current variables
        self.xPosition = xpos
        self.yPosition = ypos
        self.boardArray=boardArray

    def checklogic(self,boardArray,xpos,ypos):
        # update current variables
        self.xPosition = xpos
        self.yPosition = ypos
        self.boardArray=boardArray

    def emptyCheck(self):
        if self.boardArray[self.yPosition][self.xPosition].Piece==Piece.NoPiece :
            return True
        else :
            return False

    def placestone(self):
        # function to place the stone on the board
        if self.turn == Piece.Black:
            self.boardArray[self.yPosition][self.xPosition].Piece = Piece.Black
        else:
            self.boardArray[self.yPosition][self.xPosition].Piece = Piece.White

    def captures(self):
        # update captures of entire board, i.e. remove all stone who have 0 liberties left
        for row in self.boardArray :
            for pos in row :
                if(pos.liberties==0 and pos.Piece != Piece.NoPiece):
                    if(pos.Piece== Piece.Black):
                        self.whitetaken=self.whitetaken+1
                        self.boardArray[pos.y][pos.x]=liberties(Piece.NoPiece, pos.x, pos.y)
                        print("Black Stone Captured at x: "+str(pos.x) + ", y: "+str(pos.y))
                        return "Black Stone Captured at x: "+str(pos.x) + ", y: "+str(pos.y)
                    elif(pos.Piece== Piece.White):
                        self.blackprisoners=self.blacktaken+1
                        self.boardArray[pos.y][pos.x] = liberties(Piece.NoPiece, pos.x, pos.y)
                        print("White Stone Captured at x: " + str(pos.x) + ", y: " + str(pos.y))
                        return "White Stone Captured at x: " + str(pos.x) + ", y: " + str(pos.y)

    def updatecaptures(self):
        # With this method we found the most difficulties so we had to take some help online we saw some tutorials and blogs about the game of
        # go capturing algorithms and found some helpfull code as well
        if self.boardArray[self.yPosition][self.xPosition].getup(self.boardArray) != None and self.boardArray[self.yPosition][self.xPosition].getup(self.boardArray).liberties == 0 and self.boardArray[self.yPosition][self.xPosition].getup(self.boardArray).Piece != Piece.NoPiece:
            return self.capturePiece(self.xPosition, self.yPosition - 1)
        elif  self.boardArray[self.yPosition][self.xPosition].getright(self.boardArray) != None and self.boardArray[self.yPosition][
                self.xPosition].getright(self.boardArray).liberties == 0 and self.boardArray[self.yPosition][
                self.xPosition].getright(self.boardArray).Piece != Piece.NoPiece :
            return self.capturePiece(self.xPosition + 1, self.yPosition)
        elif  self.boardArray[self.yPosition][self.xPosition].getleft(self.boardArray) != None and self.boardArray[self.yPosition][
                self.xPosition].getleft(self.boardArray).liberties == 0 and self.boardArray[self.yPosition][
                self.xPosition].getleft(self.boardArray).Piece != Piece.NoPiece :
            return self.capturePiece(self.xPosition - 1, self.yPosition)
        elif  self.boardArray[self.yPosition][self.xPosition].getdown(self.boardArray) != None and self.boardArray[self.yPosition][
                self.xPosition].getdown(self.boardArray).liberties == 0 and self.boardArray[self.yPosition][
                self.xPosition].getdown(self.boardArray).Piece != Piece.NoPiece :
            return self.capturePiece(self.xPosition, self.yPosition + 1)
    def capturePiece(self,xpos,ypos):
        # captures a piece at the given position
        if self.boardArray[ypos][xpos].Piece == 1:  # if the piece is white
            self.blacktaken = self.blacktaken + 1
            self.boardArray[ypos][xpos] = liberties(Piece.NoPiece, xpos, ypos)
            return "White Stone is Captured at x: " + str(xpos) + ", y: " + str(ypos)
        else:  # if the piece is black
            self.whitetaken = self.whitetaken + 1
            self.boardArray[ypos][xpos] = liberties(Piece.NoPiece, xpos, ypos)
            return "Black Stone is Captured at x: " + str(xpos) + ", y: " + str(ypos)

    def liberties(self):
        # update the liberties of all the available stones
        for row in self.boardArray:
            for move in row:
                count = 0
                if move.Piece != Piece.NoPiece:
                    Stonecolor = move.Piece
                    if move.getup(self.boardArray) != None and (
                            move.getup(self.boardArray).Piece == Stonecolor or move.getup(
                            self.boardArray).Piece == Piece.NoPiece):
                        count = count + 1
                    if move.getright(self.boardArray) != None and (
                            move.getright(self.boardArray).Piece == Stonecolor or move.getright(
                            self.boardArray).Piece == Piece.NoPiece):
                        count = count + 1
                    if move.getleft(self.boardArray) != None and (
                            move.getleft(self.boardArray).Piece == Stonecolor or move.getleft(
                            self.boardArray).Piece == Piece.NoPiece):
                        count = count + 1
                    if move.getdown(self.boardArray) != None and (
                            move.getdown(self.boardArray).Piece == Stonecolor or move.getdown(
                            self.boardArray).Piece == Piece.NoPiece):
                        count = count + 1
                    move.setLiberties(count)
    def validMove(self):
        if self.turn==Piece.Black :
            oppositeplayer=Piece.White
        else :
            oppositeplayer =Piece.Black
        count=0
        # counts the neighbouring positions for opposite color
        if self.boardArray[self.yPosition][self.xPosition].getup(self.boardArray) == None or self.boardArray[self.yPosition][self.xPosition].getup(self.boardArray).Piece == oppositeplayer :
            count=count+1
        if self.boardArray[self.yPosition][self.xPosition].getleft(self.boardArray) == None or self.boardArray[self.yPosition][self.xPosition].getleft(self.boardArray).Piece == oppositeplayer :
            count = count + 1
        if self.boardArray[self.yPosition][self.xPosition].getright(self.boardArray) == None or self.boardArray[self.yPosition][self.xPosition].getright(self.boardArray).Piece == oppositeplayer :
            count = count + 1
        if self.boardArray[self.yPosition][self.xPosition].getdown(self.boardArray) == None or self.boardArray[self.yPosition][self.xPosition].getdown(self.boardArray).Piece == oppositeplayer :
            count = count + 1
        if(count==4) :
            if self.boardArray[self.yPosition][self.xPosition].getup(self.boardArray) != None and self.boardArray[self.yPosition][
                self.xPosition].getup(self.boardArray).liberties == 1:
                return False
            if self.boardArray[self.yPosition][self.xPosition].getleft(self.boardArray) != None and self.boardArray[self.yPosition][
                self.xPosition].getleft(self.boardArray).liberties == 1:
                return False
            if self.boardArray[self.yPosition][self.xPosition].getright(self.boardArray) != None and self.boardArray[self.yPosition][
                self.xPosition].getright(self.boardArray).liberties == 1:
                return False
            if self.boardArray[self.yPosition][self.xPosition].getdown(self.boardArray) != None and self.boardArray[self.yPosition][
                self.xPosition].getdown(self.boardArray).liberties == 1:
                return False
            return True
        else :
            return False

    def getBlackPrisoner(self):
        return str(self.blacktaken)
    def getWhitePrisoner(self):
        return str(self.whitetaken)
    def getBlackTerritories(self):
        return str(self.blackterritories)
    def getWhiteTerritories(self):
        return str(self.whiteterritories)
    def updateTeritories(self):
        # update the current positions occupied by each player
        blacks = 0
        whites = 0
        for row in self.boardArray:
            for cell in row:
                if cell.Piece == Piece.Black:
                    blacks = blacks + 1
                elif cell.Piece == Piece.White:
                    whites=whites+1
        self.whiteterritories=whites
        self.blackterritories=blacks
    def getScore(self,Piece):
        if Piece==2:
            return self.blackterritories+self.blacktaken
        else:
            return self.whiteterritories+ self.whitetaken

    def changeturn(self):
        # function to swap turns
        print("turn changed")
        if self.turn == Piece.Black:
            self.turn = Piece.White
        else:
            self.turn = Piece.Black







