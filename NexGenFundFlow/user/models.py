from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class InvestorProfile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    inverstor_phone_number = models.CharField(max_length=10)
    specialization = models.CharField(max_length=255)
    inverstor_avatar = models.ImageField(upload_to='images/',default='images/default.jpg')
    inverstor_birth_day = models.DateField()
    inverstor_x_link = models.URLField()
    inverstor_bio = models.TextField()
    inverstor_city = models.CharField(max_length=255)
    inverstor_LinkedIn = models.URLField()
    

    def __str__(self) -> str:
        return self.user.first_name


class StartupManagerProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    position = models.CharField(max_length=255)
    manager_phone_number = models.CharField(max_length=10)
    manager_avatar = models.ImageField(upload_to='images/',default='images/default.jpg')
    manager_birth_day = models.DateField()
    manager_x_link = models.URLField()
    manager_bio = models.TextField()
    manager_city = models.CharField(max_length=255)
    manager_LinkedIn = models.URLField()
    
    
    def __str__(self) -> str:
        return self.user.first_name
