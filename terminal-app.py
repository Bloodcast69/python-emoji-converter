from emoji import Emoji
from utils import Utils

utils = Utils()
emoji = Emoji(utils.get_api_key())

message = ''

print('Emoji converter terminal test app')
print("Press 'q' or 'Q' to quit")

while message.lower() != 'q':
    message = input('> ')
    if message.lower() != 'q':
        print(emoji.get_emoji(message))
