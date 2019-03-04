from django.db import models
from django.conf import settings
from django.utils import timezone


# from status.forms import ModelForm


class ReportModel(models.Model):
    month = models.CharField(null=True, max_length=100)

    def __str__(self):
        return self
