from django.shortcuts import render
from django.http import HttpResponse


def qr_code(request):
    return render(request, 'qr_code/index.html')
