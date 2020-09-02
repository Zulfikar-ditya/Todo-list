from django.shortcuts import render
from .forms import RegisterFrom
from django.http import HttpResponseRedirect

def register(request):
    if request.user.is_authenticated:    
       return HttpResponseRedirect('../you_are_logged_in/')
    else:
        if request.method == 'POST':
            form = RegisterFrom(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('../login/')
        else:
            form = RegisterFrom()
        return render(request, 'registration/create_account.html', {'form': form})
