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
                            question=questions[info.q_progress-1], content=answer)
        response.save()
        info.q_progress += 1
        if (info.q_progress == 28) or (info.q_progress == 40) or (info.q_progress == 49):
            info.c_progress += 1
            return render(request, 'talk/chap_bridge.html', {'cn': info.c_progress})
        info.save()
        return HttpResponseRedirect(reverse('talk:chap', args=[qn]))

    q = get_object_or_404(Question, id=13)
    choices = q.choice_set.all()
    print(choices)
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
