import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QMenu, QApplication

class Menu(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
    def initUI(self):                 
        menubar = self.menuBar()
        print(menubar)
        fileMenu = menubar.addMenu('文件')
        newAct = QAction('新建', self)   
        impMenu = QMenu('导入', self)
        impAct1 = QAction('从PDF导入', self) 
        impAct2= QAction('从Word导入', self) 
        impAct1.triggered.connect(self.actionHandler1)
        impAct2.triggered.connect(self.actionHandler2)
        impMenu.addAction(impAct1)
        impMenu.addAction(impAct2)
        
        fileMenu.addAction(newAct)
        fileMenu.addMenu(impMenu)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('菜单')    
        self.show()
    def actionHandler1(self):          
        print('从PDF导入')    
    def actionHandler2(self):          
        print('从Word导入')       
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Menu()
    sys.exit(app.exec_())