from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.http import request
import logging
import urlparse

@csrf_exempt
def login(request):
    if request.method == 'POST':
        logging.warning('POST: get post request')
        url = request.POST['url']
        parsed = urlparse.urlparse(url)
        values = parsed.fragment
        tokens = [x.split('=') for x in values.split('&')]
        print(tokens[0][1])
    elif request.method == 'GET':
        logging.warning('Why the fuck is it get?')
        logging.warning(request.GET.get('token_type', 'None?!'))
        url = 'http://foo.appspot.com/abc?def=ghi'
        
        # print(request)        

    return render(request, 'login.html')
