from .forms import MLUserCreationForm, MLUserChangeForm, AccountAuthenticationForm
from .models import MLUser
from django.contrib import messages
from django.contrib.auth import (
    authenticate,
    logout,
    login
)
from django.shortcuts import (
    render,
    get_object_or_404,
    redirect
)


# Create first request.
# def index(request):
#     # return render(request, template_name='autoML/index.html', context={'header':'Добрый день! Это главная страница.', 'title':'Главная'})
#     return render(request, 'automl/index.html',
#                   context={'header': 'Добрый день! Это главная страница!', 'title': 'Главная'})


# Новый код:
def home(request):
    """
      Home View Renders base.html
    """
    return render(request, "automl/home.html", {})


def registration_view(request):
    """
      Форма регистрации
    """
    context = {'type': 'Registration page',
               "button": "Зарегистрироваться"}
    if request.POST:
        form = MLUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_pass = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_pass)
            login(request, account)
            messages.success(request, "You have been Registered as {}".format(request.user.username))
            return redirect('home')
        else:
            messages.error(request, "Please Correct Below Errors")
            context['registration_form'] = form
    else:
        form = MLUserCreationForm()
        context['registration_form'] = form
    return render(request, "automl/login.html", context)


def logout_view(request):
    logout(request)
    messages.success(request, "Logged Out")
    return redirect("home")


def login_view(request):
    """
      Renders Login
    """
    context = {'type': 'Log In page',
               "button": "Log In"}
    user = request.user
    if user.is_authenticated:
        return redirect("home")
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user:
            login(request, user)
            messages.success(request, "Logged In")
            return redirect("home")
        else:
            messages.error("please Correct Below Errors")
    else:
        form = AccountAuthenticationForm()
    context['login_form'] = form
    return render(request, "automl/login.html", context)
