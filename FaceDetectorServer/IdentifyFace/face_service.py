import os
from PIL import Image
import face_recognition
from .tools import *
import numpy as np


class FaceService:

    def get_admin_faces(self):
        faces = [np.array(Image.open("IdentifyFace\\admfaces\\" + f)) for f in os.listdir("IdentifyFace\\admfaces")]
        print("faces:", len(faces))
        face_encodings = []
        for face in faces:
            face_locations = face_recognition.face_locations(face)
            face_encodings.extend(face_recognition.face_encodings(face, face_locations))
        return face_encodings

    def is_admin_face(self, face):
        matches = []
        try:
            face_admin_encodings = self.get_admin_faces()
            face_encodings = self.get_encodings(face)
            for face_encoding in face_encodings:
                matches.extend(face_recognition.compare_faces(face_admin_encodings, face_encoding))    
        except:
            pass
        return True in matches

    def get_encodings(self, photo):
        face_locations = face_recognition.face_locations(photo)
        face_encodings = face_recognition.face_encodings(photo, face_locations)
        return face_encodings

    