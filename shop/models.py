from django.db import models
from datetime import datetime
from stdimage.models import StdImageField
from stdimage.utils import UploadToUUID

class Banner(models.Model):
    name = models.CharField(max_length=10, verbose_name='轮播图名称')
    image = StdImageField(max_length=100,
                          upload_to = UploadToUUID(path='banner/'),
                          verbose_name='轮播图',
                          variations={'thumbnail':{'width':100, 'height': 75}},
                          default=None
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