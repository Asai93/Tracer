from django.db import models
from django.utils import timezone
# Create your models here.

class Project(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

class File(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    details = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

class Bug(models.Model):
    status_choices = (
        ('idle', 'Idle'),
        ('wip', 'WIP'),
        ('fixed', 'fixed'),
        ('pass', 'pass'),
        ('fail', 'fail')
    )
    project = models.ForeignKey(Project, null=True, blank=True, on_delete=models.SET_NULL)
    added_by = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    details = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(blank=True, null=True)
    solution = models.TextField(default='---ADD SOLUTION HERE---')
    modified_files = models.ForeignKey(File, null=True, blank=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=10, choices=status_choices, default='idle')

    def __str__(self):
        return self.title
