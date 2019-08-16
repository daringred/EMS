from django.shortcuts import render
from django.http import HttpResponse
from .models import Equipment
from utils.paginator import get_page


# Create your views here.
def index(request):
    equips = Equipment.objects.all()
    paginator, equip_list = get_page(request, equips)
    context = {'equip_list': equip_list, 'pages': paginator}
    return render(request, 'equip_manage_plat/index.html', context=context)


# def search_imei(request):
#     if request.method == 'GET':
#         IMEI = request.GET.get('imei', default='').strip()
#         # 根据IMEI号查出来只有一个设备
#         equips = Equipment.objects.filter(IMEI=IMEI)
#         if equips:
#             borrower = equips[0].borrower
#             context = {'equips': equips, 'borrower': borrower}
#             return render(request, 'equip_manage_plat/search_result.html', context=context)
#
#         else:
#             return HttpResponse('找不到该IMEI号的设备!')
#
#
# def search_code(request):
#     if request.method == 'GET':
#         code = request.GET.get('code', default='').strip()
#         # 根据设备代号查出来有可能会有多台设备
#         equips = Equipment.objects.filter(code=code)
#         if equips:
#             context = {'equips': equips}
#             return render(request, 'equip_manage_plat/code.html', context=context)
#         else:
#             return HttpResponse('找不到该设备代号的设备!')
#
#
# def search_borrower(request):
#     if request.method == 'GET':
#         borrower = request.GET.get('borrower', default='').strip()
#         equips = Equipment.objects.filter(borrower__name=borrower)
#         # 根据借用人查出来有可能会有多台设备
#         if equips:
#             context = {'equips': equips}
#             return render(request, 'equip_manage_plat/borrower.html', context=context)
#         else:
#             return HttpResponse('未找到%s的设备!' % borrower)


def search(request):
    if request.method == 'GET':
        IMEI = request.GET.get('imei').strip()
        code = request.GET.get('code').strip()
        borrower = request.GET.get('borrower').strip()
        owner = request.GET.get('owner').strip()
        if not IMEI and not code and not borrower and not owner:
            equips = Equipment.objects.all()
            paginator, equip_list = get_page(request, equips)
            context = {'equip_list': equip_list, 'pages': paginator}
            return render(request, 'equip_manage_plat/index.html', context=context)

        equips = Equipment.objects.filter(IMEI__icontains=IMEI, borrower__icontains=borrower, code__icontains=code,
                                          owner__icontains=owner)
        if equips:
            paginator, equip_list = get_page(request, equips)
            # pre_page =
            context = {
                'equip_list': equip_list,
                'pages': paginator,
                'imei': IMEI,
                'code': code,
                'borrower': borrower,
                'owner': owner,
            }
            return render(request, 'equip_manage_plat/search_result.html', context=context)
        else:
            return render(request, 'equip_manage_plat/device_not_find.html')
        # if IMEI:
        #     # 模糊匹配
        #     equips = Equipment.objects.filter(IMEI__icontains=IMEI)
        #     if equips:
        #         # borrower = equips[0].borrower
        #         paginator, equip_list = get_page(request, equips)
        #         context = {'equip_list': equip_list, 'pages': paginator}
        #         return render(request, 'equip_manage_plat/search_result.html', context=context)
        #     else:
        #         return HttpResponse('找不到该IMEI号的设备!')
        # elif code and borrower:
        #     equips = Equipment.objects.filter(borrower__icontains=borrower, code__icontains=code)
        #     # 根据设备代号+借用人查出来有可能会有多台设备
        #     if equips:
        #         paginator, equip_list = get_page(request, equips)
        #         context = {'equip_list': equip_list, 'pages': paginator}
        #         return render(request, 'equip_manage_plat/search_result.html', context=context)
        #     else:
        #         return HttpResponse('%s 没有借用代号为 %s 的设备!' % (borrower, code))
        # elif code and owner:
        #     # 根据设备代号和归属人查出来有可能会有多台设备
        #     equips = Equipment.objects.filter(code__icontains=code, owner__icontains=owner)
        #     if equips:
        #         paginator, equip_list = get_page(request, equips)
        #         context = {'equip_list': equip_list, 'pages': paginator}
        #         return render(request, 'equip_manage_plat/search_result.html', context=context)
        #     else:
        #         return HttpResponse('%s 没有代号为 %s 的设备！' % (owner, code))
        # elif borrower:
        #     equips = Equipment.objects.filter(borrower__icontains=borrower)
        #     # 根据借用人查出来有可能会有多台设备
        #     if equips:
        #         paginator, equip_list = get_page(request, equips)
        #         context = {'equip_list': equip_list, 'pages': paginator}
        #         return render(request, 'equip_manage_plat/search_result.html', context=context)
        #     else:
        #         return HttpResponse('未找到 %s 借用的设备!' % borrower)
        # elif code:
        #     equips = Equipment.objects.filter(code__icontains=code)
        #     # 根据设备代号查出来有可能会有多台设备
        #     if equips:
        #         paginator, equip_list = get_page(request, equips)
        #         context = {'equip_list': equip_list, 'pages': paginator}
        #         return render(request, 'equip_manage_plat/search_result.html', context=context)
        #     else:
        #         return HttpResponse('未找到项目代号为 %s 的设备!' % code)
        #
        # elif owner:
        #     equips = Equipment.objects.filter(owner__icontains=owner)
        #     # 根据归属人查出来有可能会有多台设备
        #     if equips:
        #         paginator, equip_list = get_page(request, equips)
        #         context = {'equip_list': equip_list, 'pages': paginator}
        #         return render(request, 'equip_manage_plat/search_result.html', context=context)
        #     else:
        #         return HttpResponse('未找到属于 %s 的设备!' % owner)
        # else:
        #     return HttpResponse('不支持该种组合搜索方式！请换一种方式搜索！')
