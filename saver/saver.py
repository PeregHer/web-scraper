import os
import psycopg2
import json
import time

class Saver():
    @classmethod
    def open_connexion(cls):
        cls.client = psycopg2.connect(host='postgres', user='admin', password='admin', port='5432', database='coincap')
        cls.client.autocommit = True
        cls.cursor = cls.client.cursor()
        return cls.cursor

    @classmethod
    def close_connexion(cls):
        cls.client.close()
        cls.cursor.close()

    @classmethod
    def find_files(cls):
        for root, dirs, files in os.walk("data", topdown=True):
            return files

    @classmethod
    def load_json(cls, path):
        with open('data/' + path) as j:
            return json.load(j)

    @classmethod
    def insert(cls, data):
        cls.open_connexion()
        SQL = "INSERT into data (currency, name, time, price, cap, volume) VALUES (%s, %s, %s, %s, %s, %s)"
        time = data['time']
        for currency in data['data']:
            name = data['data'][currency]['name']
            price = data['data'][currency]['price']
            cap = data['data'][currency]['cap']
            volume = data['data'][currency]['volume']
            cls.cursor.execute(SQL, (currency, name, time, price, cap, volume))
        cls.close_connexion()

    @classmethod
    def insert_json(cls):
        files = cls.find_files()
        for file in files:
            data = cls.load_json(file)
            cls.insert(data)
            os.remove('data/' + file)
            print(file, 'Inséré')

while True:
    time.sleep(30)
    Saver.insert_json()