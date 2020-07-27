from fastapi import FastAPI
from utils import Utils
import requests

app = FastAPI()
utils = Utils()
API_KEY = utils.get_api_key()
BASE_URL = 'https://emoji-api.com'


@app.get('/emojis/')
async def get_emojis():
    response = requests.get(f'{BASE_URL}/emojis?access_key={API_KEY}')
    return response.json()


@app.get('/emojis/{emoji_name}')
async def get_emoji(emoji_name: str):
    response = requests.get(f'{BASE_URL}/emojis/{emoji_name}?access_key={API_KEY}')

    if response.json():
        return response.json()
    else:
        return {'message': f'No emoji found: {emoji_name}'}


@app.get('/search-emoji/')
async def search_emoji(search: str):
    response = requests.get(f'{BASE_URL}/emojis?search={search}&access_key={API_KEY}')

    if response and response.json():
        return response.json()
    else:
        return {'message': f'No emoji found for query: {search}'}


@app.get('/categories/')
async def get_categories():
    response = requests.get(f'{BASE_URL}/categories?access_key={API_KEY}')
    return response.json()


@app.get('/categories/{category_name}')
async def get_emojis_in_category(category_name: str):
    response = requests.get(f'{BASE_URL}/categories/{category_name}?access_key={API_KEY}')

    if response.json():
        return response.json()
    else:
        return {'message': f'No emoji found in category: {category_name}'}
