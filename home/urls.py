from django.urls import path, include
from .import views
from . import api

app_name = 'home'


urlpatterns = [
    
    path('', views.all_older , name='home'),
    path('creat/', views.creat_ , name='creat'),
    path('order/', views.creat_Por , name='creat_Por'),


    #API_LINKS single_pord
    path('api/list',api. Pro_list , name='api_por'),
    path('api/list/<int:id>',api.single_pord , name='single_pord'),
    path('api/list/tag',api.Tag_list , name='Tag_list'),

    # class based views
    path('api/list/v/',api.Por_list_generics.as_view() , name='Por_list_generics'),

    # class based views 
    path('api/list/v/<int:id>',api.Por_list_genericsCRUD.as_view() , name='Por_list_generics'),



]
