from django.shortcuts import render
from django.urls import reverse_lazy

from django.conf import settings
import requests

# Create your views here.


def indexView(request):
    if request.method == "GET":

        return render(request, 'index.html')

    else:

        receiver = request.POST.get("number", None)
        msg = request.POST.get("message", None)

        print(receiver, "---------------->", msg)

        status = sendGetRequest(settings.SMS_URL, settings.SMS_API_KEY,
                                settings.SMS_SECRET_KEY, "stage", receiver, "girishf15", msg)

        print(status)

        if status:
            return render(request, 'success.html')
        else:
            return render(request, 'index.html')


def sendGetRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
    req_params = {
        'apikey': apiKey,
        'secret': secretKey,
        'usetype': useType,
        'phone': phoneNo,
        'message': textMessage,
        'senderid': senderId
    }
    return requests.get(reqUrl, req_params)
