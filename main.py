from dotenv import load_dotenv
import requests
import os
from urllib.parse import urlparse
import argparse


def is_shorten_link(user_link):   
    return urlparse(user_link).netloc == "vk.cc"


def get_short_url(vk_token, user_link, v=5.199):
    url = "https://api.vk.ru/method/"
    method = "utils.getShortLink"
    payload = {"access_token": vk_token,
               "v": v,
               "url": user_link}
    response = requests.get(f"{url}{method}", params=payload)
    response.raise_for_status()
    return response.json()["response"]["short_url"]


def count_click(vk_token, user_link, v=5.199):
    url = "https://api.vk.ru/method/"
    method = "utils.getLinkStats"
    payload = {"access_token": vk_token,
               "v": v,
               "key": urlparse(user_link).path.strip("/"),
               "interval": "forever"}
    response = requests.get(f"{url}{method}", params=payload)
    response.raise_for_status()
    return response.json()["response"]["stats"][0]["views"]


if __name__ == '__main__':
    load_dotenv()
    vk_token = os.environ['VK_TOKEN']
    parser = argparse.ArgumentParser()
    parser.add_argument("link", help="Выдает кароткую ссылку, если ввести полную и количество переходов по ссылке, если ввести короткую", type=str)
    args = parser.parse_args()
    user_link = args.link
    try:
        if is_shorten_link(user_link):
            print(count_click(vk_token, user_link, v=5.236))
        else:
            print(get_short_url(vk_token, user_link, v=5.199))
    except requests.exceptions.HTTPError:
        print("Произошла ошибка при попытке обработать запрос к серверу")
        
        

    
            



