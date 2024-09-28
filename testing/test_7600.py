import serial
import time
import sys

PORT= '/dev/ttyUSB0'

baud = 115200

ser = serial.Serial(PORT,baud,timeout = 1)





ser.write(str.encode('AT+CPTONE=4\r\n'))
time.sleep(0.6)
inp = ser.read(ser.in_waiting)
print(inp)

ser.write(str.encode('AT+CRXVOL=0xffff\r\n'))
time.sleep(0.6)
inp = ser.read(ser.in_waiting)
print(inp)

ser.write(str.encode('AT+CPTONE=4\r\n'))
time.sleep(0.6)
inp = ser.read(ser.in_waiting)
print(inp)

ser.write(str.encode('AT+CRXVOL=0x0004\r\n'))
time.sleep(0.6)
inp = ser.read(ser.in_waiting)
print(inp)

ser.close()
