# ---------------------------------- [edit] ---------------------------------- #
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import UserForm
from .models import Users


def signup(request):
    """
    계정생성
    """
    if request.method == "POST":

        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)

            return render(request, 'accounts/login.html')
    else:
        form = UserForm()
    return render(request, 'accounts/signup.html', {'form': form})
# ---------------------------------------------------------------------------- #
