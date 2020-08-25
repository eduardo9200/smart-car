from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
'''def home(request):
    return HttpResponse('Hello world!')
'''

def home(request):
    ip = '192.169.15.12'
    print(request.post.ipNumber)
    return render(request, 'dashboard/home.html', {'ip' : ip})