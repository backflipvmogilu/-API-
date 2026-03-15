from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello, world !")
def about(request):
    return HttpResponse("Здесь будет информация о нас")
def contact(request):
    return HttpResponse("Наши контактные данные")
def users(request):
    return HttpResponse("На данной стран"
                        "ице будет профиль пользователя")