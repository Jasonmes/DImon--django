from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    """
    渲染模板并且返回
    :param request:
    :return:
    """
    context = {'city': '深圳'}
    return render(request, 'users/index.html', context=context)