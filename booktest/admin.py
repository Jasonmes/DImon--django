from django.contrib import admin

# Register your models here.

"""
注册模型类
"""

from django.contrib import admin
from booktest.models import BookInfo, HeroInfo

admin.site.register(BookInfo)
admin.site.register(HeroInfo)


admin.site.site_title = '微书网站'
admin.site.site_header = '微书管理'
admin.site.index_title = '微书'


"""
关联编辑（块方式）
"""
class HeroInfoStackInline(admin.StackedInline):
    model = HeroInfo   # 编辑的模型类
    extra = 1          # 增空栏

class HeroInfoTabInline(admin.TabularInline):
    model = HeroInfo   # 编辑的模型类
    extra = 1          # 增空栏


"""
定义与使用Admin管理类
使用管理器
"""
# @admin.register(BookInfo)
class BookInfoAdmin(admin.ModelAdmin):
    """
    页列表
    """
    list_per_page = 100
    """
    顶部显示属性 
    actions_on_top = True/False
    底部显示属性
    actions_on_bottom = True/False
    """
    actions_on_top = True
    actions_on_bottom = True

    """
    属性如下
    """
    list_display = ['id',
                    'hname',
                    'hbook',
                    'read',
                    'hgender',
                    'hcomment',
                    'read_hero']

    """
    将方法作为列
    设置short_description属性
    """

    """
    右侧过滤器
    """
    list_filter = ['hbook',
                   'hgender']

    """
    搜索框
    """
    search_fields = ['hname']

    """
    分组显示
    """
    fieldsets = (
        ('基础', {'fields': ['btitle',
                           'bpub_date',
                           'image']}),
        ('高级', {
            'fields': ['bread',
                       'bcomment'],
            'classes': ('collapse',)   # 是否折叠显示
        })
    )
    inlines = [HeroInfoTabInline]

# @admin.register(HeroInfo)
class HeroInfoAdmin(admin.ModelAdmin):
    """
    自定义英雄类admin
    """
    list_per_page = 5
    list_display = ['hname',
                    'id',
                    'hgender',
                    'hcomments',
                    'hbook']
    actions_on_bottom = True
    actions_on_top = False
    """
    指定过滤栏
    """
    list_filter = ['hbook', 'hgender']
    search_fields = ['hname']
