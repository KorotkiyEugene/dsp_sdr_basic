import serial, time

query=":A0?\n"

ser=serial.Serial("/dev/ttyACM1",115200,timeout=1)

time.sleep(1)
# wait for serial to be ready

ser.write(query)

time.sleep(0.1)

reply=ser.readline()

print(reply.strip())

ser.close()
