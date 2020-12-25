import xadmin
from shop.models import Banner, Tag, Label, Goods, WishPool

class BannerAdmin(object):
    list_display = ['name', 'image_img', 'display', 'add_time']
    search_fields = ['name']
    list_filter = ['display']

class TagAdmin:
    list_display = ['id', 'name', 'type']
    search_fields = ['name']

class LabelAdmin:
    list_display = ['id', 'name', 'tag']
    search_fields = ['name']

class GoodsAdmin:
    list_display = ['id', 'name', 'image_img', 'type', 'status', 'index_display', 'hot']
    style_fields = {'detail': 'ueditor'}
    search_fields = ['name']
    list_filter = ['type', 'status', 'index_display', 'hot']


class WishPoolAdmin:
    list_display = ['id', 'goods_name', 'name', 'phone', 'wish', 'trace']
    search_fields = ['name', 'phone']


xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(Tag, TagAdmin)
xadmin.site.register(Label, LabelAdmin)
xadmin.site.register(Goods, GoodsAdmin)
xadmin.site.register(WishPool, WishPoolAdmin)
