import telegram
import os
import requests
import random

from dotenv import load_dotenv

from get_url_image import get_url_image


def get_random_number():
    url = "https://xkcd.com/info.0.json"
    response = requests.get(url)
    response.raise_for_status()
    comics = response.json()
    comics_number = comics["num"]
    random_num = random.randint(1, comics_number)
    return random_num


def main():
    load_dotenv()
    tg_token = os.environ["TG_TOKEN"]
    tg_chat_id = os.environ["TG_CHAT_ID"]
    
    bot = telegram.Bot(token=tg_token)

    random_num = get_random_number()
    document = get_url_image(random_num)
    bot.send_document(chat_id=tg_chat_id, document=document)

if __name__ == "__main__":
    main()