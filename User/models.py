from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    description=models.TextField(blank=True, null=True)
    phone_number=models.CharField(max_length=15,blank=True, null=True)
    picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    group=models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True
    )
    user_permissions= models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions_set',
        blank=True
    )
    class Meta:
        db_table='user_customuser'
class Followers(models.Model):
    followed=models.ForeignKey("CustomUser", related_name="followed", on_delete=models.CASCADE)
    following=models.ForeignKey("CustomUser", related_name="follower", on_delete=models.CASCADE)
    created_at=models.DateField(auto_now_add=True)
