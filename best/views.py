from unicodedata import name
from django.shortcuts import render, HttpResponseRedirect
import idna
import pkg_resources
from requests import delete
from .forms import StudentRegistration
from .models import User as uss

# Create your views here.

def Suser(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            fm = StudentRegistration()  
    else:
        fm = StudentRegistration()  
    stud = uss.objects.all()  
    return render(request, 'enroll/add.html', {'form': fm, 'stu':stud})


def DeleteUser(request, id):
    if request.method== 'POST':
        di = uss.objects.get(pk=id)
        di.delete()
        
        return HttpResponseRedirect('/')
    
    
    
def UpdateUser(request, id):
    if request.method== 'POST':
        upd = uss.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=upd)
        if fm.is_valid():
            fm.save()
    else:
        upd = uss.objects.get(pk=id)
        fm = StudentRegistration(instance=upd)
            
    return render(request, 'enroll/update.html', {'form':fm})    