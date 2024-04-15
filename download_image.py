import requests

def download_image(url_image, title):

    response = requests.get(url_image)
    response.raise_for_status()

    with open (f'image\{title}', "wb") as file:
        file.write(response.content)