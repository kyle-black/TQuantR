import redis





username = 'default'
password = 'AVNS_fEkTeQktbzivO38lxoz'
host = 'tensorquant-prediction-1-do-user-13042543-0.c.db.ondigitalocean.com'
port = '25061'
db=0





# Connect to the Redis server
#redis_connection = redis.Redis(host=host, port=port, db=db)


redis_connection = redis.Redis(host=host, port=port, db=db, username=username, password=password)



try:
    response = redis_connection.ping()
    if response:
        print("Successfully connected to Redis")
except redis.exceptions.ConnectionError as e:
    print(f"Connection failed: {e}")