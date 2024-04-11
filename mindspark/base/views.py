from django.shortcuts import render
from django.http import HttpResponse 
from .forms import userForm
from .models import user
from django.shortcuts import redirect
from django.forms import ModelForm

def home(request):
    return render(request,'home.html')

def course(request):
    return render(request,'course.html')

def result(request):
    return render(request,'result.html')

def quiz(request):
    return render(request,'quiz.html')

#  <!-- name = models.CharField(max_length=100)
#     usn = models.CharField(max_length=10)
#     dob = models.DateField
#     gender = models.CharField(max_length=10)
#     highest_edu = models.CharField(max_length=100)
#     disability = models.CharField(max_length=10)
#     sem = models.IntegerField()
#     college = models.CharField(max_length=100)
#     username = models.CharField(max_length=100)
#     password = models.CharField(max_length=100)
#     email = models.EmailField(max_length=100)
#     phone = models.CharField(max_length=10)
#     enroll_date = models.DateTimeField(auto_now_add=True)
#   -->
def userregister(request):
    if request.method == 'POST':
        form = userForm(request.POST)  # Create form instance with POST data
        if form.is_valid():
            form.save()
            return redirect('course')  # Redirect to your desired page
        else:
            context = {'form': form}
            print( form.errors )
            return HttpResponse('Invalid form')
    else:
        form = userForm()
        context = {'form': form}
    return render(request, 'userregister.html', context)
    
        
    # form = userForm(request.POST)
    
    # if request.method == 'POST':
    #     form = userForm()
    #     if form.is_valid():
    #         form.save()
    #         return redirect('course')
    #     else:
    #         return redirect('result')
    # context = {'form':form}
    # return render(request,'userregister.html',context)
    # #     name = request.POST.get('name')
    # #     usn = request.POST.get('usn')
    # #     dob = request.POST.get('dob')
    # #     gender = request.POST.get('gender')
    # #     highest_edu = request.POST.get('highestedu')
    # #     disability = request.POST.get('disability')
    # #     sem = request.POST.get('sem')
    # #     college = request.POST.get('college')
    # #     username = request.POST.get('username')
    # #     password = request.POST.get('password')
    # #     email = request.POST.get('email')
    # #     phone = request.POST.get('phone')
    # #     form = userForm(name = name, usn = usn, dob = dob,gender = gender,highest_edu = highest_edu,disability = disability,sem = sem,college = college,username = username,password = password,email = email,phone = phone)
    # #     form.save()
    
    #     # if form.is_valid():
    #     #     form.save()
    #     #     return redirect('course')
    #     # else:
    #     #     
   
    