from django.shortcuts import render

from app.models import *
from django.db.models import Q

# Create your views here.
def display_topic(request):
    QLTO=Topic.objects.all()
    d={'topics':QLTO}
    return render(request,'display_topics.html',context=d)

def display_webpages(request):
    QSW=Webpage.objects.all()
    QSW = Webpage.objects.filter(Q(name = 'Raina') & Q(topic_name = 'Cricket'))
    QSW = Webpage.objects.filter(Q(url__endswith = 'com') & Q(topic_name = 'Cricket'))
    QSW = Webpage.objects.all()


    
    d={'webpages':QSW}
    return render(request,'display_webpages.html',d)

    
from django.http import HttpResponse


def insert_topic(request):
    tn=input('enter topic name')
    T=Topic.objects.get_or_create(topic_name=tn)[0]
    T.save()
    return HttpResponse('Topic is inserted successfully')

def insert_webpage(request):
    tn=input('enter topic_name')
    name=input('enter name')
    url=input('enter url')
    T=Topic.objects.get_or_create(topic_name=tn)[0]
    T.save()
    W=Webpage.objects.get_or_create(topic_name=T,name=name,url=url)[0]
    W.save()
    return HttpResponse('Webpage data is Inserted')



def update_webpage(request):

    Webpage.objects.filter(topic_name = 'Cricket').update(name = "Rinku")
    Webpage.objects.filter(name = 'Rinku').update(topic_name = 'football')
    
    QSW=Webpage.objects.all()
    d={'webpages':QSW}
    return render(request,'display_webpages.html',d)


def delete_webpages(request):
    
    # Webpage.objects.filter(name = 'vollybal').delete()
    Webpage.objects.all().delete()
    QSW = Webpage.objects.all()
    d = {'webpages' : QSW}
    return render(request,'display_webpages.html',d)