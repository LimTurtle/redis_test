import redis
import pymysql
import time

r = redis.Redis(host="127.0.0.1", port="6379", charset="utf-8", decode_responses=True)

mysql_db = pymysql.connect(
    user="root",
    password="Z797944z!",
    host="127.0.0.1",
    port=3306,
    db="sakila",
)


res = []
for customer_id in range(1, 500):
    id = int(customer_id)
    first_time = time.time()
    result = r.get(name=id)
    print(id)

    if not result:
        print("no cache")
        cursor = mysql_db.cursor()
        sql = "select customer_id, first_name from customer where customer_id = %s"
        cursor.execute(sql, int(id))
        result = cursor.fetchone()
        r.set(name=result[0], value=result[1])
    else:
        print("cache")

    result = r.get(name=id)
    last_time = time.time()
    total_time = last_time - first_time
    print("{: .17f} Sec".format(total_time))
    print(result)
    res.append(total_time)
    print("Sum of Total Time : {}".format(sum(res)))
    print()