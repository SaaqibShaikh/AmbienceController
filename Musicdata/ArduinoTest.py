import serial
import time

ser = serial.Serial('COM3', 9600)  # open serial port
time.sleep(2)                      # wait 2 seconds
ser.write(b'Y')
# LED turns on
print("done")
time.sleep(5)
ser.write(b'W')
# LED turns off
print("done2")
time.sleep(5)

ser.write(b'R')
# LED turns on
print("done#")
time.sleep(5 )

ser.write(b'G')

# LED turns off
print("done$")
time.sleep(2)
ser.write(b'W')
ser.close()
exit()