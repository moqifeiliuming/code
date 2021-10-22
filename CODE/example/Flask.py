from flask import Flask
app = Flask(__name__)

@app.route('/')   # 使用route()装饰器告诉Flask什么样的URL能触发函数
def hello_world():
    return 'Hello World'

if __name__=='__main__':
    app.run(debug=True)

# 两种途径来启用调试模式：
# 一种是是直接应用在对象上设置
app.debug = True
app.run()
# 另一种是作为run()方法的一个参数传入
app.run(debug=True)

# Django项目中共的文件及说明
# manage.py：Django程序执行的入口
# db.sqlite3：SQLite的数据库文件，Django默认使用这种小型数据库存取数据，非必须
# templates：Django生成的HTML模板文件夹，也可以在每个app中共使用模板文件夹
# demo：Django生成的和项目同名的配置文件夹
# settings.py：Django总的配置文件，可以配置APP、数据库、中间件、模板等诸多选项
# urls.py：Django默认的路由配置文件
# wsgi.py：Django实现的WSGI接口的文件，用来处理Web请求

# migrations：执行数据库迁移生成的脚本
# admin.py：配置Django管理后台的文件
# apps.py：单独配置添加的每个App的文件
# models.py：创建数据库数据模型对象的文件
# tests.py：用来编写测试脚本的文件
# views.py：用来编写视图控制器的文件
