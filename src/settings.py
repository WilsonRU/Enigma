import json

class Settings(object):

    def __init__(self):
        file = open('settings.json')
        settings = json.loads(file)
        return settings['base']