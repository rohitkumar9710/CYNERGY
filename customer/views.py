from django.shortcuts import render
from django.http import HttpResponse
from customer.models import Custinfo
from django.utils import timezone
# Create your views here.


def redirect(request):
    return render(request,'customer/redirect.html')

def otp(request):
    name = request.POST.get('user_name')
    email = request.POST.get('e_mail')
    password = request.POST.get('password')
    phone = request.POST.get('phone_no')
    address = request.POST.get('address')
    city = request.POST.get('city')
    state = request.POST.get('state')
    global A
    A = [name,email,password,phone,address,city,state]
    
    B = list(Custinfo.objects.filter(email = email))
    if len(B)>0:
        return HttpResponse("you allready have a account")
    else:  
        return render(request, 'customer/otp.html')

def status(request):
    otp1 = request.POST.get('otp')
    if otp1 == "1234":
        person = Custinfo(cust_name=A[0],email = A[1],phone_no=A[3],password = A[2],sign_up_date = timezone.now(),city=A[5],state=A[6],addres = A[4])
        person.save()
        return render(request, 'customer/succes.html')
    else:
        return render(request, 'customer/failed.html')


def login(request):
    return render(request, 'customer/login.html')    

def profile_customer(request):
    email1 = request.POST.get('email')
    password1 = request.POST.get('passwd')
    A = list(Custinfo.objects.filter(email = email1))
    if len(A) >0:
        B = Custinfo.objects.get(email = email1)
        if password1 == B.password:
            return render(request, 'customer/customer-service-list.html')
        else:
            
            return HttpResponse("<script>window.location = '/customer/login'</script>")
    else:
        return HttpResponse("no accout with this email id , please check your email or creat one ")        

    
def about(request):

    return render(request, 'customer/about_us.html')
