# wxPython：是Python语言的一条优秀的GUI图形库，运行程序员很方便地创建完整的、功能健全的GUI用户界面
# PyQt：PyQt 是Qt库的Python版本，支持跨平台

# import wx
# class App(wx.App):
#     def OnInit(self):
#         frame = wx.Frame(parent=None,title='Hello wyPython')  # 创建窗口
#         frame.Show()  # 显示窗口
#         return True   # 返回值
#
# if __name__=='__main__':
#     app = App()         # 创建App类的实例
#     app.MainLoop()      # 调用App类的MainLoop()主循环方法

# 上面的代码可以改写成下面的方式，达到相同的效果
# import wx
# app = wx.App()
# frame = wx.Frame(None,title='Hello wyPython')  # 定义了一个顶级窗口
# frame.Show()     # 显示窗口
# app.MainLoop()   # 调用wx.App类的MainLoop()主循环方法

# 在GUI中框架通常也称为窗口，框架是一种容器，用户可以将它在屏幕上任意移动，并可以对它进行缩放，它通常包括标题栏、菜单等。
# 在wxPython中，wx.Frame是所有框架的父类，当创建wx.Frame的子类时，子类应该调用其父类的构造器wx.Frame.__init__()
# 在所有的UI工具中，最基本的任务就是在屏幕上绘制纯文本，在wxPython中，使用wx.StaticText类完成，可改变文本对齐形式、字体和颜色
# wx.TextCtrl类，允许输入单行和多行文本，可以作为密码输入控件，掩饰所按下的按键

import wx
class MyFrame(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,title='创建TextCtrl类',size=(400,300))
        # 创建面板
        panel = wx.Panel(self)
        # 创建文本和输入框
        self.title = wx.StaticText(panel,label="请输入用户名和密码",pos=(140,20))
        self.label_user = wx.StaticText(panel,label="用户名：",pos=(50,50))
        self.text_user = wx.TextCtrl(panel,pos=(100,50),size=(235,25),style=wx.TE_LEFT)
        self.label_pwd = wx.StaticText(panel,pos=(50,90),label="密  码：")
        self.text_password = wx.TextCtrl(panel,pos=(100,90),size=(235,25),style=wx.TE_PASSWORD)
        # 创建 "确定" 和 "取消" 按钮
        self.bt_confirm = wx.Button(panel,label='确定',pos=(105,130))
        self.bt_cancel = wx.Button(panel,label='取消',pos=(195,130))

if __name__=='__main__':
    app = wx.App()
    frame = MyFrame(parent=None,id = -1)
    frame.Show()
    app.MainLoop()

# BoxSizer：在一条水平或者垂直线上的窗口部件的布局，当尺寸改变时，控制窗口部件的行为上很灵活。通常用于嵌套的样式，可用于几乎任何类型的布局
# GridSizer：一个十分基础的网格布局，当你要放置的窗口部件都是同样的尺寸且整齐地放入一个规则的网格中可以使用它
# FlexGridSizer：对GridSizer稍微做了些改变，当窗口部件有不同的尺寸时，可以有更好的结果
# GridBagSizer：GridSizer系列中最灵活的成员，使得网格中的窗口部件可以随意放置
# StaticBoxSizer：一个标准的Box Sizer，带有标题和环线

import wx
class MyFrame(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,title='创建TextCtrl类',size=(400,300))
        # 创建面板
        panel = wx.Panel(self)
        self.title = wx.StaticText(panel,label="请输入用户名和密码")
        # 添加容器，容器中控件按纵向排列
        vsizer = wx.BoxSizer(wx.VERTICAL)
        vsizer.Add(self.title,proportion=0,flag=wx.BOTTOM|wx.TOP|wx.ALIGN_CENTER,border=15)
        panel.SetSizer(vsizer)

if __name__=='__main__':
    app = wx.App()
    frame = MyFrame(parent=None,id = -1)
    frame.Show()
    app.MainLoop()

# 事件
# 当发生一个事件时，需要让程序注意这些事件并且做出反应。可以将函数绑定到所涉及事件可能发生的控件上。
# 当事件发生时，函数会被调用。利用控件的Bind()方法可以将事件处理函数绑定到给定的事件上。如：为“确定”按钮添加一个单击事件
# bt_confirm.Bind(wx.EVT_BUTTON,OnclickSumbit)
import wx
class MyFrame(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,title='创建TextCtrl类',size=(400,300))
        # 创建面板
        panel = wx.Panel(self)
        # 创建“确定”和“取消”按钮，并绑定事件
        self.bt_confirm = wx.Bottom(panel,label="确定")
        self.bt_confirm.Bind(wx.EVT_BUTTON,self.OnclickSubmit)
        self.bt_cancel = wx.Button(panel,label="取消")
        self.bt_confirm.Bind(wx.EVT_BUTTON, self.OnclickCancel)

    def OnclickSubmit(self,event):
        "单击确定按钮，执行方法"
        message = ""
        username = self.text_user.GetValue()      #获取输入的用户名
        password = self.text_password.GetValue()  #获取输入的密码
        if username == "" or password == "":      #判断用户名或者密码是否为空
            message = '用户名或者密码不为空'
        elif username == 'mr' and password == 'mrsoft':  # 用户名或密码错误
            message = '登录成功'                          # 弹出提示框
        else:
            message = '用户名和密码不匹配'
        wx.MessageBox(message)

    def OnclickCanel(self,event):
        "单击取消按钮，执行放"
        self.text_user.SetValue()                  # 清空输入的用户名
        self.text_password.SetValue()              # 清空输入的密码

if __name__=='__main__':
    app = wx.App()                                 # 初始化应用
    frame = MyFrame(parent=None,id = -1)           # 实例MyFrame类，并传递参数
    frame.Show()                                   # 显示窗口
    app.MainLoop()                                 # 调用主循环方法