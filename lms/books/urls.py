from django.urls import path
from.import views

urlpatterns = [
    path('',views.index, name='book_list'),
    path('create', views.create, name='book_create'),
    path('<int:id>',views.view,name='book_detail')
]