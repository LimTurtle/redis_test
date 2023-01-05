import pymysql
import pandas as pd

mysql_db = pymysql.connect(
    user="root",
    password="Z797944z!",
    host="127.0.0.1",
    port=3306,
    db="sakila",
)

cursor = mysql_db.cursor()
sql = "select * from actor;"
cursor.execute(sql)
result = cursor.fetchall()
result = pd.DataFrame(result)
print(result)