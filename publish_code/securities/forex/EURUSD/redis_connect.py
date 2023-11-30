import redis
#from urllib.parse import urlparse  

REDIS_URL= "redis://default:AVNS_L6qlwRsOUSat_3PpWOY@tensorquant-prediction2-do-user-13042543-0.c.db.ondigitalocean.com:25061"

#parsed_url =urlparse(REDIS_URL)


url_connection = redis.from_url(REDIS_URL)
response =url_connection.ping()

print(response)

'''
username = 'default'
password = 'AVNS_fEkTeQktbzivO38lxoz'
host = 'tensorquant-prediction-1-do-user-13042543-0.c.db.ondigitalocean.com'
port = '25061'
db=0
'''




# Connect to the Redis server
#redis_connection = redis.Redis(host=host, port=port, db=db)


#redis_connection = redis.Redis(host=parsed_url.hostname, port=parsed_url.port, password=parsed_url.password, decode_responses=True)

#response = redis_connection.ping()

#if response:
#        print("Successfully connected to Redis")



'''
try:
    response = redis_connection.ping()
    if response:
        print("Successfully connected to Redis")
except redis.exceptions.ConnectionError as e:
    print(f"Connection failed: {e}")
'''


#redis_connection.set('my_key', 'my_value')

# Retrieve the value by key
#value = redis_connection.get('my_key')
#print(value.decode('utf-8'))  # Decode the value from bytes to string
