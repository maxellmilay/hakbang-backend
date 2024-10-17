from django.db import models
import json


class File(models.Model):
    '''
    **Fields:**
    - created_on (read-only): DateTimeField to store the date and time when the file was created.
    - url (required): URLField to store the URL of the file.
    '''
    url = models.URLField()
    created_on = models.DateTimeField(auto_now_add=True)
    removed = models.BooleanField(default=False)

    def __str__(self):
        return self.url


class Location(models.Model):
    data = models.JSONField()
    removed = models.BooleanField(default=False)

    def __str__(self):
        serialized_data = json.dumps(self.data)
        name = serialized_data['name']
        if name:
            return name
        return self.id


class AnnotationForm(models.Model):
    data = models.JSONField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    removed = models.BooleanField(default=False)

    def __str__(self):
        serialized_data = json.dumps(self.data)
        name = serialized_data['name']
        if name:
            return name
        return self.id


class Annotation(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='annotations')
    name = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    annotator = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE, related_name='user_annotations')
    form_data = models.JSONField()
    form_template = models.ForeignKey(AnnotationForm, on_delete=models.SET_NULL, related_name='form_annotations', null=True, blank=True)
    removed = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class AnnotationImage(models.Model):
    file = models.ForeignKey(File, on_delete=models.CASCADE, related_name='image_annotations')
    annotation = models.ForeignKey(Annotation, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return self.image.url
