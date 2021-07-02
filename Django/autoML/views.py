from .forms import MLUserCreationForm, MLUserChangeForm, AccountAuthenticationForm
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate, logout, login
from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from .models import Dataset, Project


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
    context = {'type': _('Страница регистрации'),
               "button": "Зарегистрироваться"}
    if request.POST:
        form = MLUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_pass = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_pass)
            login(request, account)
            messages.success(request, _('Вы зарегистрировались как {} ').format(request.user.email))
            return redirect('home')
        else:
            messages.error(request, _('Исправьте ошибки ниже'))
            context['form'] = form
    else:
        form = MLUserCreationForm()
        context['form'] = form
    return render(request, "automl/login.html", context)


def logout_view(request):
    logout(request)
    messages.success(request, _("Logged Out"))
    return redirect("home")


def login_view(request):
    """
      Renders Login
    """
    context = {'type': _('Страница Входа'),
               "button": _('Вход')}
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
            messages.success(request, _('Успешный вход!'))
            return redirect("lk")
        else:
            messages.error(_('Исправьте ошибки ниже'))
    else:
        form = AccountAuthenticationForm()
        context['form'] = form
    return render(request, "automl/login.html", context)


# Пока набросок - еще не готово(в работе)...
@login_required
def lk_view(request):
    if request.user.is_authenticated:
        context = {}
        proj = Project.objects.order_by('creation_datetime')[:3]
        if proj:
            context['projs'] = proj
        return render(request, "automl/lk.html", context)
    else:
        return render('%s?next=%s' % (settings.LOGIN_URL, request.path))


# Пока набросок - еще не готово(в работе)...
def create_data(request):
    if request.POST:
        name = request.POST.get('name')
        description = request.POST.get('description')
        status = ''
        dataset = Dataset(name=name, description=description, status=status)
        dataset.create_dataset()
        messages.success('Dataset good')

        user_id = request.user.id
        # dataset_new = Dataset.objects.get(user_id=user_id)
        dataset_new_2 = Dataset.objects.filter(user_id=user_id)
        context = {'name': name, 'description': description, 'data': dataset_new_2.filter()[:3]}
    return render(request, "automl/dataset_create.html")





