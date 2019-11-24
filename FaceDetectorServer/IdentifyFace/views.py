from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt


from django.views.generic import ListView, CreateView # new
from django.urls import reverse_lazy # new

from .forms import StudentForm # new
from .models import Student

import numpy as np
from .tools import *
from .face_service import FaceService
from .db_manager import DBManager
from datetime import datetime
from io import BytesIO
from PIL import  Image

def index(request):
    return HttpResponse("Student added.")


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
            student = {"encoding" : encoding.tolist(), 
                       "face":received_json_data['face'],
                       "name":received_json_data['name'],
                       "surname":received_json_data['surname'],
                       "group":received_json_data['group'],
                       }
            db.add_student(student)
            return HttpResponse('0')
        except :
            return HttpResponse('1')
    else:
        return HttpResponse('2')




class CreateStudentView(CreateView): 
    model = Student
    form_class = StudentForm
    template_name = 'add_student.html'
    success_url = reverse_lazy('index')
    def form_valid(self, form):
        face_service = FaceService()
        student = form.instance
        _image = student.photo.read()
        image = BytesIO(_image)
        pil_image = Image.open(image)
        np_image = np.asarray(pil_image)
        encoding = face_service.get_encodings(np_image)[0]
        student.encodings = json.dumps(encoding.tolist())
        return super(CreateStudentView, self).form_valid(form)