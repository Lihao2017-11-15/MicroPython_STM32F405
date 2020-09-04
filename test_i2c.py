from pyb import I2C
import time

i2c = I2C(1)                         # create on bus 1
i2c.init(I2C.SLAVE, addr=0x42)       # init as a slave with given address

while True:
    try:
        data = i2c.recv(3)
        if data:
            print(time.localtime(), data)
            i2c.send('ok')
    except Exception as err:
        pass
