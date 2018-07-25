from Adafruit_IO import *
# from private import aio_key

aio_key = "97ab045aa058453b900ba118206a2e31"

aio = Client(aio_key)

aio.send('temp', 20)