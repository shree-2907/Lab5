from django.shortcuts import render
from django.http import JsonResponse

def show(request):
    return JsonResponse({"Message": "Hello World!"})
