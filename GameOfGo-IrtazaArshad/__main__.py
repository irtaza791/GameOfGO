from PyQt5.QtWidgets import QApplication
from go import Go
import sys

app = QApplication([])
myGo = Go()
sys.exit(app.exec_())
