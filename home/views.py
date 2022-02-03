from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import logout,login,authenticate
# password harry###@@@111
# Create your views here.

def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request , 'index.html')
    
def loginUser(request):
    if request.method=='POST':
        #check the user has entered correct credentials
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
           login(request, user)
           return redirect('/')    
    
        else:
            return render(request , 'login.html')
    
    return render(request, 'login.html')
    
def logoutUser(request):
    logout(request)
    # return HttpResponse('Hello guys, this is logoutpage')
    return redirect("/login") 
    