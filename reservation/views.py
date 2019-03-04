from django.shortcuts import render, reverse, get_object_or_404, render_to_response
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from reservation.models import ReviseReservationModel
from status.models import StatusModel
from status.forms import StatusForm
from status.views import GenerateStatusInst
from reservation.forms import ReviseReservationForm
from django.template.response import TemplateResponse


# for 404 response
# return HttpResponse(status=404)

# or:

# import django.http.Http404
# return HttpResponseNotFound('<h1>Page not found</h1>')


# opens a blank reservation form

def NewReservationView(request) :
   return render(request, 'reservation/CreateReservation.html')


# posts the user populated reservation fields to the database
# creates a status entry in the database for this reservation

def NewReservationRedView(request):
   if request.method == 'POST' :
      form = ReviseReservationForm(request.POST)
      
      if form.is_valid() :
         gschoolName = request.POST.get('schoolName', '')
         gname = request.POST.get('name', '')
         gaddress1 = request.POST.get('address1', '')
         gaddress2 = request.POST.get('address2', '')
         gcity = request.POST.get('city', '')
         gstate = request.POST.get('state', '')
         gzipCode = request.POST.get('zipCode', '')
         gphone = request.POST.get('phone', '')
         gemail = request.POST.get('email', '')
         glocation = request.POST.get('location', '')
         gdistrict = request.POST.get('district', '')
         if gdistrict == 'on' :
            gdistrict = True
         else :
           gdistrict = False
         gdateStart = request.POST.get('dateStart', '')
         gdateEnd = request.POST.get('dateEnd', '')
         gtimeStart = request.POST.get('timeStart', '')
         gtimeEnd = request.POST.get('timeEnd', '')
         glunch = request.POST.get('lunch', '')
         if glunch == 'on':
             glunch = True
         else:
             glunch = False
         glevel = request.POST.get('level', '')
         ggradeLevel = request.POST.get('gradeLevel', '')
         gael = request.POST.get('ael', '')
         gmission = request.POST.get('mission', '')
         gtour = request.POST.get('tour', '')
         ghandson = request.POST.get('handson', '')
         geP = request.POST.get('eP', '')
         gsummerCamp = request.POST.get('summerCamp', '')
         gotherProg = request.POST.get('otherProg', '')
         gnumStud = request.POST.get('numStud', '')
         gnumChap = request.POST.get('numChap', '')
         gvisCost = request.POST.get('visCost', '')
         gprogCost = request.POST.get('progCost', '')
         gpaymentDue = request.POST.get('paymentDue', '')
         ginterComm = request.POST.get('interComm', '')
         gslowPay = request.POST.get('slowPay', '')
         if gslowPay == 'on':
             gslowPay = True
         else:
             gslowPay = False
         gsayNo = request.POST.get('sayNo', '')
         if gsayNo == 'on':
             gsayNo = True
         else:
             gsayNo = False
         gstatus = request.POST.get('status', '')
         gprogComm = request.POST.get('progComm', '')
         
         res_obj = ReviseReservationModel (
			schoolName = gschoolName,
            name = gname,
			address1 = gaddress1,
            address2 = gaddress2,
			city = gcity,
			state = gstate,
			zipCode = gzipCode,
			phone = gphone,
			email = gemail,
         location = glocation,
			district = gdistrict,
         dateStart = gdateStart,
         dateEnd = gdateEnd,
         timeStart = gtimeStart,
         timeEnd = gtimeEnd,
         lunch = glunch,
         level = glevel,
         gradeLevel = ggradeLevel,
         ael = gael,
         mission = gmission,
         tour = gtour,
         handson= ghandson,
         eP = geP,
         summerCamp = gsummerCamp,
         otherProg = gotherProg,
			numStud = gnumStud,
			numChap = gnumChap,
			visCost = gvisCost,
			progCost = gprogCost,
         paymentDue = gpaymentDue,
         interComm = ginterComm,
         slowPay = gslowPay,
         sayNo = gsayNo,
         status = gstatus,
         progComm = gprogComm
         
         )

         res_obj.save()


         # creates a new instance of the status form for this reservation instance
         stat_form = StatusForm(request.POST)
         if stat_form.is_valid :
            
            stat_obj_id = res_obj.pk
            
            GenerateStatusInst(request, stat_obj_id)
         
		 
         return render(request, 'reservation/reservationSubmitted.html')


   return HttpResponseNotFound('<h1>Page not found</h1>')
   



