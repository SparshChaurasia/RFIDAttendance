import serial
import requests

PORT = "com8"
BAUDRATE = 9600

conn = serial.Serial(PORT, BAUDRATE)
while True:
    data = conn.read(12)
    uid = data.decode("utf-8").strip()
    print("UID:", uid)

    body = {"uid": uid}
    res = requests.post("http://127.0.0.1:8000/api/new", data=body)
    print("Response:", res.text)

    # with open("static\error.html", "w") as f:
    #     print(res.text, file=f)

    print("---------------------")
conn.close()
