from django.db import models
import datetime
from django.utils import timezone
from django.db.models.signals import post_save


class Ami(models.Model):
    ami_name = models.CharField(max_length=255)
    ami_id = models.CharField(max_length=12)
    platform = models.CharField(max_length=15)
    creation_date = models.DateTimeField(default=timezone.now())
    end_of_life_date = models.DateTimeField(default=timezone.now() + datetime.timedelta(days=60))
    creator = models.CharField(max_length=255,default="CCOE - Hybrid Cloud Team")

    def __str__(self):
        return self.ami_name
    # If EOL in next month, return false, else true
    def near_end_life(self):
        return self.end_of_life_date < (self.creation_date + datetime.timedelta(days=60))

class Update(models.Model):
    text = models.CharField(max_length=255)
    creation_date = models.DateTimeField(default=timezone.now())
    ami = models.ForeignKey(Ami, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
