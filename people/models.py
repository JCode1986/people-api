from django.db import models
from django.contrib.auth.models import User
from django import forms
from datetime import date


COLOR_CHOICES= [
    ('green','GREEN'),
    ('blue', 'BLUE'),
    ('red','RED'),
    ('orange','ORANGE'),
    ('black','BLACK'),
    ('purple','PURPLE'),
    ('yellow','YELLOW'),
    ('pink', 'PINK'),
    ('brown','BROWN'),
    ('white','WHITE'),
    ]

# https://docs.djangoproject.com/en/3.0/topics/db/models/
class People(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
    favorite_color = models.CharField(max_length=6, choices=COLOR_CHOICES, default='green')
    birth_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nickname} -- Age: {self.calculate_age()} -- Boomer Status: {self.baby_boomer_status()}'

    def baby_boomer_status(self):
        "Returns the person's baby-boomer status."
        if self.birth_date < date(1945, 8, 1):
            return "Pre-boomer"
        elif self.birth_date < date(1965, 1, 1):
            return "Baby boomer"
        else:
            return "Post-boomer"

    def calculate_age(self):
        today = date.today()
        birth_date = self.birth_date
        return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

    @property
    def full_name(self):
        "Returns the person's full name."
        return f'{self.first_name} {self.last_name}'
