import serial
import json
connection = serial.Serial('/dev/ttyACM0', baudrate=9600)
connection.reset_input_buffer()
 
while True:
    data = connection.readline().decode("utf-8")
    # print(data)
    try:
        dict_json = json.loads(data)
        print(dict_json)
    except json.JSONDecodeError as e:
        print("JSON:", e)
