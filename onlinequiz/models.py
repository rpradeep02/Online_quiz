from django.db import models

# Create your models here.
class Exam(models.Model):
    Question = models.CharField(max_length=300)
    Option1 = models.CharField(max_length=300)
    Option2 = models.CharField(max_length=300)
    Option3 = models.CharField(max_length=300)
    Option4 = models.CharField(max_length=300)
    Correctans = models.CharField(max_length=300)

    def __str__(self):
        return self.Question