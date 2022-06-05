from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('',views.home, name ='main'),
#    path('nickname',views.nickname, name ='nickname'),
    path('select_boo',views.select_boo, name ='select_boo'),
    path('select_country',views.select_country, name ='select_country'),
    path('decorate_boo',views.decorate_boo, name ='decorate_boo'),
    path('saveImage',views.canvasToImage, name ='screenshot'),
    path('worldmap',views.worldmap, name ='worldmap'),
    path('brazil_boo', views.brazil_boo, name='brazil_boo'),
    path('japan_boo', views.japan_boo, name='japan_boo'),
    path('china_boo', views.china_boo, name='china_boo'),
    path('india_boo', views.india_boo, name='india_boo'),
    path('indonesia_boo', views.indonesia_boo, name='indonesia_boo'),
    path('spain_boo', views.spain_boo, name='spain_boo'),
]