# Generated by Django 2.2.5 on 2019-11-24 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IdentifyFace', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='encodings',
            field=models.TextField(null=True),
        ),
    ]
