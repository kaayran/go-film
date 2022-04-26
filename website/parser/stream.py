import os

import requests
import json
import re

from ..models import Film

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

    kinopoisk_id = data_json['kinopoiskId']
    name_rus = data_json['nameRu']
    name_original = data_json['nameOriginal']
    film_url = data_json['webUrl']
    rating_kinopoisk = data_json['ratingKinopoisk']
    rating_imdb = data_json['ratingImdb']
    votes_kinopoisk = data_json['ratingKinopoiskVoteCount']
    votes_imdb = data_json['ratingImdbVoteCount']

    image_url = data_json['posterUrlPreview']

    new_film = Film(kinopoisk_id=kinopoisk_id,
                    name_rus=name_rus,
                    name_original=name_original,
                    url=film_url,
                    image=image_url,
                    rating_kinopoisk=rating_kinopoisk,
                    rating_imdb=rating_imdb,
                    votes_kinopoisk=votes_kinopoisk,
                    votes_imdb=votes_imdb)

    return new_film
