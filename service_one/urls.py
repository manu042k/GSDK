from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'randommodel', views.RandomModelViewSet, basename='randommodel')


urlpatterns = [
    # path('', views.index, name='index'),
] +router.urls