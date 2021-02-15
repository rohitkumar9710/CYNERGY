from django.shortcuts import render
from django.http import HttpResponse
from customer.models import Contact
from django.utils import timezone
# Create your views here.
def home(request):
    return render(request, 'cynergy/signup.html')

def about(request):
    return render(request, 'cynergy/about_us.html')    

def contact(request):
    return render(request, 'cynergy/contact_us.html')  

def contact_status(request):
    name2 = request.POST.get('name1')
    email2 = request.POST.get('email1')
    subject2 = request.POST.get('subject1')
    comment2 = request.POST.get('comment1')
    comment = Contact(name = name2, email = email2, subject = subject2, comment = comment2,date = timezone.now())
    comment.save()
    return HttpResponse("<script>window.location = '/'</script>")
