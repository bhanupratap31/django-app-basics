from django.urls import path
from django.conf.urls import include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name="hello-viewset")
router.register('profile', views.UserProfileViewSet)
router.register('login', views.LoginViewSet, base_name='login')
urlpatterns= [
    path('Hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls))
]

