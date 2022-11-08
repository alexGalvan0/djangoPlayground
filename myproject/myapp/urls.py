from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    #path('<int:id>/',views.authors),
    path('<str:name>/', views.authBook)
]