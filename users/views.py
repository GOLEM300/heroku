from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def logout_view(name):
    """end work"""
    logout(name)
    return HttpResponseRedirect(reverse('learning_logs:index'))

def register(name):
    """reg new user"""
    if name.method != 'POST':
        #display blank reg form
        form = UserCreationForm()
    else:
        #procesing fill form
        form = UserCreationForm(data=name.POST)

        if form.is_valid():
            new_user = form.save()
            # exit and redirect to home page
            # authenticated_user = authenticate(username=new_user.username, password=name.POST.get('password', False))
            login(name, new_user, backend='django.contrib.auth.backends.ModelBackend')
            return HttpResponseRedirect(reverse('learning_logs:index'))
    
    context = {'form': form}
    return render(name, 'users/register.html', context)