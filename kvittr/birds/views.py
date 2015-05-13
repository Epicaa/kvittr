from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render
from django.shortcuts import redirect

def bird_register(request):
    context = {}
    if request.method == "POST":
        bird = User()
        bird.first_name = request.POST.get('firstname')
        bird.last_name = request.POST.get('lastname')
        bird.email = request.POST.get('email')
        bird.birdname = request.POST.get('birdname')
        bird.set_password(request.POST.get('password'))
        bird.save()
        context['bird_saved_successfully'] = True
    return render(request, 'birds/register.html', context)

def bird_login(request):
    context = {}
    if request.method == 'POST':
        birdname = request.POST['birdname']
        password = request.POST['password']
        bird = authenticate(birdname=birdname, password=password)
        if bird is not None:
            login(request, bird)
            return redirect('frontpage')
        else:
            context['login_failed'] = True
    return render(request, 'birds/login.html', context)

def bird_logout(request):
    logout(request)
    return redirect('frontpage')