from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json


def home(request):
    data = {'name': 'Dancan Chibole', 'age': 12}
    data = json.dumps(data)
    return HttpResponse(data, content_type='application/json')


@csrf_exempt
def api_git_msg(request):
    if request.method == 'POST':
        print("Data received from Webhook is: ", request.body)
        f = open('payload.txt', 'w+')
        f.write(str(json.loads(request.body)))
        f.close()
        # print(json.loads(request.body))
        return HttpResponse(request.body, content_type='application/json')




