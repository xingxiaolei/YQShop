from django.shortcuts import render, HttpResponse
from django.core import serializers
from django.http import JsonResponse
from django.conf import settings
from shop.models import Banner, Label, Tag, Goods, WishPool
from django.views import View
import json
from django.core.paginator import Paginator

def global_settings(request):
    return {
        'MEDIA_URL': settings.MEDIA_URL
    }

class Index(View):
    def get(self, request):
        bann = Banner.objects.filter(display=1)

        hot_goods = Goods.objects.filter(status=1, index_display=1, hot=1)
        box_goods = Goods.objects.filter(status=1, index_display=1, standard=3)
        single_goods = Goods.objects.filter(status=1, index_display=1, standard=1)
        gift_goods = Goods.objects.filter(status=1, index_display=1, standard=2)


        context = {
            'bann': bann,
            'hot_goods': hot_goods,
            'box_goods': box_goods,
            'single_goods': single_goods,
            'gift_goods': gift_goods
        }

        return render(request, 'index.html', context=context)

class GoodsList(View):

    def get(self, request, type_id, page):
        page = int(page)

        if request.GET:
            dic = {}
            for k, v in request.GET.items():
                if v:
                    dic[k] = v
            del dic['csrfmiddlewaretoken']
            dic['status'] = 1
            goods = Goods.objects.filter(**dic)
            # goods_lst = []
            # for good in goods:
            #     goods_lst.append(
            #         {
            #             'good_id': good.id,
            #             'good_name': good.name,
            #             'good_img': str(good.image),
            #             'good_price': good.price
            #         }
            #     )


            paginator = Paginator(goods, 1)

            num_pages = paginator.num_pages

            pager = paginator.page(page)

            if num_pages < 5:
                pages = range(1, num_pages + 1)
            elif page <= 3:
                pages = range(1, 6)
            elif num_pages - page <= 2:
                pages = range(num_pages - 4, num_pages + 1)
            else:
                pages = range(page - 2, page + 3)


            json_data = serializers.serialize("json", goods, ensure_ascii=False)  # str类型
            # data = {}
            # data['pager'] = json_data
            # data['pages'] = str(list(pages))
            #
            # data = json.dumps(json_data, ensure_ascii=False)

            return JsonResponse(json_data, safe=False)
        else:

            tags = Tag.objects.filter(type=int(type_id))

            check_goods = Goods.objects.filter(type=int(type_id), status=1)

            paginator = Paginator(check_goods, 15)

            num_pages = paginator.num_pages

            pager = paginator.page(page)

            if num_pages < 5:
                pages = range(1, num_pages + 1)
            elif page <= 3:
                pages = range(1, 6)
            elif num_pages - page <= 2:
                pages = range(num_pages - 4, num_pages + 1)
            else:
                pages = range(page - 2, page + 3)

            context = {
                'type': type_id,
                'tags': tags,
                'check_goods': pager,
                'pages': pages
            }

            return render(request, 'list.html', context=context)

    def post(self, request):
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

        num_pages = paginator.num_pages


        return JsonResponse(goods_lst, safe=False)


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

