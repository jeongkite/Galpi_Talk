from django.contrib.auth import authenticate, login
from django.core.checks import messages
from django.shortcuts import render, redirect
from accounts.forms import UserForm
from accounts.models import AccessCode


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
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username,
                                    password=raw_password)  # 사용자 인증
                access_code.is_used = True
                access_code.save()
                form.save()
                login(request, user)  # 로그인

                return redirect('accounts:intro')
    else:
        form = UserForm()
    return render(request, 'accounts/signup.html', {'form': form})


def intro(request):
    return render(request, 'accounts/intro.html')
