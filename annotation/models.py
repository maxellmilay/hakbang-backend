from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

class File(models.Model):
    """
    Represents a file in the system.

    Attributes:
        url (URLField): The URL where the file is stored.
        created_on (DateTimeField): The date and time when the file was created (auto-set).
        removed (BooleanField): Indicates if the file has been marked as removed.
    """

    url = models.URLField()
    created_on = models.DateTimeField(auto_now_add=True)
    removed = models.BooleanField(default=False)

    def __str__(self):
        return self.url


class Coordinates(models.Model):
    """
    Represents a pair of coordinates.

    Attributes:
        latitude (DecimalField): The latitude of the coordinates.
        longitude (DecimalField): The longitude of the coordinates.
        removed (BooleanField): Indicates if the coordinates have been marked as removed
    """

    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    removed = models.BooleanField(default=False)

    def __str__(self):
        return f"({self.latitude}, {self.longitude})"


class Location(models.Model):
    """
    Represents a location with flexible data structure.

    Attributes:
        data (JSONField): Stores location data in JSON format.
        start_coordinates (ForeignKey): The starting coordinates of the location.
        end_coordinates (ForeignKey): The ending coordinates of the location.
        removed (BooleanField): Indicates if the location has been marked as removed.
    """

    data = models.JSONField()
    start_coordinates = models.ForeignKey(Coordinates, on_delete=models.CASCADE, related_name='start_location')
    end_coordinates = models.ForeignKey(Coordinates, on_delete=models.CASCADE, related_name='end_location')
    removed = models.BooleanField(default=False)

    def __str__(self):
        try:
            return self.data.get('name', str(self.id))
        except AttributeError:
            return str(self.id)

    def clean(self):
        if not isinstance(self.data, dict):
            raise ValidationError("Data must be a dictionary")


class AnnotationForm(models.Model):
    """
    Represents a template for annotation forms.

    Attributes:
        data (JSONField): Stores form template data in JSON format.
        created_on (DateTimeField): The date and time when the form was created (auto-set).
        updated_on (DateTimeField): The date and time when the form was last updated (auto-set).
        removed (BooleanField): Indicates if the form has been marked as removed.
    """

    name = models.CharField(max_length=255)
    form_data = models.JSONField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    removed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-updated_on']


class Annotation(models.Model):
    """
    Represents an annotation made by a user.

    Attributes:
        location (ForeignKey): The location associated with this annotation.
        name (CharField): The name of the annotation.
        created_on (DateTimeField): The date and time when the annotation was created (auto-set).
        updated_on (DateTimeField): The date and time when the annotation was last updated (auto-set).
        annotator (ForeignKey): The user who created the annotation.
        form_data (JSONField): The data of the annotation in JSON format.
        form_template (ForeignKey): The template used for this annotation, if any.
        removed (BooleanField): Indicates if the annotation has been marked as removed.
    """

    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='annotations')
    name = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    annotator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='user_annotations')
    form_data = models.JSONField()
    form_template = models.ForeignKey(AnnotationForm, on_delete=models.SET_NULL, related_name='form_annotations', null=True, blank=True)
    coordinates = models.ForeignKey(Coordinates, on_delete=models.CASCADE, related_name='coordinates_annotations')
    removed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def clean(self):
        if not isinstance(self.form_data, dict):
            raise ValidationError("Form data must be a dictionary")

    class Meta:
        ordering = ['-updated_on']


class AnnotationImage(models.Model):
    """
    Represents an image associated with an annotation.

    Attributes:
        file (ForeignKey): The file object representing the image.
        annotation (ForeignKey): The annotation this image is associated with.
    """
    
    file = models.ForeignKey(File, on_delete=models.CASCADE, related_name='image_annotations')
    annotation = models.ForeignKey(Annotation, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return self.image.url
