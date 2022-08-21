from django.shortcuts import render
from .models import User
from django.http import JsonResponse

# Create your views here.
def home(request):
    return render(request,'home.html')

def getUsers(request):
    querySet = User.objects.all()
    return JsonResponse({'users':list(querySet.values())})