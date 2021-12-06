from django.urls import path
from home import views


urlpatterns = [
    path('', views.index, name='index'),
    path('billview/', views.get_Bill, name='billview'),
]
