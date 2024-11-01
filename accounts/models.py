from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.hashers import make_password


class Organization(models.Model):
    '''
    **Fields:**
    - created_on: DateTimeField to store the date and time when the organization was created.
    - name: CharField to store the name of the organization.
    - profile_picture: ForeignKey to store the profile picture of the organization
    - removed: BooleanField to store whether the organization is removed or not.
    '''
    name = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    profile_picture = models.ForeignKey('annotation.File', on_delete=models.SET_NULL, null=True, blank=True)
    removed = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    '''
    **Fields:**
    - first_name: CharField to store the first name of the user.
    - last_name: CharField to store the last name of the user.
    - password: CharField to store the password of the user.
    - email: EmailField to store the email address of the user.
    - is_admin: BooleanField to store whether the user is an admin or not.
    - username: CharField to store the username of the user.
    - organization: ForeignKey to store the organization of the user.
    - profile_picture: ForeignKey to store the profile picture of the user.
    - removed: BooleanField to store whether the user is removed or not.
    '''
    is_admin = models.BooleanField(default=False)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True, blank=True, related_name='members')
    profile_picture = models.ForeignKey('annotation.File', on_delete=models.SET_NULL, null=True, blank=True)
    removed = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions '
                   'granted to each of their groups.')
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    def save(self, *args, **kwargs):
        if self.password and not self.password.startswith('pbkdf2_sha256$'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
