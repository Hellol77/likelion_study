from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import auth
import random
# Create your views here.

# 회원 가입
def signup(request):
    # signup 으로 POST 요청이 왔을 때, 새로운 유저를 만드는 절차를 밟는다.
    if request.method == 'POST':
        User = get_user_model()
        # password와 confirm에 입력된 값이 같다면
        if request.POST['username']:
            # user 객체를 새로 생성
            user = User.objects.create_user(user_id=request.POST['username'], password= str(random.randrange(10000000, 99999999)))
            # 로그인 한다
            auth.login(request, user)
            return redirect('./boodecorate')
    # signup으로 GET 요청이 왔을 때, 회원가입 화면을 띄워준다.
    return render(request, 'main/nickname.html')
