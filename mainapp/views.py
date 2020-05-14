from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.urls import reverse
from django.shortcuts import render
from django.http import JsonResponse
from django.template.context_processors import csrf
from mainapp.models import Game, Genre, GameComment
from django.template.loader import render_to_string
from user.models import User
from django.contrib.auth import authenticate, login, logout
from user.forms import MyUserCreationForm, MyUserChangeForm


def index(request, ):
    games = Game.objects.all()
    top = Game.objects.all().order_by('rating')
    genre = Genre.objects.all()
    context = {
        'games': games,
        'top': top,
        'genre': genre,
    }
    return render(request, 'mainapp/index.html', context)


def android(request):
    games = Game.objects.filter(android=True)
    print(games)
    top = Game.objects.filter(android=True).order_by('rating')
    genre = Genre.objects.all()
    context = {
        'games': games,
        'top': top,
        'genre': genre,
    }
    return render(request, 'mainapp/android.html', context)


def ios(request):
    games = Game.objects.filter(ios=True)
    top = Game.objects.filter(ios=True).order_by('rating')
    genre = Genre.objects.all()
    context = {
        'games': games,
        'top': top,
        'genre': genre,
    }
    return render(request, 'mainapp/ios.html', context)


def windows(request):
    games = Game.objects.filter(windows=True)
    top = Game.objects.filter(windows=True).order_by('rating')
    genre = Genre.objects.all()
    context = {
        'games': games,
        'top': top,
        'genre': genre,
    }
    return render(request, 'mainapp/windows.html', context)


def psp(request):
    games = Game.objects.filter(psp=True)
    top = Game.objects.filter(psp=True).order_by('rating')
    genre = Genre.objects.all()
    context = {
        'games': games,
        'top': top,
        'genre': genre,
    }
    return render(request, 'mainapp/psp.html', context)


def xbox(request):
    games = Game.objects.filter(xbox=True)
    top = Game.objects.filter(xbox=True).order_by('rating')
    genre = Genre.objects.all()
    context = {
        'games': games,
        'top': top,
        'genre': genre,
    }
    return render(request, 'mainapp/x-box.html', context)


def game(request, name=None):
    if request.method == 'GET':
        if name:
            print(name)
            games = Game.objects.filter(name=name)
            comment = GameComment.objects.filter(game=name)

    context = {
        'comment': comment,
        'games': games,
    }

    return render(request, 'mainapp/game.html', context)


def ganre(request, gan):
    if request.method == 'GET':
        if gan:
            print(gan)
            games = Game.objects.filter(genre=gan)
            top = Game.objects.filter(genre=gan).order_by('rating')
            genre = Genre.objects.all()
            ganr = Genre.objects.filter(name=gan)

    context = {
        'games': games,
        'top': top,
        'genre': genre,
        'ganr': ganr,
    }

    return render(request, 'mainapp/ganre.html', context)


def user_login(request):
    if request.is_ajax():
        print('AJAX login', request.META['HTTP_REFERER'])
        context = {
            'login': reverse('auth:login'),
        }
        return JsonResponse(context)

    if request.POST:
        if 'email' in request.POST and request.POST['email']:
            email = request.POST['email']
            password = request.POST['psw']
            user = authenticate(email=email, password=password)
            if user is not None:
                print('пользователь найден: ', user)
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
        elif 'fname' in request.POST and request.POST['fname']:
            first_name = request.POST['fname']
            last_name = request.POST['lname']
            request.session['fname'] = first_name
            request.session['lname'] = last_name
            return HttpResponseRedirect(reverse('register'))

    return render(request, 'mainapp/login.html')


def user_logout(request):
    logout(request)     # стираем токен аутентификации из cookie
    return HttpResponseRedirect(reverse('index'))


def user_register(request):
    register_form = MyUserCreationForm()
    fname = request.session.get('fname', 'Нет имени')
    lname = request.session.get('lname', 'Нет фамилии')
    if request.method == "POST":
        register_form = MyUserCreationForm(request.POST, request.FILES)
        if register_form.is_valid():
            register_form.save()
            email = request.POST['email']
            password = request.POST['password1']
            user = authenticate(email=email, password=password)
            if user is not None:
                print('пользователь найден: ', user)
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        register_form = MyUserCreationForm()
    context = {
        'register_form': register_form,
        'fname': fname,
        'lname': lname,
    }

    return render(request, 'mainapp/register.html', context)


