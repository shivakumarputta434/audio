from django.shortcuts import HttpResponse,render

def home(request):
    #return HttpResponse("success")
    return render(request,'home.html')


def register(request):
    #return HttpResponse("success")
    name="shivakumar"
    num=1
    return render(request,'register.html',{'name':name,'num':num})

def login(request):
    #return HttpResponse("success")
    return render(request,'login.html')