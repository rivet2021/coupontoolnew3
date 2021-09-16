from django.shortcuts import render
import pandas as pd
import json
import requests
import openpyxl
from django.views.decorators.csrf import csrf_exempt
from copon.models import copons





# Create your views here.
 
def home(request):
    tags=request.GET.get('tags')
    url="https://api4coupons.com/v3/coupon/list"
    payload = json.dumps({
     "client_id": "6384889747946715134741991478448",
   "client_secret": "Pnhughk8ZhTJGxQkyhtc95TUVgPMtuE",
    "tags": tags
     })
    headers = {
    'Content-Type': 'application/json',
   'Cookie': 'PHPSESSID=8a3edbc2d235fdc4c16511cb4afa766d'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    data=response.json()

    coupon_info=data['coupon_info']

    context={
    'coupon_info': coupon_info
     }
    return render(request,'home.html',context)
#def sendsms(request):
#  camp=request.GET.get('coupen_id')
     
 # return render(request,'sendsms.html', {'camp_id': camp})

def smsdatabase(request):
  camp=request.GET.get('coupen_id')
  return render(request,'smsdatabase.html', {'camp_id': camp})
def smsdatabasedone(request):
  phonenumberlist = copons.objects.all()
  cam_id=request.GET.get('coupen_id')
  url = "https://api4coupons.com/v3/send/sms"
 

  for j in phonenumberlist:
        payload = json.dumps({
        "client_id": "6384889747946715134741991478448",
          "client_secret": "Pnhughk8ZhTJGxQkyhtc95TUVgPMtuE",
           "campaign": cam_id,
           "phone": j.cnumber,
        "sender": "APPOTP"
          })
        headers = {
          'Content-Type': 'application/json',
          'Cookie': 'PHPSESSID=6b8d40e13338ebdda12d3da572707bba'
           }

        response = requests.request("POST", url, headers=headers, data=payload)
        return render(request,'smsdatabasedone.html')  

         #return render(request,"smsdatabase.html",{'copons':phonenumberlist})
#@csrf_exempt 

#def smsdone(request):
  
 #excel_file = request.FILES["file"]
# cam_id=request.POST.get('cam_id')
#  url = "https://api4coupons.com/v3/send/sms"

 #wb = openpyxl.load_workbook(excel_file)
# worksheet = wb["Sheet1"]
 #for row in worksheet.iter_rows():
 #  for cell in row:
 #    payload = json.dumps({
#     "client_id": "6384889747946715134741991478448",
 #    "client_secret": "Pnhughk8ZhTJGxQkyhtc95TUVgPMtuE",
 #    "campaign": cam_id,
 #    "phone": cell.value,
 #    "sender": "APPOTP"
 #    })
  #   headers = {
  #   'Content-Type': 'application/json',
  #   'Cookie': 'PHPSESSID=6b8d40e13338ebdda12d3da572707bba'
  #   }

#     response = requests.request("POST", url, headers=headers, data=payload)
#   return render(request,'smsdone.html')  
#def sendemail(request):
#  camp=request.GET.get('coupen_id')
#  return render(request,'sendemail.html', {'camp_id': camp})

    
#@csrf_exempt 

#def emaildone(request):
  
# excel_file = request.FILES["file"]
# cam_id=request.GET.get('cam_id')
 #url = "https://api4coupons.com/v3/send/email"

# wb = openpyxl.load_workbook(excel_file)
# worksheet = wb["Sheet1"]
# for row in worksheet.iter_rows():
#   for cell in row:
 #    payload = json.dumps({
 #    "client_id": "6384889747946715134741991478448",
 #    "client_secret": "Pnhughk8ZhTJGxQkyhtc95TUVgPMtuE",
 #    "campaign": cam_id,
 #    "email": cell.value
 #    })
   #  headers = {
   #  'Content-Type': 'application/json',
  #   'Cookie': 'PHPSESSID=6b8d40e13338ebdda12d3da572707bba'
  #   }

 #    response = requests.request("POST", url, headers=headers, data=payload)
 #  return render(request,'emaildone.html')  

