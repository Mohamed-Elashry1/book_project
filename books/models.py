from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Book(models.Model):
    uploaded_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(max_length=500, null=False, blank=False, default='type any description')
    author = models.CharField(max_length=20, null=False, blank=False)
    image = models.ImageField(upload_to='books/cover/', null=False, blank=False)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} - {self.title[:20]}..."
    