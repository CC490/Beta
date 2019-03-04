from django.db import models
from django.conf import settings
from django.utils import timezone
#from status.forms import ModelForm


class StatusModel(models.Model) :

   depDue = models.CharField(null=True, max_length=5)
   depRec = models.CharField(null=True, max_length=5)
   conSent = models.CharField(null=True, max_length=5)
   conRec = models.CharField(null=True, max_length=5)
   # may need timezone.now().date, but parens make it change every instance update
   conRecDate = models.DateField(null=True, default = timezone.now)
   cancelled = models.CharField(null=True, max_length=5)
   payAmount = models.IntegerField(null=True, default=0)
   paymentDue = models.IntegerField(null=True)
   
   def __str__(self) :
      return self
