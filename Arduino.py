import serial

ser = serial.Serial("/dev/ttyACM0",9600)

while 1:
	val = input( "Numero: " ).encode()
	print(val)
	ser.write(val)