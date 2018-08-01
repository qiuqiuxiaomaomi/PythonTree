import redis

pool = redis.ConnectionPool(host='**', port=6301)

redis1 = redis.Redis(connection_pool=pool)
redis1.set('bonaparte', '3')
print(redis1['bonaparte'])