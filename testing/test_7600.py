import serial
import time
import sys
# ~ import hashlib

PORT= '/dev/ttyUSB0'

baud = 300 # 115200

ser = serial.Serial(PORT,baud,timeout = 5)



ser.write(str.encode('AT+\r\n'))
time.sleep(5)
inp = ser.read(ser.in_waiting)
# ~ print(inp)

time.sleep(5)
inp = ser.read(ser.in_waiting)
print(inp)

# ~ ser.write(str.encode('AT+CPTONE=4\r\n'))
# ~ time.sleep(0.6)
# ~ inp = ser.read(ser.in_waiting)
# ~ print(inp)

# ser.write(str.encode('AT+CRXVOL=0xffff\r\n'))
# time.sleep(0.6)
# inp = ser.read(ser.in_waiting)
# print(inp)

# ser.write(str.encode('AT+CPTONE=4\r\n'))
# time.sleep(0.6)
# inp = ser.read(ser.in_waiting)
# print(inp)

# ser.write(str.encode('AT+CRXVOL=0x0004\r\n'))
# time.sleep(0.6)
# inp = ser.read(ser.in_waiting)
# print(inp)

ser.close()
