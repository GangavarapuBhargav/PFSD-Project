from django.db import models
from django.core.validators import RegexValidator, MaxLengthValidator

class Teacher(models.Model):
    # Username with up to 6 digits
    username_validator = RegexValidator(
        regex=r'^\d{1,6}$', 
        message="Username must be up to 6 digits."
    )
    
    username = models.CharField(max_length=6, validators=[username_validator], unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    subject = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"


class Student(models.Model):
    # Username can contain letters and digits, length up to 8
    username = models.CharField(max_length=8, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"
