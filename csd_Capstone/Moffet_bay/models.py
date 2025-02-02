from django.db import models

from django.db import models

class Registration(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    phone = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)  # Store hashed password later
    returning_customer = models.BooleanField(default=False)  # Radio button

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"


class Login(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=255)  # Store hashed password later
    login_attempted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Login attempt for {self.email} at {self.login_attempted_at}"

