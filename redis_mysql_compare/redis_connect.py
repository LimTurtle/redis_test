import redis
r = redis.Redis(host="34.84.148.50", port="6379", password="a12b34", charset="utf-8", decode_responses=True)

print(r.ping())
print(r.set(name="name", value="Lim"))
print(r.get(name="name"))