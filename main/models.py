from django.db import models


# Create your models here.
class Idea(models.Model):
    idea_text = models.CharField(max_length=2000)
    idea_date = models.DateTimeField('date published')

    def __str__(self):
        return self.idea_text

