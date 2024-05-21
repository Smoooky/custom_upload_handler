from django.db import models


class TestModel(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='test')

    def __str__(self):
        return self.name
