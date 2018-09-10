#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Jason Mess
from django.utils.decorators import classonlymethod, method_decorator
from django.views.generic import View
from django.http import HttpResponse


def my_decorater(func):
    def wrapper(request, *args, **kwargs):
        print("自定义装饰器被调用了")
        print("请求路径%s" % request.path)
        return func(request, *args, **kwargs)

    return wrapper


@classonlymethod
def as_view(cls, **initkwargs):
    """
    Main entry point for a request-response process.
    """


    def view(request, *args, **kwargs):
        self = cls(**initkwargs)
        if hasattr(self, 'get') and not hasattr(self, 'head'):
            self.head = self.get
        self.request = request
        self.args = args
        self.kwargs = kwargs
        # 调用dispatch方法，按照不同请求方式调用不同请求方法
        return self.dispatch(request, *args, **kwargs)

    # 返回真正的函数视图
    return view


def dispatch(self, request, *args, **kwargs):
    # Try to dispatch to the right method; if a method doesn't exist,
    # defer to the error handler. Also defer to the error handler if the
    # request method isn't on the approved list.
    if request.method.lower() in self.http_method_names:
        handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
    else:
        handler = self.http_method_not_allowed
    return handler(request, *args, **kwargs)
"""
在类视图中装饰
函数装饰器，在调用视图函数之前做些事情：（权限认证）
"""

@method_decorator(my_decorater(), name='dispatch')  # dispatch是分发函数，装饰所有
class DemoView(View):

    @method_decorator(my_decorater) # 把my_decorater转换为类视图装饰器，只是装饰get
    def get(self, request):
        print('get方法')
        return HttpResponse('ok')

    def post(self, request):
        print('post方法')
        return HttpResponse("OK")
