import redis
r = redis.Redis(host="127.0.0.1", port="6379", charset="utf-8", decode_responses=True)

print(r.ping())
print(r.set(name="name", value="Lim"))
print(r.get(name="name"))