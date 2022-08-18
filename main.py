from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import kivy
from kivy.app import App

from kivy.uix.widget import Widget
import os

# https://4everfreebrony.bandcamp.com/
class Interface(Widget):
    def __init__(self, **kwargs):
        super(Interface, self).__init__(**kwargs)
        self.remaining = None
        self.iterlinks = None
        self.URL = 'https://4everfreebrony.bandcamp.com/'  # SETUP URL var

    def getURL(self):
        self.URL = self.ids['Input'].text  # fetch user input
        links = self.getLinks()
        self.iterlinks = iter(links)  # setup iterator
        self.remaining = len(links)
        print('test')

    def next(self):
        selected = self.iterlinks.__next__()
        # print(self.ids)
        print(selected)

        # do it!!!
        print(os.system('echo hello'))
        os.system(f'bandcamp-dl https://4everfreebrony.bandcamp.com{selected} --base-dir C:\\Users\Porter\Music\\ ')
        print(f'bandcamp-dl -d https://4everfreebrony.bandcamp.com{selected} --base-dir Music')

        self.remaining -= 1
        self.ids['infoPony'].text = f'Current: {selected} || Remaining: {self.remaining}'

    def getLinks(self):
        req = Request(self.URL)
        html_page = urlopen(req)
        soup = BeautifulSoup(html_page, "lxml")

        links = []
        for link in soup.findAll('a'):
            lin = link.get('href')
            if lin is None:
                continue
            if ('/track------' in lin) or ('/album/' in lin):
                links.append(lin)
            else:
                pass

        return links


class BandCampApp(App):

    def build(self):
        # Clock.schedule_interval()
        return Interface()


if __name__ == '__main__':
    BandCampApp().run()
