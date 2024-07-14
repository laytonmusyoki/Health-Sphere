from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Token(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"Token for {self.user.username}"
    


class OtpCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    verified=models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"OTP for {self.user.username}"
    


class Workouts(models.Model):
    vedio=models.FileField(upload_to="workouts")
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=1000)

    def __str__(self):
        return self.title
    


class Feeds(models.Model):
    image=models.ImageField(upload_to='feeds')
    title=models.CharField(max_length=200)
    sub_title=models.CharField(max_length=200)
    description=models.CharField(max_length=1000)

    def __str__(self) -> str:
        return self.title

