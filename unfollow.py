import requests
import threading
import random

from colorama import Fore, init

init(convert=True)

channel_name = input("Enter Channel: ")

def get_username():

    json = {"operationName": "ChannelShell",
            "variables": {
                "login": channel_name
            },
            "extensions": {
                "persistedQuery": {
                    "version": 1,
                    "sha256Hash": "580ab410bcd0c1ad194224957ae2241e5d252b2c5173d8e0cce9d32d5bb14efe"
                }
            }
        }

    headers = {
        'Client-ID': 'kimne78kx3ncx6brgo4mv6wki5h1ko'
    }
    r = requests.post('https://gql.twitch.tv/gql', json=json, headers=headers)
    return r.json()['data']['userOrError']['id']

channel_ID = get_username()

def unfollow():

    tokensf = open("tokens.txt")
    tokens = random.choice(tokensf.read().splitlines())
    tokensf.close()

    headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-GB',
    'Authorization': f'OAuth {tokens}',
    'Client-Id': 'kimne78kx3ncx6brgo4mv6wki5h1ko',
    'Client-Session-Id': 'aba52d30ca5f58e2',
    'Client-Version': '355d123b-5b7b-4e60-b5b3-e998df86e7c1',
    'Connection': 'keep-alive',
    'Content-Type': 'text/plain;charset=UTF-8',
    'Origin': 'https://www.twitch.tv',
    'Referer': 'https://www.twitch.tv/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    'X-Device-Id': '9e7GxupzurGeVtrQDDaTEzkOnXjijE7l',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    }

    data = '[{"operationName":"FollowButton_UnfollowUser","variables":{"input":{"targetID":"'+channel_ID+'"}},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"f7dae976ebf41c755ae2d758546bfd176b4eeb856656098bb40e0a672ca0d880"}}}]'
    r = requests.post('https://gql.twitch.tv/gql', headers=headers, data=data)
    print(Fore.GREEN + f"Unfollowed {Fore.RESET}{channel_name}{Fore.RESET}\n")

def start():
    print("Removing followers")
    while True:
        threading.Thread(target=unfollow).start()

start()
