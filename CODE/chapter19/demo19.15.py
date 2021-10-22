from PyQt5.QtWidgets import (QWidget, QHBoxLayout, 
    QLabel, QApplication)
from PyQt5.QtGui import QPixmap
import sys

class Pixmap(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):      

        hbox = QHBoxLayout(self)
        pixmap = QPixmap("face.png")

        lbl = QLabel(self)
        lbl.setPixmap(pixmap)

        hbox.addWidget(lbl)
        self.setLayout(hbox)
        self.move(300, 200)
        self.setWindowTitle('显示图像（QPixmap控件）')
        self.show()        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Pixmap()
    sys.exit(app.exec_())