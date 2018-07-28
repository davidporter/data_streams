from Adafruit_IO import *
from private import aio_key

aio = Client(aio_key)

aio.send('temp', 21)
