from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import QuestionInfo, VoteInfo
# Create your views here.

def Index(request):
    # return HttpResponse('123')
    p1 = QuestionInfo.objects.all()
    # return render(request, 'polls/index.html', {'plist': "首页"})
    return render(request, 'polls/index.html', {'plist': p1})
def Detail(request,id):
    question = QuestionInfo.objects.get(pk=id)
    # return HttpResponse('123')
    return render(request, 'polls/detail.html', {'question': question})

def VoteHandler(request):

    choice = VoteInfo.objects.get(pk=request.POST['vote'])
    choice.vnum += 1
    choice.save()
    # return HttpResponse('123')
    return HttpResponseRedirect('/result/'+str(choice.id)+'/',)
def Result(request,oid):
    Vquestion = VoteInfo.objects.get(pk=oid).vquestion
    # return HttpResponse('123')
    return render(request,'polls/result.html', {"Vquestion":Vquestion})
