from django.http import request
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView, View
from .serializers import TestPostListSerializer
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

def index(request):
    return render(request, 'test.html')


def index2(request):
    return render(request, '')

# @csrf_exempt #function base
# @method_decorator(login_required, name="dispatch")
# @method_decorator(csrf_exempt, name='dispatch') #class function
# class Test(View):
#     '''
#     #TODO post is error ...
#     => 	<title>Page not found at /accounts/login/</title>
#     '''
#     def post(self, request, **kwargs):
#         res = request.post('http://127.0.0.1:8000/test/3/', json=kwargs)
#         params = TestPostListSerializer(data=request.data)
#         return render(params, 'test3.html', {
#             'params' : params
#         })
    # def get(self, request, **kwargs):
    #     params = {
    #         'a' : 'ㅁㄴ야ㅓㅗ먀너ㅕ와',
    #         'b' : 'ㅁ쟈ㅑ져덩ㅁ',
    #         'c' : '먀너먀ㅓ누아ㅓ',
            
    #     }
    #     return render(request, 'test3.html', {
    #         'params' : params
    #     })


# @method_decorator(login_required, name="dispatch")
@method_decorator(csrf_exempt, name='dispatch') #class function
class Test(APIView):
    def post(self, request):
        serializer = TestPostListSerializer(data=request.data)
        if serializer.is_valid():
            return render(request, '../templates/test3.html', {"params" : request.data})