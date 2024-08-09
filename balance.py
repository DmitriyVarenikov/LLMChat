import requests
import json
import time

from conf import APY_KEY

response = requests.get(
    url=f"https://api.vsegpt.ru/v1/balance?timestamp={int(time.time())}",
    headers={
        "Authorization": f"Bearer {APY_KEY}",
        "Content-Type": "application/json",
        "Cache-Control": "no-cache"
    },
)


# print(response.text)
def get_balance():
    if response.status_code == 200:
        response_big = json.loads(response.text)
        if response_big.get("status") == "ok":
            credits = float(response_big.get("data").get("credits"))
            return credits
        else:
            raise response_big.get("reason")  # reason of error
    else:
        raise ValueError(str(response.status_code) + ": " + response.text)


print(get_balance())
