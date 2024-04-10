from django.shortcuts import render
from django.http import HttpResponse 
from .forms import userForm
from django.shortcuts import redirect
def home(request):
    return render(request,'home.html')

def course(request):
    return render(request,'course.html')

def result(request):
    return render(request,'result.html')

def userregister(request):
    form = userForm()
    if request.method == 'POST':
        form = userForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course')
    context = {'form':form}
    return render(request,'userregister.html',context)