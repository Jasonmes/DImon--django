from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


"""
中间件的定义方法
"""
def index(request):
    """
    :param request:
    :return:
    """
    print("试图处理中")
    return HttpResponse("OK")