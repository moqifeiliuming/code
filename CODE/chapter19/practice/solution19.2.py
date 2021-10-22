import sys
import Login
from PyQt5.QtWidgets import QApplication, QMainWindow,QMessageBox
from PyQt5.QtCore import QCoreApplication
if __name__ == '__main__':
    def usr_login():
        usr_name = ui.lineEditUserName.text()
        usr_pwd = ui.lineEditPassword.text()
        if usr_name == 'geekori' and usr_pwd == '1234':
            QMessageBox.information(MainWindow, '消息',
            "登录成功")

        else:
            QMessageBox.warning(MainWindow, '消息',
            "用户名或密码错误")      
        print()
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Login.Ui_MainWindow()
    # 调用setupUi方法动态创建控件
    ui.setupUi(MainWindow)
    ui.pushButtonOK.clicked[bool].connect(usr_login)
    ui.pushButtonCancel.clicked.connect(QCoreApplication.instance().quit)
    # 显示窗口
    MainWindow.show()
   
    # 当窗口关闭后会退出程序
    sys.exit(app.exec_())
    