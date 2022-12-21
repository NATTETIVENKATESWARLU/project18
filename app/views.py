from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.


def insert_Topic(request):
    if request.method=='POST':
        tn=request.POST['topic']
        t=Topic.objects.get_or_create(topic_name=tn)[0]
        t.save()
        return HttpResponse("yes submited")

        
    return render(request,'insert_Topic.html')




def insert_webpage(request):
    l=Topic.objects.all()
    d={'l':l}

    if request.method=='POST':
        tn=request.POST['l']
        na=request.POST['na']
        ur=request.POST['url']
        t=Topic.objects.get_or_create(topic_name=tn)[0]
        t.save()
        w=webpage.objects.get_or_create(topic_name=t,name=na,url=ur)[0]
        w.save()
        return HttpResponse("yes submited")

        
    return render(request,'insert_webpage.html',d)






def insert_A_R(request):
    l=Topic.objects.all()
    d={'l':l}
    if request.method=='POST':
        ta=request.POST['l']
        na=request.POST['b']
        ba=request.POST['a']
        da=request.POST['date']
        t=Topic.objects.get_or_create(topic_name=ta)[0]
        t.save()
        w=webpage.objects.get_or_create(topic_name=t,name=na,url=ba)[0]
        w.save()
        dn=Access_Recorde.objects.get_or_create(name=w,date=da)[0]
        dn.save()

        return HttpResponse("yes submited")

        
    return render(request,'insert_A_R.html',d)




def update_webpage(request):
    v=Topic.objects.all()
    d={'v':v}
    if request.method=='POST':
        ta=request.POST['v']
        tn=request.POST['name']
        th=request.POST['url']
        webpage.objects.filter(topic_name=ta).update(name=tn,url=th)
        return HttpResponse("yes submited")

    return render(request,'update_webpage.html',d)  



def delete_webpage(request):
    v=Topic.objects.all()
    d={'v':v}
    if request.method=='POST':
        ta=request.POST['v']
        va=request.POST['name']
        Topic.objects.filter(topic_name=va).delete()
        webpage.objects.filter(topic_name=va).delete()
        return HttpResponse("yes submited")

    return render(request,'delete_webpage.html',d) 


def select_topic(request):
    v=Topic.objects.all()
    d={'v':v}
    if request.method=='POST':
        ta=request.POST.getlist('v')
        web=webpage.objects.none()
        for i in ta:
            web=web|webpage.objects.filter(topic_name=i)
        d={'web':web}
        return render(request,'display.html',d)

    return render(request,'select_topic.html',d)
    
