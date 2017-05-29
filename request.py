import http.client
import time


conn = http.client.HTTPSConnection("api.um.warszawa.pl")
headers = {'cache-control': "no-cache"}
while True:
    print("start")
    conn.request("GET", "/api/action/wsstore_get?id=c7238cfe-8b1f-4c38-bb4a-de386db7e776&apikey=25cbeeea-13ae-4e8d-9b32-a506db94284c", headers=headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))
    time.sleep(180)
