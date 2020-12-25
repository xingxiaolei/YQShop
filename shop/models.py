from django.db import models
from datetime import datetime
from stdimage.models import StdImageField
from stdimage.utils import UploadToUUID
from DjangoUeditor.models import UEditorField

class Banner(models.Model):
    name = models.CharField(max_length=10, verbose_name='轮播图名称')
    image = StdImageField(max_length=100,
                          upload_to = UploadToUUID(path='banner/'),
                          verbose_name='轮播图',
                          variations={'thumbnail':{'width':100, 'height': 75}},
                          default=None,
                          blank=True,
                          null=True
                          )
    choice = (
        (0, '不展示'),
        (1, '展示')
    )
    display = models.SmallIntegerField(default=0, choices=choice, verbose_name='是否展示')
    add_time = models.DateTimeField(default=datetime.now(), verbose_name='创建时间')


    def __str__(self):
        return self.name

    class Meta:
        db_table = 'banner'
        verbose_name = '轮播图管理'
        verbose_name_plural = '轮播图管理'

    def image_img(self):
        if self.image:
            return str('<img src="%s">' % self.image.thumbnail.url)
        else:
            return u'上传图片'

    image_img.short_description = '轮播图'
    image_img.allow_tags = True

TYPE = (
    (1, '葡萄酒'),
    (2, '白兰地'),
    (3, '洋酒')
)

STANDARDS = (
    (1, '单瓶'),
    (2, '礼盒'),
    (3, '整箱')
)

PRICE_RANGE = (
    (1, '0-50'),
    (2, '50-200'),
    (3, '200-500'),
    (4, '500-1000'),
    (5, '1000以上'),
)

class Tag(models.Model):
    type = models.SmallIntegerField(default=1, choices=TYPE, verbose_name='酒种')
    name = models.CharField(max_length=10, verbose_name='标签分类')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tag'
        verbose_name = '标签分类'
        verbose_name_plural = verbose_name

class Label(models.Model):
    name = models.CharField(max_length=10, verbose_name='标签名称')
    tag = models.ForeignKey(Tag, verbose_name='所属标签分类', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'label'
        verbose_name = '所属标签分类'
        verbose_name_plural = verbose_name

class Goods(models.Model):
    name = models.CharField(max_length=20, verbose_name='商品名称')
    image = StdImageField(max_length=100,
                          upload_to = UploadToUUID(path='goods/'),
                          verbose_name='商品图',
                          variations={'thumbnail':{'width':100, 'height': 75}},
                          default=None,
                          blank=True,
                          null=True
                          )
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='商品价格')
    price_range = models.SmallIntegerField(default=1, choices=PRICE_RANGE, verbose_name='价格区间')
    standard = models.SmallIntegerField(default=1, choices=STANDARDS, verbose_name='规格')
    type = models.SmallIntegerField(default=1, choices=TYPE, verbose_name='酒种')
    tag = models.ForeignKey(Tag, verbose_name='标签分类', on_delete=models.CASCADE)
    label = models.ForeignKey(Label, verbose_name='商品标签', on_delete=models.CASCADE)
    detail = UEditorField(verbose_name='商品详情',width=1200, imagePath='goods_detail/', filePath='goods_file/', default='')
    choice = (
        (0, '下架'),
        (1, '上架')
    )
    status = models.SmallIntegerField(default=0, choices=choice, verbose_name='是否上架')
    choice1 = (
        (0, '否'),
        (1, '是')
    )
    index_display = models.SmallIntegerField(default=0, choices=choice1, verbose_name='是否首页展示')

    choice2 = (
        (0, '否'),
        (1, '是')
    )
    hot = models.SmallIntegerField(default=0, choices=choice2, verbose_name='是否爆款推荐')

    add_time = models.DateTimeField(default=datetime.now(), verbose_name='创建时间')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'goods'
        verbose_name = '商品管理'
        verbose_name_plural = verbose_name

    def image_img(self):
        if self.image:
            return str('<img src="%s">' % self.image.thumbnail.url)
        else:
            return u'上传图片'

    image_img.short_description = '商品图'
    image_img.allow_tags = True


class WishPool(models.Model):
    goods_name = models.CharField(max_length=50, verbose_name='欲购商品')
    name = models.CharField(max_length=10, verbose_name='客户姓名')
    phone = models.CharField(max_length=11, verbose_name='客户电话')
    wish = models.CharField(max_length=100, verbose_name='意向内容')
    trace = models.CharField(max_length=200, verbose_name='跟进', null=True, blank=True, default='')
    create_time = models.DateTimeField(default=datetime.now(), verbose_name='创建时间')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'wish'
        verbose_name = '意向池'
        verbose_name_plural = verbose_name