from django.db import models

# Create your models here.
class topic(models.Model):
    topic_name=models.CharField(max_length=100,primary_key=True)
    def __str__(self):
        return self.topic_name

class webpage(models.Model):
    topic_name=models.ForeignKey(topic, on_delete=models.CASCADE)
    name=models.CharField(max_length=100,unique=True)
    url=models.URLField(max_length=100,unique=True)
    def __str__(self):
        return self.name
    
class access_record(models.Model):
    name=models.ForeignKey(webpage, on_delete=models.CASCADE)
    date=models.DateField(auto_now=True)
    author=models.CharField(default='NO One', max_length=50)
    def __str__(self):
        return str(self.id)