from django.db import models


class Paint(models.Model):
    title = models.CharField(max_length=255, blank=False)
    description = models.TextField(max_length=255, blank=False)
    date = models.DateTimeField(auto_now_add=False)
    image = models.ImageField(upload_to="paint_images", blank=True, null=True)

    def __str__(self):
        return self.title
