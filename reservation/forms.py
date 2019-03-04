from django import forms
from django.forms import ModelForm
# might need to use my_project in place of 'reservation' below
from reservation.models import ReviseReservationModel

class ReviseReservationForm(forms.Form):
      
   model = ReviseReservationModel

   # field names in database table
   fields = (

      'schoolName',
	   'name',
	   'address1',
	   'address2',
	   'city',
	   'state',
	   'zipCode',
	   'phone',
	   'email',
	   'location',
	   'district',
		'dateStart',
      'dateEnd',
		'timeStart',
		'timeEnd',
		'lunch',
		'level',
		'gradeLevel',
		'ael',
      'mission',
		'tour',
		'handson',
		'eP',
		'summerCamp',
		'otherProg',
		'numStud',
		'numChap',
		'visCost',
		'progCost',
      'paymentDue',
      'interComm',
		'slowPay',
		'sayNo',
		'status',
		'progComm',
      
      )

   # Labels for fields on html page
   labels = {
      
      'schoolName': ('School/Group Name:'),
		'name': ('Name:'),
		'address1': ('Street Address 1:'),
		'address2': ('Street Address 2:'),
		'city': ('City:'),
		'state': ('State:'),
		'zipCode': ('Zip Code:'),
		'phone': ('Phone:'),
		'email': ('Email:'),
		'location': ('Location:'),
		'district': ('District:'),
		'dateStart': ('Start Date:'),
      'dateEnd': ('End Date:'),
		'timeStart': ('Start Time:'),
		'timeEnd': ('End Time:'),
		'lunch': ('30 Minute Lunch:'),
		'level': ('Level:'),
	 	'gradeLevel': ('Grade Level:'),
		'ael': ("AEL:"),
      'mission': ("Mission:"),
		'tour': ("Tour:"),
		'handson': ("Handson:"),
		'eP': ("eP:"),
		'summerCamp': ("Summer Camp:"),
		'otherProg': ("Other:"),
		'numStud': ('Number of Students:'),
		'numChap': ('Number of Chaperones:'),
		'visCost': ('Student Cost:'),
		'progCost': ('Program Cost:'),
      'paymentDue': ('Payment Due:'), 
      'interComm': ('Comments:'),
		'slowPay': ("Slow Pay:"),
		'sayNo': ("Say No:"),
		'status': ("Status:"),
		'progComm': ("ProgComm:"),
      
      }

   def __str__(self) :
      return self