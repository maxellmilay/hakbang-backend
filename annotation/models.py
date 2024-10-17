from django.db import models


class File(models.Model):
    url = models.URLField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.url

