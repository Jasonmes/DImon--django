from django.db import models

# Create your models here.

"""
定义模型类
定义图书模型类BookInfo
数据库中的字段field

"""
from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings


class BookInfo(models.Model):
    """
    生成数据库
    数据库表面：小写app应用名_小写模型类名
    属性=models.字段类型(选项)
    """
    btitle = models.CharField(max_length=20, verbose_name='名称')
    bpub_date = models.DateField(verbose_name='发布日期')
    bread = models.IntegerField(default=0, verbose_name='阅读量')
    bcomment = models.IntegerField(default=0, verbose_name='评论量')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')
    """
    添加图片字段
    """
    image = models.ImageField(verbose_name='图片', null=True, upload_to='books')

    class Meta:
        db_table = 'tb_books'  # 指明数据库表名
        verbose_name = '图书'  # 在admin站点中显示的名称 verbose--->> 详细
        verbose_name_plural = verbose_name  # 显示的复数名称

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.btitle

    """
    # 设置方法字段在admin中显示的标题
    """
    def pub_date(self):
        return self.bpub_date.strftime('%Y年%m月%d日')

    pub_date.short_description = '发布日期'

    """
    为方法指定排序依据
    使用已有的属性进行排序
    """
    pub_date.admin_order_field = 'bpub_date'


    """
    函数返回所有的图书的英雄
    """
    def read_hero(self):
        list = []
        """
        查询hbook_id为self.id的书籍的所有英雄
        """
        heros = HeroInfo.objects.filter(hbook__id=self.id)
        for hero in heros:
            list.append(hero.hname)
        return list
    # 函数的描述给前端看的
    read_hero.short_description = '英雄列表'


"""
定义英雄模型类HeroInfo
"""
class HeroInfo(models.Model):
    GENDER_CHOICES = (
        (0, 'female'),
        (1, 'male')
    )

    hname = models.CharField(max_length=20, verbose_name='名称')
    hgender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0, verbose_name='性别')
    hcomment = models.CharField(max_length=200, null=True, verbose_name='描述信息')
    hbook = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name='图书')  # 外键
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')


    class Meta:
        db_table = 'tb_heros'
        verbose_name = '英雄'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.hname
    """
    在模型类中封装方法，访问关联对象的成员
    """
    def read(self):
        return self.hbook.bread

    read.short_description = '图书阅读量'


def get_sentinel_user():
    """

    :return:
    """
    return get_user_model().objects.get_or_create(username='delete')[0]

class MyModel(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET(get_sentinel_user),
    )



"""
A
将模型类同步到数据库中
迁移
将模型类同步到数据库中。

1）生成迁移文件

python manage.py makemigrations
2）同步到数据库中

python manage.py migrate
"""


"""
B
shell
python manage.py shell
"""

"""
C
查看mysql数据库日志
"""
