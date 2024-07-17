import requests
import json
import time

user_address = input("Enter adress: ")
user_choice = input("Enter name of worker: (case sensitive, press enter for general address info)")

if  user_choice == "": 
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

    get_request(url)
    time.sleep(10)
else:
    wurl = f"https://luckpool.net/verus/worker/{user_address}.{user_choice}"

def get_request(wurl):
    response_wurl = requests.get(wurl)
    wurldata = response_wurl.json()
    display_custom_format(wurldata)

def display_custom_format(wurldata):
    avg_hashrate = wurldata.get("hashrateString", "N/A")
    shares = wurldata.get("shares", "N/A")
    est_luck = wurldata.get("estimatedLuck", "N/A")
    
    print(f"|AvgHashrate: {avg_hashrate}/s\n|Shares: {shares}\n|EstLuck: {est_luck}\n")
if 1+1==2:
    get_request(wurl)
    time.sleep(10)