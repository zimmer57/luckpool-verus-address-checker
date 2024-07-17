import requests
import json
import time

user_address = input("Enter adress: ")
url = f"https://luckpool.net/verus/miner/{user_address}"

def get_request(url):
    response_url = requests.get(url)
    urldata = response_url.json()
    display_custom_format(urldata)

def display_custom_format(urldata):
    address = urldata.get("address", "N/A")
    avg_hashrate = urldata.get("hashrateString", "N/A")
    est_luck = urldata.get("estimatedLuck", "N/A")
    bal = urldata.get("balance", "N/A")
    
    print(f"|Address: {address}\n|Balance: {bal}\n|AvgHashrate: {avg_hashrate}/s\n|EstLuck: {est_luck}\n")

for i in range(9999999999999):
    get_request(url)
    time.sleep(2)