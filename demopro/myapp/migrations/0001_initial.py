# Generated by Django 2.2.4 on 2020-05-24 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('course_id', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
            ],
        ),
    ]