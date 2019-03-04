from django.db import models
from django.conf import settings
from django.utils import timezone
#from reservation.forms import ModelForm

# Create your models here.



class ReviseReservationModel(models.Model):
	schoolName = models.CharField(max_length = 140)
	name = models.CharField(max_length=140)
	address1 = models.CharField(max_length = 140)
	address2 = models.CharField(max_length=140)
	city = models.CharField(max_length = 140)
	state = models.CharField(max_length = 140)
   # change to zipCode, zip seems to be keyword
	zipCode = models.CharField(max_length = 140)
	phone = models.IntegerField(null=True)
	email = models.CharField(max_length = 140)
	location = models.CharField(max_length = 140)
	district = models.BooleanField(null=True)
	dateStart = models.DateField(null=True)
	dateEnd = models.DateField(null=True)
	timeStart = models.TimeField(null=True)
	timeEnd = models.TimeField(null=True)
	lunch = models.BooleanField(null=True)
	level = models.CharField(max_length=24)
	gradeLevel = models.CharField(max_length=24)
	ael = models.CharField(max_length = 140)
	mission = models.CharField(max_length=140)
	tour = models.CharField(max_length = 140)
	handson = models.CharField(max_length = 140)
	eP = models.CharField(max_length = 140)
	summerCamp = models.CharField(max_length = 140)
	otherProg = models.CharField(max_length = 140)
	numStud = models.IntegerField(null=True)
	numChap = models.IntegerField(null=True)
	visCost = models.IntegerField(null=True)
	progCost = models.IntegerField(null=True)
	paymentDue = models.IntegerField(null=True)
	interComm = models.CharField(max_length = 140)
	slowPay = models.BooleanField(null=True)
	sayNo = models.BooleanField(null=True)
	status = models.CharField(max_length = 140)
	progComm = models.CharField(max_length = 140)

	def __str__(self):
		return self