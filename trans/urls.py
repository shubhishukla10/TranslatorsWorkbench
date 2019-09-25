from django.urls import path
from . import views

urlpatterns = [
        path('post/trans/', views.post_trans, name = 'post_trans'),
        path('post/hello', views.post_hello, name = 'post_hello'),
]
