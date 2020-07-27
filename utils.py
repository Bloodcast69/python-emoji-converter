API_KEY = ''


class Utils:
    def get_api_key(self):
        file = open('emoji-api-key.txt', 'r')

        if file.mode == 'r':
            self.API_KEY = file.read()
        file.close()
        return self.API_KEY
