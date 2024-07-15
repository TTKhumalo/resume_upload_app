from django.db import models
from django.contrib.auth.models import User


class RESUME(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    excel_file = models.FileField(upload_to="resumes/")
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.JSONField(null=True, blank=True)

    # Additional fields
    first_name = models.CharField(max_length=100, default="")
    last_name = models.CharField(max_length=100, default="")
    email = models.EmailField(default="")
    phone_number = models.CharField(max_length=20, default="")
    summary = models.TextField(default="")
    experience = models.TextField(default="")
    education = models.TextField(default="")

    def __str__(self):
        return (
            f"{self.first_name} {self.last_name}'s RESUME uploaded on {self.created_at}"
        )
