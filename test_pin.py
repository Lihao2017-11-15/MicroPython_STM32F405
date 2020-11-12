from pyb import Pin, ExtInt

#callback = lambda e: print("intr")
#ext = ExtInt(Pin('Y1'), ExtInt.IRQ_RISING, Pin.PULL_NONE, callback)

def callback(line):
    print("line =", line)
    
for i in range(1,13):
    ExtInt(Pin('X%d' % i), ExtInt.IRQ_FALLING, Pin.PULL_UP, callback)    