from django.contrib.auth.models import User
from django.db import models

class CustomUser(User):
    date_of_birth = models.DateField(null=True, blank=True)