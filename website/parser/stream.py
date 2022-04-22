import os

import requests
import json
import re

headers = {
    'X-API-KEY': os.environ['KINOPOISK_API'],
    'Content-Type': 'application/json',
}


def get_film_id(url):
    match = re.search(r'\d+', url)
    film_id = match.group(0)

    return film_id


def get_film_data(film_id):
    link = f'https://kinopoiskapiunofficial.tech/api/v2.2/films/{film_id}'
    req = requests.get(url=link, headers=headers)
    data = req.text
    data_json = json.loads(data)

    name = data_json['nameRu']
    poster = data_json['posterUrl']

    return name, poster
