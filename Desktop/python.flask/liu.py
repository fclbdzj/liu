import pymysql


## 数据库连接
db = pymysql.connect(host='127.0.0.1',
                     port= 3306,
                     user='root',
                     password='mysql',
                     database='liu',
                     charset='utf8')
# 使用 cursor() 方法创建一个游标对象 cursor

print ("数据库连接成功！")

cursor = db.cursor()





## 创建表 （如何自增插入数据？）
sql="""CREATE TABLE 小明身高体重变化 (记录地点id int primary key auto_increment ,
                                    年份 CHAR(20) NOT NULL,
                                    记录月份 CHAR(20),
                                    年龄 INT,
                                    身高 FLOAT,
                                    体重 FLOAT)"""
                                    #constraint 记录地点id_key foreign key (记录地点id) references 记录地点(id))"""(这一句好像有点问题？)
# #数据库操作之前，ping 一下，防止数据库关闭
# db.ping(reconnect=True)
# 运行sql语句
cursor.execute(sql)



##数据库插入操作（如何自增插入数据？）

sql = """insert into 小明身高体重变化(记录地点id,年份,记录月份,年龄,身高,体重) values 
             (32,'2004','4','0','80','15'),
             (null,'2005','4','1','85','20'),
             (null,'2006','4','2','95','35')"""


    # 运行sql语句
cursor.execute(sql)
    # 修改
db.commit()
print("成功插入数据!")



# # ## 查询语句
# # try:
# cursor = db.cursor()
# sql = "select * from 小明身高体重变化"

# cursor.execute(sql)
# result = cursor.fetchall()
# for data in result:
#     print(data)

# print(result)#不一样的效果
# # except Exception:
# #     print("查询失败")
# # # 关闭数据库连接
# # db.close()
# # cursor.close()


# # SQL 删除语句
# sql = "DELETE FROM 小明身高体重变化 where 小明身高体重变化.身高=80"

# cursor.execute(sql)
#    # 向数据库提交
# db.commit()

# # 成功提示
# print("成功删除!")


# ##一对多关系实现
# sql_1="create table 记录地点(id int auto_increment primary key,name char(50) not null)"
# sql_2="INSERT INTO 记录地点 (id, name) VALUES (1, '家里'),(2, '学校'),(3, '游乐场')"
# sql_3="""CREATE TABLE 炫曦身高体重变化(年份 CHAR(20) NOT NULL,
#                                     记录月份 CHAR(20),
#                                     年龄 INT,
#                                     身高 FLOAT,
#                                     体重 FLOAT,
#                                     记录地点id int,
#                                     constraint 记录地点id_key foreign key (记录地点id) references 记录地点(id))"""
# sql_4="""insert into 炫曦身高体重变化(年份,记录月份,年龄,身高,体重,记录地点id) values 
#              ('2004','4','0','80','15','1'),
#              ('2005','4','1','85','20','2'),
#              ('2006','4','2','95','35','3')"""

# cursor = db.cursor()
# cursor.execute(sql_1)
# cursor.execute(sql_2)
# cursor.execute(sql_3)
# cursor.execute(sql_4)
# db.commit()




# ##一对一关系实现
# sql_1="""
# create table tb_user(id int auto_increment primary key,
#                      name   varchar(10),
#                      age    int,
#                      gender char(1),
#                      phone  char(11))"""
# sql_2="""create table tb_user_edu(id int auto_increment primary key,
#                                   degree varchar(20),
#                                   major varchar(50),
#                                   primaryschool varchar(50),
#                                   middleschool varchar(50),
#                                   university varchar(50),
#                                   userid int unique,
#                                   constraint fk_userid foreign key (userid) references tb_user(id))"""
# sql_3="""insert into tb_user(id, name, age, gender, phone) values 
#        (null, '黄渤', 45, '1', '18800001111'),
#        (null, '冰冰', 35, '2', '18800002222'),
#        (null, '码云', 55, '1', '18800008888'),
#        (null, '李彦宏', 50, '1', '18800009999')"""
# sql_4="""insert into tb_user_edu(id, degree, major, primaryschool, middleschool, university, userid) values
#        (null, '本科', '舞蹈', '静安区第一小学', '静安区第一中学', '北京舞蹈学院', 1),
#        (null, '硕士', '表演', '朝阳区第一小学', '朝阳区第一中学', '北京电影学院', 2),
#        (null, '本科', '英语', '杭州市第一小学', '杭州市第一中学', '杭州师范大学', 3),
#        (null, '本科', '应用数学', '阳泉第一小学', '阳泉区第一中学', '清华大学', 4);"""
# cursor=db.cursor()
# cursor.execute(sql_1)
# cursor.execute(sql_2)
# cursor.execute(sql_3)
# cursor.execute(sql_4)
# db.commit()
