import os
from PIL import Image
import face_recognition
from .tools import *
import numpy as np
from .models import Student
import json 
class FaceService:

        
    def get_admin_faces(self):
        return [np.asarray(json.loads(student.encodings)) for student in Student.objects.all() if student.encodings is not None]


    def is_admin_face(self, face):
        matches = []
        # try:
        face_admin_encodings = self.get_admin_faces()
        print('face_admin_encodings:', len(face_admin_encodings))
        face_encodings = self.get_encodings(face)
        for face_encoding in face_encodings:
            matches.extend(face_recognition.compare_faces(face_admin_encodings, face_encoding))    
        # except:
        #     pass
        return True in matches

    def get_encodings(self, photo):
        face_locations = face_recognition.face_locations(photo)
        face_encodings = face_recognition.face_encodings(photo, face_locations)
        return face_encodings

    