from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm


def get_name(request):
    if request.method == 'POST':
        form = NameForm
        if form.is_valid():
            return HttpResponseRedirect('/')

    else:
        form = NameForm
    return render(request, 'signup.html', {'form' : form})

