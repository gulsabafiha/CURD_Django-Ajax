from django.http.response import JsonResponse
from django.shortcuts import render
from . forms import StudentReg
from . models import User
# from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    form= StudentReg()
    stud= User.objects.all()

    return render(request,'enroll/home.html',{'form':form,'stud':stud})


# @csrf_exempt
def save_data(request):
    if request.method == 'POST':
        form= StudentReg(request.POST)
        if form.is_valid():
            name= request.POST['name']
            email= request.POST['email']
            password= request.POST['password']
            user= User(name=name,email=email,password=password)
            user.save()
            return JsonResponse({'status':'Save'})
        else:
            return JsonResponse({'status':0})