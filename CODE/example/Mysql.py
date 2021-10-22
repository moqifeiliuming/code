# 导入PyMysql模块
import pymysql
# 调用connect()函数生产connection连接对象
db = pymysql.connect(host = 'localhost',user = 'root',password = 'root',database = 'mrsoft')  # 顺序不能乱
# 调用cursor()方法，创建Cursor对象
cursor = db.cursor()
# 执行SQL语句
cursor.execute('select version()')
data = cursor.fetchone()
print(data)
# 关闭连接
cursor.close()
db.close()