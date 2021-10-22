import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, 
    QHBoxLayout, QVBoxLayout, QApplication)


class BoxLayout(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        okButton = QPushButton("确定")
        cancelButton = QPushButton("取消")

        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        vbox.addStretch()
        vbox.addLayout(hbox)

        self.setLayout(vbox)    

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('盒布局')    
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = BoxLayout()
    sys.exit(app.exec_())