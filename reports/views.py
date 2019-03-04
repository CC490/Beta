from django.shortcuts import render, reverse, get_object_or_404, render_to_response
from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpResponseNotFound
from status.models import StatusModel
from reservation.models import ReviseReservationModel
from status.forms import StatusForm
from django.template.response import TemplateResponse
from django.views.generic import View
from django.template.loader import get_template
from my_project.utils import render_to_pdf
from django.utils import timezone
#from datetime import datetime

# Create your views here.
def ReportView(request):
    return render(request, 'reports.html')


def AcctRecView(request):
    pdf = render_to_pdf('acctRec.html')
    return HttpResponse(pdf, content_type='application/pdf')


def MonthVisView(request):
    pdf = render_to_pdf('monthVis.html')
    return HttpResponse(pdf, content_type='application/pdf')


def AttendView(request):
    pdf = render_to_pdf('attend.html')
    return HttpResponse(pdf, content_type='application/pdf')


def AllDataView(request):
   pdf = render_to_pdf('allData.html')
   return HttpResponse(pdf, content_type='application/pdf')

