from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from .forms import UserCreateForm
from django.core.mail import send_mail


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('warehouse_m:index'))
            else:
                return HttpResponse('ACCOUNT NOT ACTIVE!')

    return render(request, 'login_whm/user_login.html', {})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login_whm:user_login'))


def sign_up(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            sender = form.cleaned_data['email']
            message = f"Username: {form.cleaned_data['username']} \n" \
                      f"Password: {form.cleaned_data['password1']} \n" \
                      f"First Name: {form.cleaned_data['first_name']} \n" \
                      f"Last Name: {form.cleaned_data['last_name']} \n" \
                      f"Email: {form.cleaned_data['email']}"
            send_mail("Waiting for approval!", message, sender, ['django.test.email2021@gmail.com'])
            return HttpResponseRedirect(reverse('login_whm:sign_up_success'))
    else:
        form = UserCreateForm()
    return render(request, 'login_whm/sign_up.html', {'form': form})


def sign_up_success(request):
    return render(request, 'login_whm/sign_up_success.html')

