import os

API_CONF = {
    'HOST' : os.getenv('HOST','0.0.0.0'),
    'PORT' : os.getenv('PORT','8080'),
    'THREADED' : os.getenv('THREADED',True)
}