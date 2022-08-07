from django.shortcuts import render

# Create your views here.


def reg(request):
    return render(request,'register.html')



def log(request):
    return render(request,'login.html')


    
def sur(request):
    return render(request,'survey.html')