from PyQt5 import Qt
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QDockWidget, QVBoxLayout, QWidget, QLabel, \
    QPushButton, QTextEdit, QDialog, QFrame  # TODO import additional Widget classes as desired
from PyQt5.QtCore import pyqtSlot
from piece import Piece


class ScoreBoard(QDockWidget):
    '''# base the score_board on a QDockWidget'''

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        '''initiates ScoreBoard UI'''
        self.resize(200, 200)
        self.setFixedWidth(200)
        self.center()
        self.setWindowTitle('ScoreBoard')
        # create a widget to hold other widgets
        self.mainWidget = QWidget()
        self.mainWidget.setStyleSheet("background-color:white; border: 2px solid grey;")
        self.mainLayout = QVBoxLayout()


        # create two labels which will be updated by signals
        self.instructions = QLabel("Instructions \n \n 1. End Game: Press E \n 2. Reset Game: Press R \n 3. Pass Move: Press P ")
#        self.resignbtn = QPushButton("Resign", self)
#        self.resignbtn.setCheckable(True)
#        self.passbtn = QPushButton("Pass", self)
#        self.passbtn.setCheckable(True)
#        self.resetbtn = QPushButton("Reset", self)
#        self.resetbtn.setCheckable(True)
#        self.resignbtn.clicked.connect(self.passevent)
#        self.passbtn.clicked.connect(self.passevent)
  #      self.resetbtn.clicked.connect(self.passevent)



        self.label_turn = QLabel("Current Turn: ")
        self.label_turn.setStyleSheet("border-radius:20px; padding: 20px; ")
        self.label_clickLocation = QLabel("Click Location: ")
        self.label_clickLocation.setStyleSheet("border-radius:20px; padding: 20px;")
        self.label_timeRemaining = QLabel("Time remaining: ")
        self.label_timeRemaining.setStyleSheet("border-radius:20px; padding: 20px;")
        self.label_PrisonersBlack = QLabel("Captures by Black: ")
        self.label_PrisonersBlack.setStyleSheet("border-radius:20px; padding: 20px;")
        self.label_PrisonersWhite = QLabel("Captures by White: ")
        self.label_PrisonersWhite.setStyleSheet("border-radius:20px; padding: 20px;")
        self.label_TerritoriesBlack = QLabel("Black Territories: ")
        self.label_TerritoriesBlack.setStyleSheet("border-radius:20px; padding: 20px;")
        self.label_TerritoriesWhite = QLabel("White Territories: ")
        self.label_TerritoriesWhite.setStyleSheet("border-radius:20px; padding: 20px;")
        self.mainWidget.setLayout(self.mainLayout)
        # self.mainLayout.addWidget(self.passbutton)
        self.mainLayout.addWidget(self.instructions)
        self.mainLayout.addWidget(self.label_turn)
        self.mainLayout.addWidget(self.label_clickLocation)
        self.mainLayout.addWidget(self.label_timeRemaining)
        self.mainLayout.addWidget(self.label_PrisonersBlack)
        self.mainLayout.addWidget(self.label_PrisonersWhite)
        self.mainLayout.addWidget(self.label_TerritoriesBlack)
        self.mainLayout.addWidget(self.label_TerritoriesWhite)

        self.setWidget(self.mainWidget)
        self.show()

    def center(self):
        '''centers the window on the screen, you do not need to implement this method'''

    def make_connection(self, board):
        '''this handles a signal sent from the board class'''
        # when the clickLocationSignal is emitted in board the setClickLocation slot receives it
        board.clickLocationSignal.connect(self.setClickLocation)
        # when the updateTimerSignal is emitted in the board the setTimeRemaining slot receives it
        board.updateTimerSignal.connect(self.setTimeRemaining)
        # when the updatePrionersSignal is emitted in the board the updatePrisoners slot receives it
        board.updatePrionersSignal.connect(self.updatePrisoners)
        board.updateTerritoriesSignal.connect(self.updateTerritories)
        board.showNotificationSignal.connect(self.displaynotification)
        board.displaychangeturnSignal.connect(self.updateturn)

    @pyqtSlot(str)  # checks to make sure that the following slot is receiving an argument of the type 'int'
    def setClickLocation(self, clickLoc):
        '''updates the label to show the click location'''
        self.label_clickLocation.setText(clickLoc)
        # print('slot ' + clickLoc)

    @pyqtSlot(int)
    def setTimeRemaining(self, timeRemainng):
        '''updates the time remaining label to show the time remaining'''
        update = "Time Remaining:" + str(timeRemainng)
        if timeRemainng < 10:
            self.label_timeRemaining.setStyleSheet("color:red; font-size: 14px; border-radius:20px; padding: 20px;" )
        self.label_timeRemaining.setText(update)

    def updateturn(self, Piece):
        if (Piece == 1):
            self.label_turn.setText("Current Turn: White")
            self.label_turn.setStyleSheet("border-radius:20px; padding: 20px; background-color:white; color: black")
        elif (Piece == 2):
            self.label_turn.setText("Current Turn: Black")
            self.label_turn.setStyleSheet("border-radius:20px; padding: 20px; background-color:black; color: white")

    def updatePrisoners(self, n, Player):
        if (Player == Piece.Black):
            update = "Captures by Black: " + n
            self.label_PrisonersBlack.setText(update)
        elif (Player == Piece.White):
            update = "Captures by White: " + n
            self.label_PrisonersWhite.setText(update)

    def updateTerritories(self, n, Player):
        if (Player == Piece.Black):
            update = "Black territories: " + n
            self.label_TerritoriesBlack.setText(update)
        elif (Player == Piece.White):
            update = "White territories: " + n
            self.label_TerritoriesWhite.setText(update)

#    def passevent(self):
#        print("Pass clicked")
#        if self.passbtn.isChecked():
#            print("pass")
#            Go.getBoard().resetGame()
#        if self.resignbtn.isChecked():
#            print("resign")
#        if self.resetbtn.isChecked():
#            print("reset")

    def displaynotification(self, message):
        notifDiaglog = QDialog(self)
        notifDiaglog.setFixedWidth(300)
        notifDiaglog.setWindowTitle("Message!")
        self.modellayout = QVBoxLayout()
        self.modellayout.addWidget(QLabel(message))
        notifDiaglog.setLayout(self.modellayout)
        notifDiaglog.exec_()
