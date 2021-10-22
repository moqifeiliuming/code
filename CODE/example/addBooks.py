# 导入PyMysql模块
import pymysql
# 调用connect()函数生产connection连接对象
db = pymysql.connect(host = 'localhost',user = 'root',password = 'root',database = 'mrsoft',charset="utf8")  # 顺序不能乱
# 调用cursor()方法，创建Cursor对象
cursor = db.cursor()
# data = ('零基础学Python','python','78.90','2018-11-11')
data = [('零基础学Python','python','78.90','2018-11-11'),
        ('零基础学PHP','PHP','69.90','2012-2-12'),
        ('零基础学java','java','88.80','2020-9-8'),]
# 执行SQL语句
try:
    sql = "insert into books(name,category,price,publish_time) values(%s,%s,%s,%s) " # 在使用insert语句插入数据时，使用%s作为占位符，可以防止SQL注入
    # cursor.execute(sql,data) #此时时插入一条记录
    cursor.executemany(sql,data)
    # 提交数据
    db.commit()
except:
    # 发生错误时回滚
    db.rollback()
# 关闭连接
cursor.close()
db.close()