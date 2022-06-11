from django.shortcuts import render, redirect
from users.decorators import login_message_required
from users.models import User
from .forms import CountryWriteForm, ImageForm
import random, base64, os
from django.http import JsonResponse
from django.conf import settings
from .models import Image, Country
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

def home(request):
    return render(request, 'main/index.html')

#@login_message_required
def select_boo(request):
    return render(request, 'main/select_boo.html')

#@login_message_required
@method_decorator(csrf_exempt)
def select_country(request):
    if request.method == 'POST':
        form = CountryWriteForm(request.POST)
        user = request.user

        if request.POST["send"] == "0":
            if Country.objects.all().filter(nickname = user):
                del_board = Country.objects.get(nickname=user)
                del_board.delete()
                country = form.save(commit = False)
                country.nickname = User.objects.get(user_id=user)
                country.country = '인도'
                country.save()
                return render(request, 'main/decorate_boo.html')
            else:
                country = form.save(commit = False)
                country.nickname = User.objects.get(user_id=user)
                country.country = '인도'
                country.save()
                return render(request, 'main/decorate_boo.html')
            
        elif request.POST["send"] == "1":
            if Country.objects.all().filter(nickname = user):
                del_board = Country.objects.get(nickname=user)
                del_board.delete()
                country = form.save(commit = False)
                country.nickname = User.objects.get(user_id=user)
                country.country = '인도네시아'
                country.save()
                return render(request, 'main/decorate_boo.html')
            else:
                country = form.save(commit = False)
                country.nickname = User.objects.get(user_id=user)
                country.country = '인도네시아'
                country.save()
                return render(request, 'main/decorate_boo.html')

        elif request.POST["send"] == "2":
            if Country.objects.all().filter(nickname = user):
                del_board = Country.objects.get(nickname=user)
                del_board.delete()
                country = form.save(commit = False)
                country.nickname = User.objects.get(user_id=user)
                country.country = '일본'
                country.save()
                return render(request, 'main/decorate_boo.html')
            else:
                country = form.save(commit = False)
                country.nickname = User.objects.get(user_id=user)
                country.country = '일본'
                country.save()
                return render(request, 'main/decorate_boo.html')

        elif request.POST["send"] == "3":
            if Country.objects.all().filter(nickname = user):
                del_board = Country.objects.get(nickname=user)
                del_board.delete()
                country = form.save(commit = False)
                country.nickname = User.objects.get(user_id=user)
                country.country = '브라질'
                country.save()
                return render(request, 'main/decorate_boo.html')
            else:
                country = form.save(commit = False)
                country.nickname = User.objects.get(user_id=user)
                country.country = '브라질'
                country.save()
                return render(request, 'main/decorate_boo.html')

        elif request.POST["send"] == "4":
            if Country.objects.all().filter(nickname = user):
                del_board = Country.objects.get(nickname=user)
                del_board.delete()
                country = form.save(commit = False)
                country.nickname = User.objects.get(user_id=user)
                country.country = '중국'
                country.save()
                return render(request, 'main/decorate_boo.html')
            else:
                country = form.save(commit = False)
                country.nickname = User.objects.get(user_id=user)
                country.country = '중국'
                country.save()
                return render(request, 'main/decorate_boo.html')

        elif request.POST["send"] == "5":
            if Country.objects.all().filter(nickname = user):
                del_board = Country.objects.get(nickname=user)
                del_board.delete()
                country = form.save(commit = False)
                country.nickname = User.objects.get(user_id=user)
                country.country = '스페인'
                country.save()
                return render(request, 'main/decorate_boo.html')
            else:
                country = form.save(commit = False)
                country.nickname = User.objects.get(user_id=user)
                country.country = '스페인'
                country.save()
                return render(request, 'main/decorate_boo.html')

    return render(request, 'main/select_country.html')

#@login_message_required
def decorate_boo(request):
    return render(request, 'main/decorate_boo.html')

def worldmap(request):
    return render(request, 'main/worldmap.html')

