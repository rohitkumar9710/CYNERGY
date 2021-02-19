from django.shortcuts import render
from django.http import HttpResponse
from customer.models import Custinfo,Custom_order,Customer_random
from customer.models import Contact,Feedback
from serviceman.models import Serviceinfo
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
        return HttpResponse('<script>window.location = "/customer/login";window.alert("You already have a account , please login from that");</script>')
    else:  
        return render(request, 'customer/otp.html')

def status(request):
    otp1 = request.POST.get('otp')
    if otp1 == "1234":
        person = Custinfo(cust_name=A[0],email = A[1],phone_no=A[3],password = A[2],sign_up_date = timezone.now(),city=A[5],state=A[6],addres = A[4])
        person.save()
        return render(request, 'customer/succes.html')
    else:
        return HttpResponse('<script>window.location = "/customer/login";window.alert("You entered a wrong otp");</script>')


def login(request):
    return render(request, 'customer/login.html')    
  
def profile_customer(request):
    email1 = request.POST.get('email')
    password1 = request.POST.get('passwd')
    global K 
    K = [email1,password1]
    A = list(Custinfo.objects.filter(email = email1))
    if len(A) >0:
        B = Custinfo.objects.get(email = email1)
        if password1 == B.password:
            B.loginstate = "yes"
            B.save()
            return HttpResponse("<script>window.location = '/customer/login/loggedin/services'</script>")
        else:
            
            return HttpResponse('<script>window.location = "/customer/login";window.alert("Your Password is wrong ");</script>')
    else:
        return HttpResponse('<script>window.location = "/";window.alert("No account found of this email id . Kindly create one or check your email id. ");</script>')        

def services(request):
    B = Custinfo.objects.get(email = K[0])
    k = B.loginstate
    not1 = Custom_order.objects.filter(customer_email=K[0],accept_status="None")
    not2 = Custom_order.objects.filter(customer_email=K[0],accept_status="Accepted")  
    A = len(not1)+len(not2)    
    if k == "yes":
        return render(request, 'customer/customer-service-list.html',{"len":A})
    else:
        return HttpResponse("<script>window.location = '/customer/login'</script>")    

def about(request):
    B = Custinfo.objects.get(email = K[0])
    k = B.loginstate
    if k == "yes":
        not1 = Custom_order.objects.filter(customer_email=K[0],accept_status="None")
        not2 = Custom_order.objects.filter(customer_email=K[0],accept_status="Accepted")  
        A = len(not1)+len(not2)    
        return render(request, 'customer/about_us.html',{"len":A})
    else:
        return HttpResponse("<script>window.location = '/customer/login'</script>")   

def profile(request):
    B = Custinfo.objects.get(email = K[0])
    k = B.loginstate
    not1 = Custom_order.objects.filter(customer_email=K[0],accept_status="None")
    not2 = Custom_order.objects.filter(customer_email=K[0],accept_status="Accepted")  
    A = len(not1)+len(not2)    
    data = {"name":B.cust_name,"gender":B.gender,"date":B.sign_up_date,"email":B.email,"phoneno":B.phone_no,"address":B.addres,"city":B.city,"state":B.state,"password":B.password,"len":A}
    if k == "yes":
        return render(request,'customer/cust_profile.html',data)
    else:
        return HttpResponse("<script>window.location = '/customer/login'</script>")

def profileupdate(request):
    name2 = request.POST.get('user_name1')
    email2 = request.POST.get('email1')
    password2 = request.POST.get('password1')
    phone2 = request.POST.get('phone_no1')
    address2 = request.POST.get('address1')
    city2 = request.POST.get('city1')
    state2 = request.POST.get('state1')
    gender2 = request.POST.get('gender1')
    B = Custinfo.objects.get(email = K[0])
    B.cust_name = name2
    B.email = email2
    B.phone_no = phone2
    B.password = password2
    B.addres = address2
    B.city = city2
    B.state = state2
    B.gender = gender2
    B.save()
    return HttpResponse("<script>window.location = '/customer/login/loggedin/profile'</script>")

def logout(request):
    B = Custinfo.objects.get(email = K[0])
    
    if B.loginstate == "yes":
        B.loginstate = "no"
        B.save()
        print("logged out")
        return HttpResponse("<script>window.location = '/'</script>")
    else:
        return HttpResponse("<script>window.location = '/customer/login'</script>")

