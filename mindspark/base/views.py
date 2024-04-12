from django.shortcuts import render
from django.http import HttpResponse 
from .forms import userForm
from .models import user
from django.shortcuts import redirect
from django.forms import ModelForm
from django.contrib.messages import constants as messages

def home(request):
    return render(request,'home.html')

def course(request):
    enable_camera = True  
    return render(request,'course.html',{'enable_camera': enable_camera})

def result(request):
    return render(request,'result.html')

def quiz(request):
    return render(request,'quiz.html')

def userregister(request):
    if request.method == 'POST':
        form = userForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('course')  
        else:
            form = userForm()
            context = {'form': form}
            print(form.errors)
            return HttpResponse("Invalid Form")
            # Return the form with errors to the user
        return render(request, 'userregister.html', {'form': form})
        
    else:
        form = userForm()
        context = {'form': form}
    return render(request, 'userregister.html', context)

def profile(request):
    return render(request,'profile.html') 
        
def home(request):
    return render(request,'home.html')
   