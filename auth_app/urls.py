from django.urls import path 
from . import views
from .views import (
    PostListView,
    OtzivListView,
    StatistikaListView,
    TarifListView,
    PropListview,
    KabinetListView,
    OtzivDetail,
    NatijaListView,
    NatijaDetail,
    )


urlpatterns = [
    path('register/',views.register_view,name='register'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('dashboard/',views.dashboard_view,name='dashboard') , 
    path('', PostListView.as_view(), name='index'),
    path('otziv/', OtzivListView.as_view(), name='otziv'),
    path('statistika/', StatistikaListView.as_view(), name='statistika'),
    path('tarif/', TarifListView.as_view(), name='tarif'),
    path('prop-tredir/', PropListview.as_view(), name='prop-tredir'),
    path('kabinet/', KabinetListView.as_view(), name='kabinet'),
    path('otziv/<int:pk>/',OtzivDetail.as_view(), name='otziv_detail'),
    path('natija/', NatijaListView.as_view(), name='natija'),
    path('natija/<int:pk>/',NatijaDetail.as_view(), name='natija_detail'),
]

