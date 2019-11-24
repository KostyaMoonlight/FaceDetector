from pymongo import MongoClient
from bson import ObjectId
import os


class DBManager():
    def __init__(self, collection='students'):
        super(DBManager, self).__init__()
        self.client = MongoClient('localhost', 27017)
        self.db = self.client["face_detector"]
        self.collection=collection
        self.students = self.db[self.collection]


    def get_all_students(self):
        return self.students.find({})

    def get_student(self, _id):
        return self.students.find_one({'_id':ObjectId(_id)})

    def get_ids(self):
        return self.students.find({}, { '_id':1})

    def get_encodings(self):
        return self.students.find({}, { 'encoding':1, '_id':0})

    def get_students(self, ids):
        return self.students.find({ "_id": { "$in": ids }})

    
    def add_student(self, student):
        try:        
            student = self.students.insert_one(student)
            return "Ok"
        except:
            raise Exception('Could not add to database')
