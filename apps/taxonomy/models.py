from django.db import models


class Topic(models.Model):
    display_name = models.CharField(max_length=50)
    internal_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return '{} <{}>'.format(self.display_name, self.internal_name)
