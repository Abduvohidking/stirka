from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(verbose_name="Ism", max_length=100)
    username = models.CharField(verbose_name="Telegram username", max_length=100, null=True)
    telegram_id = models.BigIntegerField(verbose_name='Telegram ID', unique=True, default=1)

    def __str__(self):
        return f"{self.id} - {self.telegram_id} - {self.full_name}"

class Gilam(models.Model):
    NEW = 'new'
    PENDING = 'pending'
    PROCESSING = 'processing'
    COMPLETED = 'completed'
    CANCELED = 'canceled'

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (PROCESSING, 'Processing'),
        (COMPLETED, 'Completed'),
        (CANCELED, 'Canceled'),
    ]

    id = models.AutoField(primary_key=True)
    user_id = models.BigIntegerField(unique=True)
    user_name = models.CharField(max_length=255,null=True)
    olcham = models.IntegerField(default=0, blank=False, null=False)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default=NEW)
    adress = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=100)
    sum = models.IntegerField(default=0, blank=False, null=False)

    def __str__(self):
        return f"{self.user_id} {self.user_name} - {self.phone_number}"