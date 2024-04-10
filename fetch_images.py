import requests
import random


def get_url_image(random_num):
    url = "https://xkcd.com/{num}/info.0.json"
    response = requests.get(url.format(num=random_num))
    response.raise_for_status()
    comics = response.json()
    link = comics['img']
    title = comics['title']
    download_image(link, title)


def download_image(link, title):

    response = requests.get(link)
    response.raise_for_status()

    with open (f'images/{title}.png', "wb") as file:
        file.write(response.content)


def main():
    url = "https://xkcd.com/info.0.json"
    response = requests.get(url)
    response.raise_for_status()
    comics = response.json()
    comics_number = comics["num"]
    random_num = random.randint(1, comics_number)
    get_url_image(random_num)


if __name__ == "__main__":
    main()