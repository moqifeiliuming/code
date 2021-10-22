import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication

class AbsoluteLayout(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        lbl1 = QLabel('姓名', self)
        lbl1.move(15, 10)

        lbl2 = QLabel('年龄', self)
        lbl2.move(35, 40)

        lbl3 = QLabel('所在城市', self)
        lbl3.move(55, 70)        

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('绝对布局')    
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = AbsoluteLayout()
    sys.exit(app.exec_())