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
    return render(request, '../templates/test.html')


def index2(request):
    
    return render(request, '../templates/test2.html')


def index3(request):
    return render(request, '../templates/crawl.html')

# @csrf_exempt #FBV
# @method_decorator(login_required, name="dispatch")
@method_decorator(csrf_exempt, name='dispatch') #CBV
class Test(APIView):
    def post(self, request):
        serializer = TestPostListSerializer(data=request.data)
        if serializer.is_valid():
            return render(request, '../templates/test3.html', {"params" : request.data})