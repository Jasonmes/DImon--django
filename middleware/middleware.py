#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Jason Mess

"""
自定义中间件

"""
def my_middleware(get_response):
    """
    类似before_first_request （中间件的初始化，第一次请求调用一次init）
    :param get_response:
    :return: middleware
    """
    print('init')
    def middleware(request):
        # before_request （每一次请求前调用）
        print('before request')
        response = get_response(request)

        # 每一次请求后调用 ：after request
        print('after request')
        return response

    return middleware