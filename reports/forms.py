from django import forms
# from django.forms import ModelForm
from reports.models import ReportModel


class StatusForm(forms.Form):
    model = ReportModel
    # field names in database table
    fields = (

        'month',

    )
    # Labels for fields on html page
    labels = {

        'month': ('Month:'),

    }
