# Generated by Django 2.2.7 on 2019-12-11 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Userapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userreg',
            name='Resume',
            field=models.FileField(upload_to='FileUpload/'),
        ),
    ]
