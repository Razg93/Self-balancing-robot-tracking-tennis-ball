import serial
ser = serial.Serial('/dev/rfcomm3',baudrate=115200)  # open serial port
j=str(5)         # check which port was really used
b = j.encode()     # write a string
ser.write(b)

import serial # Module needed for serial communication
import time # Module needed to add delays in the code
 
# Set the port name and the baud rate. This baud rate should match the
# baud rate set on the Arduino.
# Timeout parameter makes sure that program doesn't get stuck if data isn't
# being received. After 1 second, the function will return with whatever data
# it has. The readline() function will only wait 1 second for a complete line 
# of input.
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
 
# Get rid of garbage/incomplete data
ser.flush()
 
# Infinite loop
while (1):
 
  send_string = ("My name is Raspberry Pi\n")
   
  # Send the string. Make sure you encode it before you send it to the Arduino.
  ser.write(send_string.encode('utf-8'))
   
  # Do nothing for 500 milliseconds (0.5 seconds)
  time.sleep(0.5)
 
  # Receive data from the Arduino
  receive_string = ser.readline().decode('utf-8').rstrip()
 
  # Print the data received from Arduino to the terminal
  print(receive_string)