def contact(request):
    B = Custinfo.objects.get(email = K[0])
    k = B.loginstate
    not1 = Custom_order.objects.filter(customer_email=K[0],accept_status="None")
    not2 = Custom_order.objects.filter(customer_email=K[0],accept_status="Accepted")  
    A = len(not1)+len(not2)    
    if k == "yes":
        return render(request, 'customer/contact_us.html',{"len":A})
    else:
        return HttpResponse("<script>window.location = '/customer/login'</script>")

def contact_submit(request):
    name2 = request.POST.get('name1')
    email2 = request.POST.get('email1')
    subject2 = request.POST.get('subject1')
    comment2 = request.POST.get('comment1')
    comment = Contact(name = name2, email = email2, subject = subject2, comment = comment2,date = timezone.now())
    comment.save()
    return HttpResponse("<script>window.location = '/customer/login/loggedin/services'</script>")



def search(request):
    B = Custinfo.objects.get(email = K[0])
    k = B.loginstate
    if k == "yes":

        B = Custinfo.objects.get(email = K[0])
        carpenter2 = request.POST.get('carpenter')
        electrecian2 = request.POST.get('electrecian')
        plumber2= request.POST.get('plumber')
        technecian2 = request.POST.get('technecian')
        cleaning2 = request.POST.get('cleaning')
        kitchen2 = request.POST.get('kitchen')
        button12 = request.POST.get('button1')
        button22 = request.POST.get('button2')
        lst = [cleaning2,technecian2,plumber2,electrecian2,carpenter2,kitchen2]
        services = ['cleaning','technecian','plumber','electrecian','carpenter','kitchen']
        not1 = Custom_order.objects.filter(customer_email=K[0],accept_status="None")
        not2 = Custom_order.objects.filter(customer_email=K[0],accept_status="Accepted")  
        A = len(not1)+len(not2)    
        if button12 == "on":
            print(lst)
            l = lst.index('on')
            print(l,services[l])
            service = services[l]
            if service == 'cleaning':
                service_data = Serviceinfo.objects.filter(cleaning='on')
                order_data = Custom_order.objects.filter(customer_email=K[0],work='cleaning')
                list1= [i.serviceman_email for i in order_data]
                list2 = [i.email for i in service_data]
                list3 = list(set(list2)-set(list1))
                list4 = [ Serviceinfo.objects.get(email=i) for i in list3]
                print(service_data,list1,list2,list3,list4)
                return render(request,'customer/custom_search.html',{"data":list4,'job':service,"len":A})
            elif service == 'technecian':
                service_data = Serviceinfo.objects.filter(technecian='on')
                order_data = Custom_order.objects.filter(customer_email=K[0],work='technecian')
                list1= [i.serviceman_email for i in order_data]
                list2 = [i.email for i in service_data]
                list3 = list(set(list2)-set(list1))
                list4 = [ Serviceinfo.objects.get(email=i) for i in list3]
                print(service_data)    
                return render(request,'customer/custom_search.html',{"data":list4,'job':service,"len":A})
            elif service == 'plumber':
                service_data = Serviceinfo.objects.filter(plumber='on')
                order_data = Custom_order.objects.filter(customer_email=K[0],work='plumber')
                list1= [i.serviceman_email for i in order_data]
                list2 = [i.email for i in service_data]
                list3 = list(set(list2)-set(list1))
                list4 = [ Serviceinfo.objects.get(email=i) for i in list3]
                print(service_data) 
                return render(request,'customer/custom_search.html',{"data":list4,'job':service,"len":A})
            elif service == 'electrecian':
                service_data = Serviceinfo.objects.filter(electrecian='on')
                order_data = Custom_order.objects.filter(customer_email=K[0],work='electrecian')
                list1= [i.serviceman_email for i in order_data]
                list2 = [i.email for i in service_data]
                list3 = list(set(list2)-set(list1))
                list4 = [ Serviceinfo.objects.get(email=i) for i in list3]
                return render(request,'customer/custom_search.html',{"data":list4,'job':service,"len":A})
            elif service == 'carpenter':
                service_data = Serviceinfo.objects.filter(carpenter='on')
                order_data = Custom_order.objects.filter(customer_email=K[0],work='carpenter')
                list1= [i.serviceman_email for i in order_data]
                list2 = [i.email for i in service_data]
                list3 = list(set(list2)-set(list1))
                list4 = [ Serviceinfo.objects.get(email=i) for i in list3]
                return render(request,'customer/custom_search.html',{"data":list4,'job':service,"len":A})
            elif service == 'kitchen':
                service_data = Serviceinfo.objects.filter(kitchen='on')
                order_data = Custom_order.objects.filter(customer_email=K[0],work='kitchen')
                list1= [i.serviceman_email for i in order_data]
                list2 = [i.email for i in service_data]
                list3 = list(set(list2)-set(list1))
                list4 = [ Serviceinfo.objects.get(email=i) for i in list3] 
                return render(request,'customer/custom_search.html',{"data":list4,'job':service,"len":A})
            else:
                return HttpResponse("Entered Wrong information")
            
        elif button22 == "on":
            l = lst.index('on')
            print(l,services[l])
            service = services[l]
            return render(request,'customer/random _search.html',{"work":service,"len":A}) 
    else:
        return HttpResponse("<script>window.location = '/customer/login'</script>")