@csrf_exempt
def canvasToImage(request):
    data = request.POST.__getitem__('data')
    data = data[22:]        # 앞의 'data:image/png;base64'부분을 제거
    number = random.randrange(1,10000)    # 동시에 다른 사용자가 접근시 최대한 중복을 막기위함.

    path = str(os.path.join(settings.MEDIA_ROOT, 'images/'))
    filename = 'image' + str(number) + '.png'

  # "wb"(즉, 바이너리파일 쓰기전용)으로 파일을 open
    image = open(path+filename, "wb")
  # `base64.b64decode()`를 통하여 디코딩을 하고 파일에 써준다.
    image.write(base64.b64decode(data))
    image.close()

    user = request.user
    if Image.objects.all().filter(nickname = user):
        del_board = Image.objects.get(nickname=user)
        del_board.delete()
        form = ImageForm(request.POST)
        country = form.save(commit = False)
        country.nickname = User.objects.get(user_id=user)
        country.image = 'images/'+filename
        country.save()

    else:
        form = ImageForm(request.POST)
        country = form.save(commit = False)
        country.nickname = User.objects.get(user_id=user)
        country.image = 'images/'+filename
        country.save()

  # filename을 json형식에 맞추어 response를 보내준다.
    answer = {'filename': filename}
    return JsonResponse(answer)

def brazil_boo(request):
    country = Country.objects.filter(country = '브라질').all()
    num = len(country)

    a = Country.objects.filter(country = '브라질').values_list()
    b = Image.objects.values_list()

    image = []

    for i in range(num):
        for j in range(len(b)):
            if a[i][1] == b[j][1]:
                image.append((b[j][0]))

    image = Image.objects.filter(pk__in=image)
    count = len(image)

    r = (count+3)//4
    r_dict = {}
    for i in range(r):
        r_dict[4*i] = 4*i+4

    return render(request, 'main/Brazil_BOO.html', {'image':image,'count':count, 'r_dict':r_dict})

def japan_boo(request):
    country = Country.objects.filter(country = '일본').all()
    num = len(country)

    a = Country.objects.filter(country = '일본').values_list()
    b = Image.objects.values_list()

    image = []

    for i in range(num):
        for j in range(len(b)):
            if a[i][1] == b[j][1]:
                image.append((b[j][0]))

    image = Image.objects.filter(pk__in=image)
    count = len(image)

    r = (count+3)//4
    r_dict = {}
    for i in range(r):
        r_dict[4*i] = 4*i+4

    return render(request, 'main/Japan_BOO.html', {'image':image,'count':count, 'r_dict':r_dict})

def china_boo(request):
    country = Country.objects.filter(country = '중국').all()
    num = len(country)

    a = Country.objects.filter(country = '중국').values_list()
    b = Image.objects.values_list()

    image = []

    for i in range(num):
        for j in range(len(b)):
            if a[i][1] == b[j][1]:
                image.append((b[j][0]))

    image = Image.objects.filter(pk__in=image)
    count = len(image)

    r = (count+3)//4
    r_dict = {}
    for i in range(r):
        r_dict[4*i] = 4*i+4    

    return render(request, 'main/China_BOO.html', {'image':image,'count':count, 'r_dict':r_dict})

def india_boo(request):
    country = Country.objects.filter(country = '인도').all()
    num = len(country)

    a = Country.objects.filter(country = '인도').values_list()
    b = Image.objects.values_list()

    image = []

    for i in range(num):
        for j in range(len(b)):
            if a[i][1] == b[j][1]:
                image.append((b[j][0]))

    image = Image.objects.filter(pk__in=image)
    count = len(image)

    r = (count+3)//4
    r_dict = {}
    for i in range(r):
        r_dict[4*i] = 4*i+4

    return render(request, 'main/India_BOO.html', {'image':image,'count':count, 'r_dict':r_dict})

def indonesia_boo(request):
    country = Country.objects.filter(country = '인도네시아').all()
    num = len(country)

    a = Country.objects.filter(country = '인도네시아').values_list()
    b = Image.objects.values_list()

    image = []

    for i in range(num):
        for j in range(len(b)):
            if a[i][1] == b[j][1]:
                image.append((b[j][0]))

    image = Image.objects.filter(pk__in=image)
    count = len(image)

    r = (count+3)//4
    r_dict = {}
    for i in range(r):
        r_dict[4*i] = 4*i+4

    return render(request, 'main/Indonesia_BOO.html', {'image':image,'count':count, 'r_dict':r_dict})

def spain_boo(request):
    country = Country.objects.filter(country = '스페인').all()
    num = len(country)

    a = Country.objects.filter(country = '스페인').values_list()
    b = Image.objects.values_list()

    image = []

    for i in range(num):
        for j in range(len(b)):
            if a[i][1] == b[j][1]:
                image.append((b[j][0]))

    image = Image.objects.filter(pk__in=image)
    count = len(image)

    r = (count+3)//4
    r_dict = {}
    for i in range(r):
        r_dict[4*i] = 4*i+4

    return render(request, 'main/Spain_BOO.html', {'image':image,'count':count, 'r_dict':r_dict})


def boodecorate(request):
    return render(request, 'main/boodecorate.html')