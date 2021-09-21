from django.urls import path, include
from django.conf.urls import url
from . import views 


urlpatterns = [
    path('',views.index, name='index'),
    path('home',views.home, name='home'),
    path('homea',views.homea, name='homea'),
    path('homeu',views.homeu, name='homeu'),
    path('agence',views.agence, name='agence'),
    path('magence/<str:id>/',views.magence, name='magence'),
    path('dagence/<str:id>/',views.dagence),
    path('compte',views.compte, name='compte'),
    path('comptea',views.compte, name='comptea'),
    path('mcompte/<str:cid>/',views.mcompte, name='mcompte'),
    path('dcompte/<str:cid>/',views.dcompte),
    path('dashboard',views.dashboard, name='dashboard'),
    path('dashboarda',views.dashboarda, name='dashboarda'),
    path('dashboardu',views.dashboardu, name='dashboardu'),
    path('client-chart/', views.client_chart, name='client-chart'),
    path('att-chart/', views.att_chart, name='att-chart'),
    
]