import json
from django.shortcuts import render
from django.http import HttpResponse

from .models import UsRequest


def index(request):
    return render(request, 'main/index.html')


def save_request(request):
    req = request.GET
    fname = request.GET.get('fname')
    phone = request.GET.get('phone')
    msg = request.GET.get('msg')
    print(f'{req=}')
    # Передача данных через HttpResponse в json
    data = {"header": "Hello Django", "message": "Заявка успешно отправлена"}
    # Create a new record using the model's constructor.
    a_record = UsRequest(fname=fname, phone=phone, msg=msg)
    # Save the object into the database.
    a_record.save()
    return HttpResponse(json.dumps(data), content_type='application/json')
