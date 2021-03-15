import random
import time

class Scraper:
    def __init__(self):
        self.AA = ['AAAA', 'AABA', 'ADSA', 'SAAAA']

    def search(self):
        self.AA = self.AA.remove('AAAA')



while True:
    scraper = Scraper()
    print('Created')
    while True:
        try:
            scraper.search()
            print('Searched')
            time.sleep(4)
        except:
            break