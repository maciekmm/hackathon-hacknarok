from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class RoomCategory(models.Model):
    caption = models.CharField(max_length=128)

    def __str__(self):
        return self.caption


class Room(models.Model):
    caption = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    limit = models.IntegerField(blank=True, null=True)
    start = models.DateTimeField()
    end = models.DateTimeField(null=True, blank=True)
    category = models.ForeignKey(RoomCategory, on_delete=models.SET_NULL, null=True)
    members = models.ManyToManyField(User)
    lon = models.DecimalField(max_digits=9, decimal_places=6)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    storey = models.IntegerField(blank=True, null=True)
    building_name = models.CharField(blank=True, max_length=128)
    room_number = models.CharField(blank=True, max_length=64)

    def __str__(self):
        return self.caption


class Profile(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    bio = models.TextField(max_length=512, blank=True)
    lon = models.DecimalField(null=True, blank=True, max_digits=9, decimal_places=6)
    lat = models.DecimalField(null=True, blank=True, max_digits=9, decimal_places=6)
    building_name = models.CharField(blank=True, null=True, max_length=128)
    room_number = models.CharField(blank=True, null=True, max_length=128)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
