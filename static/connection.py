import serial
import requests

conn = serial.Serial("com6", 9600)
while True:
    data = conn.read(12)
    uid = data.decode("utf-8").strip()
    print(uid)

    body = {"uid": uid}
    res = requests.post("http://127.0.0.1:8000/api/", data=body)
    print(res)
conn.close()
