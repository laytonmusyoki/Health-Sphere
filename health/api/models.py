from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Token(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"Token for {self.user.username}"