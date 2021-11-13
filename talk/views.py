from django.http import response
from django.shortcuts import get_object_or_404, redirect, render
from talk.models import *
from accounts.models import AccessCode
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def chap_bridge(request, cn):
    return render(request, 'talk/chap_bridge.html', {"cn": cn})


def chap_start(request, qn):
    user_code = get_object_or_404(AccessCode, user=request.user)

    try:
        info = Info.objects.get(user=request.user)
    except Info.DoesNotExist:
        info = Info(user=request.user,
                    address_num=int(user_code.access_code[0]),
                    c_progress=1,
                    q_progress=1)
        info.save()
    question = get_object_or_404(Question, id=2)

    return render(request, 'talk/chap.html', {'question': question})


Chap = [1, 28, 40, 49]


def chap(request, qn):
    info = Info.objects.get(user=request.user)

    chapter = get_object_or_404(Chapter, chap_num=info.c_progress)
    questions = Question.objects.filter(
        id__lte=int(info.q_progress)+1, chapter=chapter)
    qn = questions.last().id
    this_q = get_object_or_404(Question, id=qn)
    bubbles = []
    for q in questions:
        this_response = q.response_set.filter(user=request.user)

        if this_response:
            item = []
            item.append(q)
            item.append(this_response[0])
            bubbles.append(item)

    if request.method == "POST":
        answer = request.POST['answer']
        response = Response(user=request.user, chapter=chapter,
                            question=questions[info.q_progress-Chap[chapter.chap_num-1]], content=answer)
        response.save()
        info.q_progress += 1
        info.save()
        if (info.q_progress == 28) or (info.q_progress == 40) or (info.q_progress == 49):
            info.c_progress += 1
            info.save()
            return render(request, 'talk/chap_bridge.html', {'cn': info.c_progress})
        return HttpResponseRedirect(reverse('talk:chap', args=[qn]))

    ctx = {
        'chapter': chapter,
        'bubbles': bubbles,
        'qn': qn,
        'this_q': this_q,
    }

    return render(request, 'talk/chap.html', context=ctx)


def update_answer(request, rn):
    response = get_object_or_404(Response, pk=rn)
    question = get_object_or_404(Question, pk=response.question.id)
    info = request.user.info

    if request.method == "POST":
        answer = request.POST['answer']
        response.content = answer
        response.save()
        return HttpResponseRedirect(reverse('talk:chap', args=[info.q_progress]))
    ctx = {
        'question': question,
        'response': response,
    }
    return render(request, 'talk/answer_update.html', context=ctx)


def chapter50(request):
    info = Info.objects.get(user=request.user)
    hellos = LastHello.objects.filter(user=request.user)
    chapter = get_object_or_404(Chapter, pk=4)
    question = get_object_or_404(Question, pk=50)
    ctx = {
        'chapter': chapter,
        'question': question,
        'hellos': hellos,
        'qn': 51,
    }

    if request.method == "POST":
        if not hellos:
            arr = []
            for i in range(1, 7):
                arr.append(LastHello(user=request.user, chapter=chapter, question=question,
                                     name=request.POST['name' + str(i)], contact=request.POST['contact' + str(i)]))

            hello = LastHello.objects.bulk_create(arr)
            info.q_progress += 1
            info.save()

            return render(request, 'talk/chap.html', context=ctx)
        else:
            for i in range(1, len(hellos)):
                hellos[i].name = request.POST['name' + str(i)]
                hellos[i].contact = request.POST['contact' + str(i)]
                hellos[i].save()
            return render(request, 'talk/chap.html', context=ctx)
    else:
        return render(request, 'talk/chapter50.html', context=ctx)


def chapter51(request):
    info = Info.objects.get(user=request.user)
    responses = Response.objects.filter(user=request.user)
    response = responses[0]
    chapter = get_object_or_404(Chapter, pk=4)
    question = get_object_or_404(Question, pk=51)
    ctx = {
        'chapter': chapter,
        'question': question,
        'response': response,
        'qn': 51,
    }

    if request.method == "POST":
        if not response:
            answer = request.POST['answer']
            response = Response(user=request.user, chapter=chapter,
                                question=question, content=answer)
            response.save()
            info.q_progress = 50
            info.c_progress = 4
            info.save()
            return render(request, 'talk/chap_bridge.html', {'cn': info.c_progress})
        else:
            answer = request.POST['answer']
            response.content = answer
            response.save()
            return render(request, 'talk/chap_bridge.html', {'cn': info.c_progress})
    else:
        return render(request, 'talk/chapter51.html', context=ctx)
