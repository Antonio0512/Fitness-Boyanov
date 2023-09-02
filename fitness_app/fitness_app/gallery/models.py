from django.db import models

class Gallery(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

class Photo(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='gallery_photos/')
    caption = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.caption or self.image.name