# passes pk-id to arg "id_arg," gets that reservation object, returns it to the
# read-only template. 
def ReservationSummaryView(request, id) :
   
   res_obj = get_object_or_404(ReviseReservationModel, pk=id)
   
   return TemplateResponse(request, 'reservation/ReservationSummary.html', {'res_obj': res_obj})


# Deletes status and reservation tables from status page
def DeleteReservationView(request, id) :

   status_obj = get_object_or_404(StatusModel, pk=id)

   res_obj = get_object_or_404(ReviseReservationModel, pk=id)

   id_num = status_obj.pk

   status_obj.delete()

   res_obj.delete()

   return TemplateResponse(request, 'reservation/reservationDeleted.html', {'id_num': id_num})



# opens an editable reservation page with fields prepopulated from db entry of pk==id

def ReviseReservationView(request, id) :

   res_obj = get_object_or_404(ReviseReservationModel, pk=id)

   return TemplateResponse(request, 'reservation/ReviseReservation.html', { 'res_obj' : res_obj })







# allows for user update of database reservation entries
def EditReservationRedView(request, id):
   if request.method == 'POST' :
      form = ReviseReservationForm(request.POST)
      
      if form.is_valid() :
         gschoolName = request.POST.get('schoolName', '')
         gname = request.POST.get('name', '')
         gaddress1 = request.POST.get('address1', '')
         gaddress2 = request.POST.get('address2', '')
         gcity = request.POST.get('city', '')
         gstate = request.POST.get('state', '')
         gzipCode = request.POST.get('zipCode', '')
         gphone = request.POST.get('phone', '')
         gemail = request.POST.get('email', '')
         glocation = request.POST.get('location', '')
         gdistrict = request.POST.get('district', '')
         if gdistrict == 'on' :
            gdistrict = True
         else :
           gdistrict = False
         gdateStart = request.POST.get('dateStart', '')
         gdateEnd = request.POST.get('dateEnd', '')
         gtimeStart = request.POST.get('timeStart', '')
         gtimeEnd = request.POST.get('timeEnd', '')
         glunch = request.POST.get('lunch', '')
         if glunch == 'on':
             glunch = True
         else:
             glunch = False
         glevel = request.POST.get('level', '')
         ggradeLevel = request.POST.get('gradeLevel', '')
         gael = request.POST.get('ael', '')
         gmission = request.POST.get('mission', '')
         gtour = request.POST.get('tour', '')
         ghandson = request.POST.get('handson', '')
         geP = request.POST.get('eP', '')
         gsummerCamp = request.POST.get('summerCamp', '')
         gotherProg = request.POST.get('otherProg', '')
         gnumStud = request.POST.get('numStud', '')
         gnumChap = request.POST.get('numChap', '')
         gvisCost = request.POST.get('visCost', '')
         gprogCost = request.POST.get('progCost', '')
         gpaymentDue = request.POST.get('paymentDue', '')
         ginterComm = request.POST.get('interComm', '')
         gslowPay = request.POST.get('slowPay', '')
         if gslowPay == 'on':
             gslowPay = True
         else:
             gslowPay = False
         gsayNo = request.POST.get('sayNo', '')
         if gsayNo == 'on':
             gsayNo = True
         else:
             gsayNo = False
         gstatus = request.POST.get('status', '')
         gprogComm = request.POST.get('progComm', '')
         
         res_obj = ReviseReservationModel (
         pk=id,
			schoolName = gschoolName,
            name = gname,
			address1 = gaddress1,
            address2 = gaddress2,
			city = gcity,
			state = gstate,
			zipCode = gzipCode,
			phone = gphone,
			email = gemail,
         location = glocation,
			district = gdistrict,
         dateStart = gdateStart,
         dateEnd = gdateEnd,
         timeStart = gtimeStart,
         timeEnd = gtimeEnd,
         lunch = glunch,
         level = glevel,
         gradeLevel = ggradeLevel,
         ael = gael,
         mission = gmission,
         tour = gtour,
         handson= ghandson,
         eP = geP,
         summerCamp = gsummerCamp,
         otherProg = gotherProg,
			numStud = gnumStud,
			numChap = gnumChap,
			visCost = gvisCost,
			progCost = gprogCost,
         paymentDue = gpaymentDue,
         interComm = ginterComm,
         slowPay = gslowPay,
         sayNo = gsayNo,
         status = gstatus,
         progComm = gprogComm
         
         )

         res_obj.save()
         
		 
         return render(request, 'reservation/reservationSubmitted.html')

   return HttpResponseNotFound('<h1>Page not found</h1>')





