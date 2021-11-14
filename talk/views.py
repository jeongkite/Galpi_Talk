from django.http import response
from django.shortcuts import get_object_or_404, redirect, render
from talk.models import *
from accounts.models import AccessCode, Address
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def chap_bridge(request, cn):
    return render(request, 'talk/chap_bridge.html', {"cn": cn})


def chap_start(request, qn):
    question = get_object_or_404(Question, id=2)

    return render(request, 'talk/chap.html', {'question': question})


Chap = [1, 28, 40, 49]


def chap(request, qn):
    info = Info.objects.get(user=request.user)
    if (qn == 2) and (info.q_progress > 50):
        info.c_progress = 1
    elif qn == 29:
        info.c_progress = 2
    elif qn == 40:
        info.c_progress = 3
    elif qn == 50:
        info.c_progress = 4
    info.save()

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
    chapter = get_object_or_404(Chapter, pk=question.chapter.pk)
    info = request.user.info

    if request.method == "POST":
        answer = request.POST['answer']
        response.content = answer
        response.save()
        return HttpResponseRedirect(reverse('talk:chap', args=[info.q_progress]))
    ctx = {
        'chapter': chapter,
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
        'qn': 50,
        'this_q': question,
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

            return render(request, 'talk/chap50.html', context=ctx)
        else:
            for i in range(0, len(hellos)):
                hellos[i].name = request.POST['name' + str(i+1)]
                hellos[i].contact = request.POST['contact' + str(i+1)]
                hellos[i].save()
            return render(request, 'talk/chap50.html', context=ctx)
    else:
        return render(request, 'talk/chapter50.html', context=ctx)


def chapter51(request):
    info = Info.objects.get(user=request.user)
    chapter = get_object_or_404(Chapter, pk=4)
    question = get_object_or_404(Question, pk=51)
    responses = Response.objects.filter(user=request.user, question=question)
    response = None

    if responses:
        response = responses[0]
    ctx = {
        'chapter': chapter,
        'response': response,
        'question': question,
        'qn': 51,
    }

    if request.method == "POST":
        if not responses:
            answer = request.POST['answer']
            response = Response(user=request.user, chapter=chapter,
                                question=question, content=answer)
            response.save()
            ctx['response'] = response
            info.q_progress = 50
            info.c_progress = 5
            info.save()
            return render(request, 'talk/chap50.html', context=ctx)
        else:
            answer = request.POST['answer']
            response.content = answer
            response.save()
            info.q_progress = 50
            info.c_progress = 5
            info.save()
            ctx['response'] = response
            return render(request, 'talk/chap50.html', context=ctx)
    else:
        return render(request, 'talk/chapter51.html', context=ctx)


def write_last(request):
    chapter = get_object_or_404(Chapter, pk=5)
    question = get_object_or_404(Question, pk=52)
    responses = Response.objects.filter(user=request.user, question=question)
    response = None
    info = Info.objects.get(user=request.user)
    info.c_progress = 1
    info.q_progress = 52
    info.save()
    if responses:
        response = responses[0]
    if request.method == "POST":
        if not response:
            answer = request.POST['answer']
            response = Response(user=request.user, chapter=chapter,
                                question=question, content=answer)
        else:
            answer = request.POST['answer']
            response.content = answer
        response.save()
        return HttpResponseRedirect(reverse('talk:address'))
    else:
        ctx = {
            'chapter': chapter,
            'response': response,
            'question': question,
        }
        return render(request, 'talk/write_last.html', context=ctx)


def address(request):
    info = get_object_or_404(Info, user=request.user)
    add_num = info.address_num
    add_nums = ""
    for i in range(0, add_num+1):
        add_nums += str(i)
    addresss = Address.objects.filter(user=request.user)
    if request.method == "POST":
        if not addresss:
            address_arr = []
            for i in range(0, add_num+1):
                name = request.POST['name'+str(i)]
                phone = request.POST['phone'+str(i)]
                postal = request.POST['postal'+str(i)]
                addy = request.POST['addy'+str(i)]

                if (i == 0):
                    address = Address(
                        user=request.user, name=name, phone=phone, postal=postal, addy=addy, is_other=False)
                else:
                    address = Address(
                        user=request.user, name=name, phone=phone, postal=postal, addy=addy, is_other=True)
                address_arr.append(address)
            Address.objects.bulk_create(address_arr)
        else:
            for i in range(0, add_num+1):
                addresss[i].name = request.POST['name'+str(i)]
                addresss[i].phone = request.POST['phone'+str(i)]
                addresss[i].postal = request.POST['postal'+str(i)]
                addresss[i].addy = request.POST['addy'+str(i)]
                addresss[i].save()
        return render(request, 'talk/final.html')
    else:
        ctx = {
            'addresss': addresss,
            'add_nums': add_nums
        }
        return render(request, 'talk/address.html', context=ctx)


def final(request):
    return render(request, 'talk/final.html')


def chap5(request):
    return render(request, 'talk/chap5.html')