def random_data(request):
    work2 = request.POST.get('job')
    deadline_date2 = request.POST.get('deadline_date')
    address2 = request.POST.get('address')
    description2 = request.POST.get('description')
    A = [work2,deadline_date2,address2,description2]
    print(A)
    data = Customer_random(customer_email = K[0],request_date= timezone.now(),deadline_date=deadline_date2,work_address=address2,work_description=description2)
    data.save()
    return HttpResponse("<script>window.location = '/customer/login/loggedin/services'</script>")

def search_request(request):
    B = Custinfo.objects.get(email = K[0])
    a = request.POST.get('request')
    b= request.POST.get('deadline_date')
    work2 = request.POST.get('work1')
    worker = Serviceinfo.objects.get(email = a)
    work5 = Custom_order(customer_email=K[0],customer_name=B.cust_name,customer_phone=B.phone_no,serviceman_email=a,serviceman_name=worker.name,serviceman_phone=worker.phone_no,request_date=timezone.now(),work = work2,deadline_date=b)
    work5.save()
    
    return HttpResponse('<script>window.location = "/customer/login/loggedin/services";window.alert("Your request sent succesfully");</script>')






#*********************************notifications*********************************************************************************************
def notification(request):
    B = Custinfo.objects.get(email = K[0])
    
    if B.loginstate == "yes":
        not1 = Custom_order.objects.filter(customer_email=K[0],accept_status="None")
        not2 = Custom_order.objects.filter(customer_email=K[0],accept_status="Accepted")  
        A = len(not1)+len(not2)      
        data = {"noti1":not1.reverse(),"noti2":not2.reverse(),"len":A}
        
        return render(request,'customer/cust-notif.html',data)
    else:
        return HttpResponse("<script>window.location = '/customer/login'</script>")

def cencle_button(request):
    a = request.POST.get('email1')
    b = request.POST.get('work1')
    c = request.POST.get('date1')
    data = Custom_order.objects.get(customer_email=K[0],serviceman_email=a,work=b,request_date=c)
    data.delete()
    return HttpResponse("<script>window.location = '/customer/login/loggedin/services';window.alert('Your request CANCLED succesfully');</script>")


def feedback(request):
    a = request.POST.get('s_mail')
    b = request.POST.get('work1')
    c = request.POST.get('r_date')
    d = request.POST.get('complete_date')
    e = request.POST.get('rating')
    f = request.POST.get('feedback-text')
    if a  == "None" or b == "None" or c == "None":
         return HttpResponse("<script>window.location = '/customer/login/loggedin/notification';window.alert('Wrong Information');</script>")
    else:
        order = Custom_order.objects.get(customer_email=K[0],serviceman_email=a,work=b,request_date=c)
        order.delete()
        feedback = Feedback(customer_email=K[0],serviceman_email=a,feedback=f,work=b,request_date = c,feedback_date=timezone.now(),rating = e,w_done_date=d)
        feedback.save()
        print(a,b,c,d,e,f)
        return HttpResponse("<script>window.location = '/customer/login/loggedin/notification';window.alert('Thank you for your feedback');</script>")

#**************************************remaining******************************************************************************************************
def history(request):
    B = Custinfo.objects.get(email = K[0])
    not1 = Custom_order.objects.filter(customer_email=K[0],accept_status="None")
    not2 = Custom_order.objects.filter(customer_email=K[0],accept_status="Accepted")  
    A = len(not1)+len(not2)    
    if B.loginstate == "yes":
        
        return render(request,'customer/customer_history_page.html',{"len":A})
    else:
        return HttpResponse("<script>window.location = '/customer/login'</script>")

def donate(request):
    B = Custinfo.objects.get(email = K[0])
    not1 = Custom_order.objects.filter(customer_email=K[0],accept_status="None")
    not2 = Custom_order.objects.filter(customer_email=K[0],accept_status="Accepted")  
    A = len(not1)+len(not2)    
    if B.loginstate == "yes":
        
        return render(request,'customer/donate.html',{"len":A})
    else:
        return HttpResponse("<script>window.location = '/customer/login'</script>")