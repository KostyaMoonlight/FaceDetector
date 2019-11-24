from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt


from django.views.generic import ListView, CreateView # new
from django.urls import reverse_lazy # new

from .forms import StudentForm # new
from .models import Student, Log
import os
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
def verify_face(request):
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

        received_json_data=json.loads(request.body)
        face = restore_image(received_json_data['image'])
        try:
            encoding = face_service.get_encodings(face)[0]
            pil_face= Image.fromarray(face)
            image_save_path = f"media/logs/log-{datetime.now()}.jpeg".replace(':','_')
            b, g, r = pil_face.split()
            pil_face = Image.merge("RGB", (r, g, b))
            pil_face.save(image_save_path, "JPEG")
            log = Log(encoding=encoding, datetime =datetime.now(), image=image_save_path)
            log.save()
            return HttpResponse('0')
        except Exception as e:
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