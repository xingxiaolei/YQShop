import xadmin
from shop.models import Banner

class BannerAdmin(object):
    list_display = ['name', 'image_img', 'display', 'add_time']

xadmin.site.register(Banner, BannerAdmin)