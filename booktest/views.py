from django.shortcuts import render

# Create your views here.
# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Jason Mess


from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from django.shortcuts import render
from django.views.generic.base import View

from .models import BookInfo, HeroInfo

import json
"""

图书管理系统
url:
请求方式:
    GET  /books/     返回所有书   JSON/列表    200
        操作数据(取所有书)
        转换成字典
        字典转换成JSON返回
    POST /books/     返回新的书   JSON        201
        获取前端发送过来的数据
        转换获取的数据为字典
        字典转出成模型类对象，写成数据库
        模型类对象转换成字典
        字典转换成JSON返回

    GET /books/id/       返回id=id的数据 JSON 200
        验证id，读取数据库id的书，获取模型类的对象
        模型类对象转换成字典
        字典转换成JSON返回
        
    PUT /books/id/       修改书， 返回修改后的书  JSON  201
        验证id，取数据库id的书，获取模型类对象(需要修改的书)
        获取前端发送过来的数据
        修改书(操作数据库)
        模型类对象转转成字典
        字典转换成JSON返回
        
    DELETE /books/id/    删除书，返回状态204
        验证id， 取数据库id的书，获取模型类对象(需要修改的书)
        操作数据库  delete
        返回 204
        
"""


class BookApiView(View):
    """

    """

    def get(self, request):
        """
        返回所有书
        :param request:
        :return:
        """
        books = BookInfo.objects.all()
        list = []
        for book in books:
            list.append({
                "id": book.id,
                "btitle": book.btitle,
                "bpub_date": book.bpub_date
            })

        return JsonResponse(list, safe=False)

    def post(self, request):
        """
        增加书,返回新的书(JSON)
        获取前段发送过来的数据
        :param request:
        :return:
        """
        json_bytes = request.body
        json_str = json_bytes.decode()
        book_dict = json.loads(json_str)

        # 验证
        # 增加书
        book = BookInfo.objects.create(
            btitle=book_dict.get('btitle'),
            bpub_date=book_dict.get('bpub_date'),
        )

        # 返回新的书
        return JsonResponse({
            "id": book.id,
            "btitle": book.btitle,
            "bpub_date": book.bpub_date
        }, status=201)




class BooksApiView(View):
    """

    """

    def get(self, request, id):
        """
        返回id=id的数据(JSON) 200
        :param request:
        :param id:
        :return:
        """
        # 验证id，读取数据库id的书
        try:
            book = BookInfo.objects.get(id=id)
        except BookInfo.DoesNotExist:
            return HttpResponseNotFound('BooksApiView error get')

        return JsonResponse({
            "id": book.id,
            "btitle": book.btitle,
            "bpub_date": book.bpub_date
        }, status=200)

    def put(self, request, id):
        """
        修改书，返回修改后的书(JSON) 201
        :param request:
        :param id:
        :return:
        """
        try:
            book = BookInfo.objects.get(id=id)
        except BookInfo.DoesNotExist:
            return HttpResponseNotFound('error')

        # 获取前端发送过来的数据
        json_bytes = request.body
        json_str = json_bytes.decode()
        book_dict = json.loads(json_str)

        # 修改
        book.btitle = book_dict.get('btitle', book.btitle)
        book.bpub_date = book_dict.get('bpub_date', book.bpub_date)
        book.save()

        return JsonResponse({
            "id": book.id,
            "btitle": book.btitle,
            "bpub_date": book.bpub_date
        }, status=201)



    def delete(self, request, id):
        """
        删除书  返回状态204
        :param request:
        :param id:
        :return:
        """
        # 验证id，取数据库id的书
        try:
            book = BookInfo.objects.get(id=id)
        except BookInfo.DoesNotExist:
            return HttpResponseNotFound('error')
         # 操作数据库 删除
        book.delete()
        return HttpResponse(status=204)