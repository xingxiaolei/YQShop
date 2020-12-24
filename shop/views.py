from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.conf import settings
from shop.models import Banner, Label, Tag, Goods, WishPool
from django.views import View

from django.core.paginator import Paginator

def global_settings(request):
    return {
        'MEDIA_URL': settings.MEDIA_URL
    }


class Index(View):
    def get(self, request):
        bann = Banner.objects.filter(display=1)


        context = {
            'bann': bann
        }

        return render(request, 'index.html', context=context)

class GoodsList(View):

    def get(self, request, type_id):

        tags = Tag.objects.filter(type=int(type_id))

        check_goods = Goods.objects.filter(type=int(type_id), status=1)

        paginator = Paginator(check_goods, 15)

        page_nums = paginator.num_pages
        page = paginator.page(1)
        context = {
            'type': type_id,
            'tags': tags,
            'check_goods': page,
            'page_nums': page_nums
        }

        return render(request, 'list.html', context=context)


class GoodsDetail(View):

    def get(self, request):
        goods_id = request.GET.get('goods_id')

        goods = Goods.objects.get(id=int(goods_id))

        context = {
            'goods_name': goods.name,
            'goods_price': goods.price,
            'goods_img': str(goods.image),
            'goods_detail': goods.detail,
            'goods_id': goods_id
        }

        return render(request, 'detail.html', context=context)

def check_goods(request):
    res = request.POST

    dic = {}
    for k, v in res.items():
        if v:
            dic[k] = v
    del dic['csrfmiddlewaretoken']
    dic['status'] = 1
    goods = Goods.objects.filter(**dic)
    goods_lst = []
    for good in goods:
        goods_lst.append(
            {
                'good_id': good.id,
                'good_name': good.name,
                'good_img': str(good.image),
                'good_price': good.price
            }
        )
    paginator = Paginator(goods_lst, 15)

    return JsonResponse(goods_lst, safe=False)

def wish(request):
    res = request.POST

    goods = Goods.objects.get(id=int(res['id']))
    goods_name = goods.name
    name = res['name']
    phone = res['phone']
    wish = res['wish']
    try:
        WishPool.objects.create(goods_name=goods_name, name=name, phone=phone, wish=wish)
        return HttpResponse('1')
    except Exception as e:
        return HttpResponse('0')

