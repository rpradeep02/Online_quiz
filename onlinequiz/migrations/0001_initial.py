# Generated by Django 3.1.4 on 2021-01-18 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question', models.CharField(max_length=300)),
                ('Option1', models.CharField(max_length=300)),
                ('Option2', models.CharField(max_length=300)),
                ('Option3', models.CharField(max_length=300)),
                ('Option4', models.CharField(max_length=300)),
                ('Correctans', models.CharField(max_length=300)),
            ],
        ),
    ]
