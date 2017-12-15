# coding=utf-8
def create_table():
    #建立连接
    db = pymysql.connect(host='localhost',user='root',password='root',db='MYDB')
    #创建表
    sql = '''
            create table if no exit student (
            id int not null AUTO_INCREMENT,
            name text,
            job text,
            age int,
            PRIMARY KEY('id')
            )
    '''
    #使用cursor()方法创建一个游标对象
    cursoe = db.cursor()
    try:
        cursor.excute(sql)
        db.commit()
        print('建表成功')
    except BaseException as e:
        db.rollback()
        print(2)
    finally:
        #关闭游标连接
        cursor.close()
        db.close()

        create_table()
print('数据库连接')
