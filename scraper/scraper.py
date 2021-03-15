import selenium
from selenium import webdriver
import time
import datetime
import json

def multiply(number):
    mult = number[-1]
    value = float(number[:-1])
    mults = {'t': 10**12, 'b': 10**9, 'm': 10**6, 'k': 10**3}
    return int(value * mults[mult])

class Scraper:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--headless")
        self.options.add_argument("--no-sandbox")
        self.options.add_argument("--disable-dev-shm-usage")

        self.browser = webdriver.Chrome(options=self.options)
        self.browser.get('https://coincap.io/')

    def search(self):
        stocks = {}
        for i in range(1, 21):
            name = self.browser.find_element_by_xpath(f'/html/body/div[2]/main/div[4]/div/table/tbody/tr[{i}]/td[2]/div/a').text.split('\n')
            price = float(self.browser.find_element_by_xpath(f'/html/body/div[2]/main/div[4]/div/table/tbody/tr[{i}]/td[3]/span').text.replace('$', '').replace(',', ''))
            cap = self.browser.find_element_by_xpath(f'/html/body/div[2]/main/div[4]/div/table/tbody/tr[{i}]/td[4]/span').text.replace('$', '')
            volume = self.browser.find_element_by_xpath(f'/html/body/div[2]/main/div[4]/div/table/tbody/tr[{i}]/td[7]/span').text.replace('$', '')
            stocks[name[1]] = {'name': name[0], 'price': price, 'cap': multiply(cap), 'volume': multiply(volume)}
        self.data = {'time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 'data': stocks}
        print(self.data)
    
    def save_json(self):
        with open(f'data/{datetime.datetime.now().timestamp()}.json', 'w') as fp:
            json.dump(self.data, fp, indent=4)


scraper = Scraper()

while True:
    scraper.search()
    scraper.save_json()
    time.sleep(10)