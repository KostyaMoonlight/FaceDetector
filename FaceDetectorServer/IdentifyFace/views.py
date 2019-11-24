from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt


import numpy as np
from .tools import *
from .face_service import FaceService
from .db_manager import DBManager
from datetime import datetime

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


@csrf_exempt
def get_face(request):
    if request.method == 'GET':
        return HttpResponse("Get face got get.")
    elif request.method == 'POST':
        face_service =FaceService()
        received_json_data=json.loads(request.body)
        face = restore_image(received_json_data['image'])
        isface = face_service.is_admin_face(face)
        if isface:
            return HttpResponse('0')
        else:
            return HttpResponse('1')

@csrf_exempt
def log_face(request):
    if request.method == 'POST':
        face_service =FaceService()
        db = DBManager()
        received_json_data=json.loads(request.body)
        face = restore_image(received_json_data['image'])
        try:
            encoding = face_service.get_encodings(face)[0]
            student = {"time":str(datetime.now()), "encoding" : encoding.tolist(), "face":received_json_data['image']}
            db.add_student(student)
            return HttpResponse('0')
        except :
            return HttpResponse('1')


def add_student(request):
    pass