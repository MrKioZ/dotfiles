from urllib.request import urlopen, Request
import json

def get(url="https://jsonplaceholder.typicode.com/posts/1"):

    if not url.startswith("http"):
        raise RuntimeError("Incorrect and possibly insecure protocol in url")

    httprequest = Request(url, headers={"Accept": "application/json"})

    with urlopen(httprequest) as response:
        # print(response.status)
        # print(response.read().decode())
        if response.status == 200:
            return json.loads(response.read().decode())
        else:
            return {"error":response.status}
