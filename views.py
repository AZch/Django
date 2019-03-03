import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from xml.sax.saxutils import escape
from django.http import JsonResponse

import cv2
import glob

from lr.models import *




def loadPhotosExt(photoLoc, ext):
    photos = []
    for img in glob.glob(photoLoc + "*." + ext):
        imgRead = cv2.imread(img)
        if imgRead is not None:
            photos.append(img)
    return photos


def getPhotos(photoLocation):
    images = []
    images.append(loadPhotosExt(photoLocation, 'jpg'))
    images.append(loadPhotosExt(photoLocation, 'png'))
    images.append(loadPhotosExt(photoLocation, 'jpeg'))


def renderIndex(request, admin):
    landfill = Landfill.objects.all() # Landfill.objects.all().order_by('name')
    #for i in range(len(landfill)):
     #   landfill[i].photolocation = getPhotos(landfill[i].photoLocation)

    context = {
        'landfill': landfill,
        'admin': admin
    }
    return render(request, 'index.twig', context)


@require_http_methods(["GET"])
def index(request):
    return renderIndex(request, False)


@require_http_methods(["GET"])
def admin(request):
    return renderIndex(request, True)


def landfillOpen(request, id):
    try:
        landfill = Landfill.objects.get(id=id)
        landfill.datefind = str(landfill.datefind)
        landfill.datestatement = str(landfill.datestatement)
        info = landfill
    except Exception:
        return HttpResponse('Свалка с id = ' + str(id) + ' не найдена, сообщите администратору')

    #info.photolocation = getPhotos(info.photolocation)
    vols = Volunteers.objects.filter(idlandfillvolunt=id)
    events = Events.objects.filter(idlandfillevent=id)

    context = {
        'info': info
    }
    return render(request, 'openDump.twig', context)


def form(request, id):
    context = {
        'edit': id != False
    }
    if id != False:
        try:
            landfill = Landfill.objects.get(id=id)
            landfill.datefind = str(landfill.datefind)
            landfill.datestatement = str(landfill.datestatement)
            context['info'] = landfill
            print(landfill.datefind)
        except Exception:
            return HttpResponse('Свалка с id = ' + str(id) + ' не найдена, сообщите администратору')
    return render(request, 'form.twig', context)


@require_http_methods(["GET"])
def formAdd(request):
    return form(request, False)


@require_http_methods(["GET"])
def formEdit(request, id):
    return form(request, id)


def htmlSpecialChars(unsafe):
    return escape(unsafe, {'"': '&quot;', '\'': '&#039;'})


def landfillPost(request, id):
    if id != False:
        landfill = Landfill.objects.get(id=id)
    else:
        landfill = Landfill()
    formatStr = '%Y-%m-%d'

    landfill.name = htmlSpecialChars(request.POST['nameDump'].strip())
    if len(landfill.name) == 0:
        return JsonResponse({'result': 'Error', 'message': 'Название свалки не может оставаться пустым'})

    landfill.location = htmlSpecialChars(request.POST['location'])
    if len(landfill.location) == 0:
        return JsonResponse({'result': 'Error', 'message': 'Местоположение свалки не может оставаться пустым'})

    landfill.datefind = datetime.datetime.strptime(htmlSpecialChars(request.POST['datefind']), formatStr)
    # if len(landfill.dateFind) == 0:
    #     return JsonResponse({'result': 'Error', 'message': 'Дата нахождения свалки не может оставаться пустым'})

    landfill.datestatement = datetime.datetime.strptime(htmlSpecialChars(request.POST['datestatement']), formatStr)
    # if len(landfill.dateStatement) == 0:
    #     return JsonResponse(
    #         {'result': 'Error', 'message': 'Дата подачи заявления на свалку не может оставаться пустым'})

    landfill.photolocation = htmlSpecialChars(request.POST['photolocation'])
    if len(landfill.photolocation) == 0:
        return JsonResponse(
            {'result': 'Error', 'message': 'Ссылка с фотографиями на свалку не может оставаться пустым'})

    landfill.save()
    return JsonResponse({'result': 'OK'})



@require_http_methods(["GET", "POST", "DELETE"])
def landfill(request, id):
    if request.method == "GET":
        return landfillOpen(request, id)
    elif request.method == "POST":
        return landfillPost(request, id)
    elif request.method == "DELETE":
        landfill.objects.filter(id=id).delete()
        return HttpResponse('')

@require_http_methods(["POST", "DELETE"])
def landfillDel(request, id):
    Landfill.objects.filter(id=id).delete()
    return HttpResponse('')



@require_http_methods(["POST"])
def landfillAdd(request):
    return landfillPost(request, False)