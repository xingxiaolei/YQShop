import xadmin
from shop.models import Banner, Tag, Label, Goods, WishPool

class BannerAdmin(object):
    list_display = ['name', 'image_img', 'display', 'add_time']

class TagAdmin:
    list_display = ['id', 'name', 'type']
    # inlines = [Label, ]

class LabelAdmin:
    list_display = ['id', 'name', 'tag']
    # model = Tag
    # extra = 1

class GoodsAdmin:
    list_display = ['id', 'name', 'image_img', 'type', 'status']
    style_fields = {'detail': 'ueditor'}

class WishPoolAdmin:
    list_display = ['id', 'goods_name', 'name', 'phone', 'wish', 'trace']


xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(Tag, TagAdmin)
xadmin.site.register(Label, LabelAdmin)
xadmin.site.register(Goods, GoodsAdmin)
xadmin.site.register(WishPool, WishPoolAdmin)
