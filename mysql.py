import pymysql
db = pymysql.connect("localhost", "root", "", "DBName")
cursor = db.cursor()
sql = """CREATE TABLE TableName(
    Name varchar(255),
    Age int
);"""
cursor.execute(sql)
db.close()
