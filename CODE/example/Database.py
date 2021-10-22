import pymysql

# conn = pymysql.Connect(
#     host='localhost',
#     user='user',
#     password='password',
#     db='test',
#     charset='utf8',
#     cursorclass=pymysql.cursors.DictCursor
# )

# # 操作sqlite3的步骤
# # 导入模块
# import sqlite3
# # 创建连接对象
# conn = sqlite3.connect('mrsoft.db')
# # 创建游标对象
# cursor = conn.cursor()
# # 执行SQL语句
# cursor.execute('create table user(id int(10) primary key,name varchar(20))')  # primary key 表示主键
# # 关闭游标
# cursor.close()
# # 关闭连接
# conn.close()

# 操作sqlite3的步骤
# 导入模块
# import sqlite3
# # 创建连接对象
# conn = sqlite3.connect('mrsoft.db')
# # 创建游标对象
# cursor = conn.cursor()
# # 执行SQL语句
# # cursor.execute('create table user(id int(10) primary key,name varchar(20))')
# sql = 'insert into user(id,name) values(1,"mrsoft")'
# cursor.execute(sql)
# # sql = 'insert into user(id,name) values(?,?)'  # 避免SQL注入问题，如"andy 'or 1=1 or'"
# # cursor.execute(sql,(2,'xiaoming'))
# data = [(3,'andy'),(4,'kobe'),(5,'Jame')]
# cursor.executemany(sql,data)
# # 关闭游标
# cursor.close()
# # 提交事务
# conn.commit()
# # 关闭连接
# conn.close()

# 查询数据的3种方式
# 导入模块
# import sqlite3
# # 创建连接对象
# conn = sqlite3.connect('mrsoft.db')
# # 创建游标对象
# cursor = conn.cursor()
# # 执行SQL语句
# sql = 'select * from user'
# cursor.execute(sql)
# result = cursor.fetchone()
# print(result)
# cursor.execute('select * from user where id > ?',(0,)) # 查询所有的记录
# result1 = cursor.fetchall()
# print(result1)
# # 关闭游标
# cursor.close()
# # 关闭连接
# conn.close()

# 修改用户数据信息
# 导入模块
import sqlite3
# 创建连接对象
conn = sqlite3.connect('mrsoft.db')
# 创建游标对象
cursor = conn.cursor()
# 执行SQL语句
sql = 'update user set name = ? where id = ?'
cursor.execute(sql,('MR',1))
# 提交事务
conn.commit()
# 关闭游标
cursor.close()
# 关闭连接
conn.close()

# 删除用户数据信息
# 导入模块
import sqlite3
# 创建连接对象
conn = sqlite3.connect('mrsoft.db')
# 创建游标对象
cursor = conn.cursor()
# 执行SQL语句
sql = 'delete from user where id = ?'
cursor.execute(sql,(1,))
cursor.execute('select * from user')
result = cursor.fetchall()
print(result)
# 关闭游标
cursor.close()
# 提交事务
conn.commit()
# 关闭连接
conn.close()