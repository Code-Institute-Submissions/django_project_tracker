from django.db import models
from django.conf import settings 


class Item(models.Model):
    
    Issue = models.CharField(max_length=30, blank=False)
    done = models.BooleanField(blank=False, default=False)

    last_updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    date_created = models.DateTimeField(auto_now=False, auto_now_add=True)

    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)

    def __str__(self):
        return self.Issue
    
class Feature(models.Model):
    name = models.CharField(max_length=30, blank=False)
    done = models.BooleanField(blank=False, default=False)

    last_updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    date_created = models.DateTimeField(auto_now=False, auto_now_add=True)

    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
    amount_needed = models.DecimalField(max_digits=6, decimal_places=2)
    like_cost = models.DecimalField(max_digits=6, decimal_places=2)
    money_received = models.DecimalField(max_digits=6, decimal_places=2)


    def __str__(self):
        return self.name

class Feedback(models.Model):
    feedback = models.CharField(max_length=200, blank=False)
    date_added = models.DateTimeField(auto_now=False, auto_now_add=True)
    name = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.feedback
