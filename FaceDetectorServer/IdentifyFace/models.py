from django.db import models

class Student(models.Model):
    name = models.TextField()
    surname = models.TextField()
    group = models.TextField()
    photo = models.ImageField(upload_to='images/')
    encodings = models.TextField(null=True)
    def __str__(self):
        return f"{self.name} {self.surname}"

class Log(models.Model):
    encoding = models.TextField()
    datetime = models.DateTimeField()
    image = models.ImageField(upload_to='logs/')