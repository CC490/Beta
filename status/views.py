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



# for 404 response
# return HttpResponse(status=404)

# or:

# import django.http.Http404
# return HttpResponseNotFound('<h1>Page not found</h1>')




#def Status(request):
#    status = StatusModel.objects.all()
#    return TemplateResponse(request, 'home.html', {"status": status})



def StatusSummaryView(request, id):
    status_obj = get_object_or_404(StatusModel, pk=id)
    res_obj = get_object_or_404(ReviseReservationModel, pk=id)
    return TemplateResponse(request, 'status/statusSummary.html', {'status_obj': status_obj, 'res_obj': res_obj})


def StatusPDFView(request, id) :
#   template = get_template('pdf/invoice.html')

   status_obj = get_object_or_404(StatusModel, pk=id)

   res_obj = get_object_or_404(ReviseReservationModel, pk=id)

#   stat_dict = {'stat_obj': stat_obj, 'res_obj': res_obj}

#   html = template.render(stat_dict)

   pdf = render_to_pdf('status/statuspdf.html', {'status_obj': status_obj, 'res_obj': res_obj})


#   pdf = render_to_pdf('pdf/invoice.html', stat_dict)

   return HttpResponse(pdf, content_type='application/pdf')

#   return HttpResponse(html)


# Deletes status and reservation tables from status page
def DeleteStatusView(request, id) :

   status_obj = get_object_or_404(StatusModel, pk=id)

   res_obj = get_object_or_404(ReviseReservationModel, pk=id)

   id_num = status_obj.pk

   status_obj.delete()

   res_obj.delete()

   return TemplateResponse(request, 'status/statusDeleted.html', {'id_num': id_num})






def ReviseStatusView(request, id):
   status_obj = get_object_or_404(StatusModel, pk=id)
   res_obj = get_object_or_404(ReviseReservationModel, pk=id)
   return render(request, 'status/status.html', {'status_obj': status_obj, 'res_obj': res_obj})



def ReviseStatusRedView(request, id):
   
   if request.method == 'POST' :
      form = StatusForm(request.POST)
      
      if form.is_valid() :
         
         gdepDue = request.POST.get('depDue', '')
         gdepRec = request.POST.get('depRec', '')
         gconSent = request.POST.get('conSent', '')
         gconRec = request.POST.get('conRec', '')
         gconRecDate = request.POST.get('conRecDate', '')
         gcancelled = request.POST.get('cancelled', '')
         gpayAmount = request.POST.get('payAmount', '')
         gpaymentDue = request.POST.get('paymentDue', '')
         
         
         status_obj = StatusModel(
         pk=id,
         depRec=gdepRec,
         depDue=gdepDue,
         conSent=gconSent,
         conRec=gconRec,
         conRecDate=gconRecDate,
         cancelled=gcancelled,
         payAmount=gpayAmount,
         paymentDue=gpaymentDue
         
         )
            
         status_obj.save()
            
         return render(request, 'status/statusUpdated.html')

   return HttpResponseNotFound('<h1>Page not found</h1>')





def GenerateStatusInst(request, id) :
   if request.method == 'POST':
      form = StatusForm(request.POST)

   if form.is_valid():
      gdepDue = request.POST.get('depDue', '')
      gdepRec = request.POST.get('depRec', '')
      gconSent = request.POST.get('conSent', '')
      gconRec = request.POST.get('conRec', '')
      gconRecDate = request.POST.get('conRecDate')
      gcancelled = request.POST.get('cancelled', '')
      gpayAmount = request.POST.get('payAmount', '0')
      gpaymentDue = request.POST.get('paymentDue', '')

      status_obj = StatusModel(
      depRec=gdepRec,
      depDue=gdepDue,
      conSent=gconSent,
      conRec=gconRec,
      conRecDate=gconRecDate,
      cancelled=gcancelled,
      payAmount=gpayAmount,
      paymentDue=gpaymentDue,
      
      )
      
      status_obj.save()




#class GeneratePDF(View) :

#   def MakePDF(request, id) :

#      template = get_template('pdf/invoice.html')

#      stat_obj = get_object_or_404(StatusModel, pk=id)

#      res_obj = get_object_or_404(ReviseReservationModel, pk=id)

#      stat_dict = {'stat_obj': stat_obj, 'res_obj': res_obj}

#      html = template.render(stat_dict)

#      return HttpResponse(html)

#      stat_dict = {'stat_obj': stat_obj, 'res_obj': res_obj}

#      stat_pdf = render_to_pdf('pdf/invoice.html', stat_dict)

#      return HttpResponse(stat_pdf, content_type='application/pdf')






#   def get(self, request, *args, **kwargs) :

#      data = {}

#      pdf = render_to_pdf('pdf/invoice.html', data)

#      return HttpResponse(pdf, content_type='application/pdf')

# to force download:
#      
#   def get(self, request, *args, **kwargs):
#      template = get_template('invoice.html')
      
#      context = {
#         "invoice_id": 123,
#         "customer_name": "John Cooper",
#         "amount": 1399.99,
#         "today": "Today",
#         }
         
#      html = template.render(context)
#      pdf = render_to_pdf('invoice.html', context)
#      if pdf:
#         response = HttpResponse(pdf, content_type='application/pdf')
#         filename = "Invoice_%s.pdf" %("12341231")
#         content = "inline; filename='%s'" %(filename)
#         download = request.GET.get("download")
#         if download:
#            content = "attachment; filename='%s'" %(filename)
#            response['Content-Disposition'] = content
         
#         return response
#      return HttpResponse("Not found")