import redis

pool = redis.ConnectionPool(host='127.0.0.1', port=6301)

redis1 = redis.Redis(connection_pool=pool)
redis1.set('bonaparte', '3')
print(redis1['bonaparte'])