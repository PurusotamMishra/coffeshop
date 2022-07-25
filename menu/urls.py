from django.urls import path
from . import views

urlpatterns = [
    path('coffee', views.coffee, name='coffee'),
    path('tea', views.tea, name='tea'),
    path('cake', views.cake, name='cake')

]

