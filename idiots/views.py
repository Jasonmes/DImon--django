from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(requrst):
    return HttpResponse("idiot")


# response = HttpResponse()
# response['Itcast'] = 'Python'


"""
试图用类方法来表示
"""
from django.views.generic import View

class RegiterView(View):
    """
    类视图
    处理注册
    """
    def get(self):
        """

        :return:
        """

    def psot(self):
        """

        :return:
        """


def indeXX(request):
    """
    request.META会自动解析请求头，（键值对格式）
    键会被修改
    Content—Type 会改成
    :param request:
    :return:
    """