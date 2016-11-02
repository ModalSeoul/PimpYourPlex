from utils import *

title = args.title
count = args.count
URL = 'http://kissanime.to/Anime/{}'.format(title)


class KissAnime:
    def __init__(self):
        self.req = scraper.get(URL).content
        print(self.req)

ka = KissAnime()
