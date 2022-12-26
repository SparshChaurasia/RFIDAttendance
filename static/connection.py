import serial
import requests

PORT = "com6"
BAUDRATE = 9600

conn = serial.Serial(PORT, BAUDRATE)
while True:
    data = conn.read(12)
    uid = data.decode("utf-8").strip()
    print("UID:", uid)

    body = {"uid": uid}
    res = requests.post("http://127.0.0.1:8000/api/new", data=body)
    print("Response:", res.text)
    print("---------------------")
conn.close()
