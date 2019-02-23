from pymongo import MongoClient


class DBManager:
    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client.sensor_readings
        self.collection = self.db.alldata
    
    def insrt(self, current_reading):
        alldata = self.collection
        alldata.insert_one(current_reading)
        

