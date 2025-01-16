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

    latitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)
    removed = models.BooleanField(default=False)

    class Meta:
        unique_together = ('latitude', 'longitude')

    def __str__(self):
        return f"({self.latitude}, {self.longitude})"


class Sidewalk(models.Model):
    """
    Represents a sidewalk segment with flexible data and results structure.

    Attributes:
        accessibility_score (DecimalField): The accessibility score of the sidewalk
        adjacent_street (CharField): The name of the adjacent street.
        data (JSONField): Stores location data in JSON format.
        results (JSONField): Stores results data in JSON format.
        anchor (CharField); The nearest anchor location of the sidewalk
        start_coordinates (ForeignKey): The starting coordinates of the location.
        end_coordinates (ForeignKey): The ending coordinates of the location.
        removed (BooleanField): Indicates if the location has been marked as removed.
    """

    ANCHOR_A = '123.9419001850121,10.327600060884297'
    ANCHOR_B = '123.94220321636607,10.328668797875494'
    ANCHOR_C = '123.94318663887299,10.327099440742616'
    ANCHOR_D = '123.94351254051777,10.328185054214456'
    ANCHOR_E = '123.94495908641485,10.32757193618587'
    ANCHOR_F = '123.94445022244315,10.326536945241577'

    ANCHOR_CHOICES = (
        (ANCHOR_A, 'Anchor A'),
        (ANCHOR_B, 'Anchor B'),
        (ANCHOR_C, 'Anchor C'),
        (ANCHOR_D, 'Anchor D'),
        (ANCHOR_E, 'Anchor E'),
        (ANCHOR_F, 'Anchor F'),
    )

    accessibility_score = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    adjacent_street = models.CharField(max_length=255, blank=True, null=True)
    data = models.JSONField()
    results = models.JSONField(blank=True, null=True)
    anchor = models.CharField(max_length=50, choices=ANCHOR_CHOICES, default=ANCHOR_C)
    start_coordinates = models.ForeignKey(Coordinates, on_delete=models.CASCADE, related_name='start_sidewalk')
    end_coordinates = models.ForeignKey(Coordinates, on_delete=models.CASCADE, related_name='end_sidewalk')
    removed = models.BooleanField(default=False)

    class Meta:
        unique_together = ('start_coordinates', 'end_coordinates')

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
        name (CharField): The name of the form.
        template (JSONField): Stores form template data in JSON format.
        created_on (DateTimeField): The date and time when the form was created (auto-set).
        updated_on (DateTimeField): The date and time when the form was last updated (auto-set).
        removed (BooleanField): Indicates if the form has been marked as removed.
    """

    name = models.CharField(max_length=255)
    template = models.JSONField()
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
        sidewalk (ForeignKey): The sidewalk associated with this annotation.
        name (CharField): The name of the annotation.
        created_on (DateTimeField): The date and time when the annotation was created (auto-set).
        updated_on (DateTimeField): The date and time when the annotation was last updated (auto-set).
        annotator (ForeignKey): The user who created the annotation.
        data (JSONField): The data of the annotation in JSON format.
        template (ForeignKey): The template used for this annotation, if any.
        removed (BooleanField): Indicates if the annotation has been marked as removed.
    """
    User = get_user_model()

    FLOOD_HAZARD = {
        '0': 0,
        '1': 0,
        '2': 1,
        '3': 2
    }

    BORDER_BUFFER = {
        'No': 0,
        'Yes': 1
    }

    LIGHTING_CONDITION = {
        'Poor': 1,
        'Adequate': 2,
        'Excellent': 3
    }

    ZONING_AREA = {
        'City Core Commercial': 1,
        'Residential': 2,
        'Industrial': 3
    }

    sidewalk = models.ForeignKey(Sidewalk, on_delete=models.CASCADE, related_name='annotations')
    name = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    annotator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='annotations')
    data = models.JSONField()
    template = models.ForeignKey(AnnotationForm, on_delete=models.SET_NULL, related_name='annotations', null=True, blank=True)
    coordinates = models.ForeignKey(Coordinates, on_delete=models.CASCADE, related_name='annotations')
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
    
    file = models.ForeignKey(File, on_delete=models.CASCADE, related_name='annotation_image')
    annotation = models.ForeignKey(Annotation, on_delete=models.CASCADE, related_name='annotation_images')

    def __str__(self):
        return self.file.url
