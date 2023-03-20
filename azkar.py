# Send (printing) zkr every 5 sec 
import requests
import json
from time import sleep

def API():
    res = requests.get('https://ayah.nawafdev.com/api/dekr?types=random')
    response = json.loads(res.text)

    # print(res.json())
    print(response['content'])

while True:
    sleep(5)
    API()
