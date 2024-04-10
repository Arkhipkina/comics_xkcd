import telegram
import os

from dotenv import load_dotenv


def main():
    load_dotenv()
    tg_token = os.environ["TG_TOKEN"]
    tg_chat_id = os.environ["TG_CHAT_ID"]
    bot = telegram.Bot(token=tg_token)
    bot.send_message(chat_id=tg_chat_id, text="Всем привет!")

if __name__ == "__main__":
    main()