import http.client
from secret import *

conn = http.client.HTTPSConnection("studio.edgeimpulse.com")

payload = "{\"label\":\"idle\",\"lengthMs\":5000,\"category\":\"training\",\"intervalMs\":10,\"sensor\":\"Inertial\"}"

headers = {
    'content-type': "application/json",
    'x-api-key': API_Key
    }

#conn.request("GET", f"/v1/api/{project_ID}/device/{device_ID}", headers=headers)

conn.request("POST", f"/v1/api/{project_ID}/device/{device_ID}/start-sampling", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))