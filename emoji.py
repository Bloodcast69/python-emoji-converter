import requests


class Emoji:
    BASE_URL = 'https://emoji-api.com/'
    API_TOKEN = ''

    def __init__(self, token: str):
        self.API_TOKEN = token

    def get_single_emoji(self, emoji_name: str):
        response = requests.get(f'{self.BASE_URL}/emojis/{emoji_name}?access_key={self.API_TOKEN}')
        if (response.json()):
            return response.json()[0]['character']
        else:
            return None

    def search_emoji(self, emoji_name: str):
        response = requests.get(
            f'{self.BASE_URL}/emojis?search={emoji_name.replace("-", " ")}&access_key={self.API_TOKEN}')
        if (response.json()):
            emojis = []
            for emoji in response.json():
                emojis.append({'icon': emoji['character'], 'slug': emoji['slug']})
            return emojis
        else:
            return None

    def get_emoji(self, emoji_name: str):
        single_emoji = self.get_single_emoji(emoji_name)
        if single_emoji:
            return single_emoji
        else:
            return self.search_emoji(emoji_name)

    def get_emoji_categories(self):
        response = requests.get(f'{self.BASE_URL}/categories?access_key={self.API_TOKEN}')
        return response.json()

    def get_emoji_in_category(self, category_name):
        response = requests.get(f'{self.BASE_URL}/categories/{category_name}?access_key={self.API_TOKEN}')
        if response.json():
            return response.json()
        else:
            return None
