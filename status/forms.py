from django import forms
#from django.forms import ModelForm
from status.models import StatusModel



class StatusForm(forms.Form):
   model = StatusModel
   # field names in database table
   fields = (
      
      'depDue',
      'depRec',
      'conSent',
      'conRec',
      'conRecDate',
      'cancelled',
      'payAmount',
      'paymentDue',
      
      )
# Labels for fields on html page
   labels = {

      'depDue': ('Deposit Due:'),
      'depRec': ('Deposit Received:'),
      'conSent': ('Confirmation Sent:'),
      'conRec': ('Confirmation Received:'),
      'conRecDate': ('Confirmation Received Date:'),
      'cancelled': ('Cancelled:'),
      'payAmount': ('Payment Amount:'),
      'paymentDue': ("Payment Due:"),
      
      }

#   def __str__(self) :
#      return self

#      widgets = {
#      }
#      error_messages = {
# use exact syntax below, including quotes and commas. may need underscore
# leading the message parenthesis, but it threw error message
# so will try not using it.
# 'dbFieldName': {
#
#    'error_name': ("Desired Custom Error Message."),
#
# },
#      }
# might need below:
# def clean_names(self):
# ...custom validation for name field
