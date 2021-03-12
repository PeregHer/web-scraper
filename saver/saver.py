import os
import pymongo
import json
import time


class Saver:
    @classmethod
    def find_files(cls):
        for root, dirs, files in os.walk("data", topdown=True):
            return files

    @classmethod
    def load_json(cls, path):
        with open('data/' + path) as json_file:
            return json.load(json_file)

    @classmethod
    def open_connexion(cls):
        cls.client = pymongo.MongoClient("mongodb+srv://Stephane:isen-brest@bel-cluster.1cbyc.mongodb.net/coincap?retryWrites=true&w=majority")
        cls.db = cls.client['coincap']
        cls.collection = cls.db['data']
    
    @classmethod
    def close_connexion(cls):
        cls.client.close()

    @classmethod
    def insert(cls, data):
        cls.open_connexion()
        cls.collection.insert_one(data)
        cls.close_connexion()

    @classmethod
    def insert_files(cls):
        files = cls.find_files()
        for file in files:
            data = cls.load_json(file)
            cls.insert(data)
            os.remove('data/' + file)


while True:
    time.sleep(600)
    Saver.insert_files()
