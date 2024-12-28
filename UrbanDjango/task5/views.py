from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister

users = ['pavel', 'ivan', 'john']
info = {}


def sign_up_by_html(request):
    if request.method == 'POST':
        register_user = False
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))
        if username in users:
            info['error'] = 'Пользователь уже существует'
        else:
            if repeat_password == password:
                if age >= 18:
                    register_user = True
                else:
                    info['error'] = 'Вы должны быть старше 18'
            else:
                info['error'] = 'Пароли не совпадают'
        if register_user:
            out_message = f'Приветствуем, {username}!'
            print(out_message)
        else:
            out_message = info['error']
        return HttpResponse(out_message)
    return render(request, 'registration_page.html', info)


def sign_up_by_django(request):
    if request.method == 'POST':
        register_user = False
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = int(form.cleaned_data['age'])
            if username in users:
                info['error'] = 'Пользователь уже существует'
            else:
                if repeat_password == password:
                    if age >= 18:
                        register_user = True
                    else:
                        info['error'] = 'Вы должны быть старше 18'
                else:
                    info['error'] = 'Пароли не совпадают'
            if register_user:
                out_message = f'Приветствуем, {username}!'
                print(out_message)
            else:
                out_message = info['error']
        return HttpResponse(out_message)

    else:
        form = UserRegister()
    info['form'] = form
    return render(request, 'registration_page.html', info)
