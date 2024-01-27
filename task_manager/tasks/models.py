from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=85)
    content = models.CharField(max_length=255)
    data_posted = models.DateTimeField(auto_now_add=True)


class Review(models.Model):
    reviewer_name = models.CharField(max_length=255)
    reviewer_title = models.CharField(max_length=255)

    task = models.ForeignKey(Task, on_delete= models.CASCADE)