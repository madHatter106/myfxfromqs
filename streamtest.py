import requests
import json
import settings

domain = settings.STREAM_DOMAIN
access_token = settings.ACCESS_TOKEN
account_id = settings.ACCOUNT_ID
endpoint = 'v1/prices'
url = 'https://%s/%s' % (domain, endpoint)
instruments = "EUR_USD"
headers = {'Authorization': 'Bearer ' + access_token}
params = {'accountId': account_id, 'instruments': instruments}
req = requests.Request('GET', url, headers=headers, params=params)
pre = req.prepare()
client = requests.Session()
print('connecting to %s' % url)
resp = client.send(pre, stream=True, verify=False)
for line in resp.iter_lines(1):
    if line:
        msg = json.loads(line.decode())
        if "instrument" in msg:
            print
