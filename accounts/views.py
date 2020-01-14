from django.shortcuts import render, redirect
from accounts.forms import SignUpForm
from django.contrib.auth import login as auth_login
from rest_framework import generics

from accounts.models import Account
from accounts.serializers import AccountSerializers


def index(request):
    return render(request, 'accounts/base.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('accounts:index')

    else:
        form = SignUpForm()

    return render(request, 'accounts/signup.html', {'form': form})


class AccountListAPI(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = AccountSerializers

    def get_queryset(self):
        return Account.objects.all()


