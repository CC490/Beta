from django.shortcuts import render, reverse, get_object_or_404, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from reservation.models import ReviseReservationModel
from reservation.forms import ReviseReservationForm
from django.template.response import TemplateResponse
from status.models import StatusModel
# Create your views here.

# Remove this from reservation if it works
def HomeReservationView(request) :
   
   reservations = ReviseReservationModel.objects.all()
   status_objs = StatusModel.objects.all()

   home_objs = zip(reservations, status_objs)

   return TemplateResponse(request, 'home.html', {'home_objs': home_objs})
   
#   return TemplateResponse(request, 'home.html', { "reservations": reservations, 'status_objs': status_objs })
