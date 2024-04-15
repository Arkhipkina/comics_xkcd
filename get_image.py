import requests

def get_url_image(random_num):
    url = "https://xkcd.com/{num}/info.0.json"
    response = requests.get(url.format(num=random_num))
    response.raise_for_status()
    comics = response.json()
    link = comics['img']
    alt = comics['alt']
    return link, alt
