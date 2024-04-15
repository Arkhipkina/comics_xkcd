import requests

# from download_image import download_image

def get_url_image(random_num):
    url = "https://xkcd.com/{num}/info.0.json"
    response = requests.get(url.format(num=random_num))
    response.raise_for_status()
    comics = response.json()
    link = comics['img']
    return link
    # title = comics["title"]
    # download_image(link, title)
