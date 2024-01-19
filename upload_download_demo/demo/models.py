from django.db import models
from os.path import basename


class Record(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')

    def get_image_name(self):
        return basename(self.image.name)

