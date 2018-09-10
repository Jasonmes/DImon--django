# #!/usr/bin/env python
# # -*- coding:utf-8 -*-
# # Jason Mess
#
#
# from django.http import HttpResponse, JsonResponse
# from django.shortcuts import render
# from django.views.generic.base import View
#
# from .models import BookInfo, HeroInfo
#
# """
#
# 图书管理系统
# url:
# 请求方式:
#     GET  /books/     返回所有书   JSON/列表    200
#     POST /books/     返回新的书   JSON        201
#
#     GET /books/id/       返回id=id的数据 JSON 200
#     PUT /books/id/       修改书， 返回修改后的书  JSON  201
#     DELETE /books/id/    删除书，返回状态204
# """
#
# class BookApiView(View):
#     """
#
#     """
#     def get(self, request):
#         """
#         返回所有书
#         :param request:
#         :return:
#         """
#         books = BookInfo.objects.all()
#         list = []
#         for book in  books:
#             list.append({
#                 "id": book.id,
#                 "btitle": book.btitle,
#                 "bpub_date": book.bpub_date
#             })
#
#         return JsonResponse(list, safe=False)
#
#
#     def post(self, request):
#         """
#         增加书
#         :param request:
#         :return:
#         """
#         json_bytes = request.body
#          = json_bytes.decode()
#         json.loads(json_str)
#
#         book = BookInfo.objects.create(
#             book_dict.get()
#         )
#         return JsonResponse
#
#
# class BooksApiView(View):
#     """
#
#     """
#     def get(self, request, id):
#         """
#         返回id=id的数据(JSON) 201
#         :param request:
#         :param id:
#         :return:
#         """
#         try:
#             book = BookInfo.objects.get(id=id)
#         except BookInfo.DoesNotExist:
#             return HttpResponse('BooksApiView error get')
#         return JsonResponse({
#             "id": book.id,
#             "btitle": book.btitle,
#             "bpub_date": book.bpub_date
#         })
#
#
#     def put(self, request, id):
#         """
#         修改书，返回修改后的书 201
#         :param request:
#         :param id:
#         :return:
#         """
#
#
#     def delete(self, request, id):
#         """
#         删除书
#         :param request:
#         :param id:
#         :return:
#         """
#
#         return HttpResponse("204")