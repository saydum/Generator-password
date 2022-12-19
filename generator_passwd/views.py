from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator_password/home.html')


def password(request):

    characters = list('abcdifghijklmnopqrstuvwxyz');
    characters.extend(list('ABCDIFGHIJKLMNOPQRSTUVWXYZ'))
    characters.extend(list('0123456789'))
    characters.extend(list('!@#$%^&*()'))

    length = int(request.GET.get('length'))

    thepassword = ''

    for x in range(length):
        thepassword += random.choice(characters)


    return render(request, 'generator_password/home.html', {'password':thepassword})
