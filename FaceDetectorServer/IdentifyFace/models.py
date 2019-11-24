from django.db import models


class Student(models.Model):
    name = models.TextField()
    surname = models.TextField()
    group = models.TextField()
    photo = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"{self.name} {self.surname}"