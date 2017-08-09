from django.db import models

class Exhibition(models.Model):
    title = models.CharField(max_length=250)
    file = models.FileField()
    text = models.CharField(max_length=2500)

    def __str__(self):
        return self.title
	
	
    
