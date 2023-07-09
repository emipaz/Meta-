from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter, BaseRouter
from . import views


router = DefaultRouter(trailing_slash=False)
router.register('libros_v2', views.LibrosViewset, basename='libros2')
router.register('libros_v3', views.LibrosModelViewset, basename='libros3')

urlpatterns = [
    path('libros', views.libros),
    path('libro/<int:pk>', views.LibroView.as_view()),
    path('libroGen/<int:pk>', views.LibroViewGeneric.as_view()),
    path('categoria/<int:pk>', views.categoria_detail, name='categoria-detail'),
    path('', include(router.urls))
]