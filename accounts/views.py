from django.contrib.auth import authenticate, login
from django.core.checks import messages
from django.shortcuts import get_object_or_404, get_list_or_404, render, redirect
from accounts.forms import PrivacyForm, UserForm
from accounts.models import AccessCode, Privacy


def signup(request):
    """
    계정생성
    """
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            access_code = None
            code = form.cleaned_data.get('code')
            access_code = AccessCode.objects.filter(access_code=code).first()
            if access_code == None:
                message = "잘못된 인증코드입니다."
                return render(request, 'accounts/signup.html', {'form': form, 'message': message})
            elif (access_code.is_used == True):
                message = "이미 사용된 인증코드입니다."
                return render(request, 'accounts/signup.html', {'form': form, 'message': message})
            else:
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username,
                                    password=raw_password)  # 사용자 인증
                access_code.is_used = True
                access_code.user = user
                access_code.save()
                login(request, user,
                      backend='django.contrib.auth.backends.ModelBackend')

                return redirect('accounts:info')
    else:
        form = UserForm()
    return render(request, 'accounts/signup.html', {'form': form})


def intro(request):
    return render(request, 'accounts/intro.html')


def start(request):
    return render(request, 'accounts/start.html')


def info(request):
    return render(request, 'accounts/info.html')


def help1(request):
    return render(request, 'accounts/help1.html')


def help2(request):
    return render(request, 'accounts/help2.html')


def help3(request):
    return render(request, 'accounts/help3.html')


def help4(request):
    return render(request, 'accounts/help4.html')


def question(request):
    return render(request, 'accounts/question.html')


def privacy(request):
    try:
        privacy = get_object_or_404(Privacy, user=request.user)
    except:
        privacy = -1
    if request.method == "POST":
        if privacy == -1:
            form = PrivacyForm(request.POST)
        else:
            form = PrivacyForm(request.POST, instance=privacy)
        if form.is_valid():
            privacy = form.save(commit=False)
            privacy.user = request.user
            privacy.save()
            return redirect("talk:chap_bridge", cn=1)
    else:
        if privacy == -1:
            form = PrivacyForm()
        else:
            form = PrivacyForm(instance=privacy)

    ctx = {"form": form, 'privacy': privacy}
    return render(request, "accounts/privacy_form.html", ctx)
