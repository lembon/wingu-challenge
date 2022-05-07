from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

reclamo_lista = views.ReclamoViewSet.as_view({'get': 'list',})
reclamo_alta = views.ReclamoViewSet.as_view({'post': 'create',})
reclamo_baja = views.ReclamoViewSet.as_view({'delete': 'destroy',})
reclamo_edicion = views.ReclamoViewSet.as_view({'put': 'update',})

urlpatterns = [
    path('reclamos/', reclamo_lista, name='reclamo-lista'),
    path('reclamos/alta', reclamo_alta, name='reclamo-alta'),
    path('reclamos/baja/<int:pk>/', reclamo_baja, name='reclamo-baja'),
    path('reclamos/edicion/<int:pk>/', reclamo_edicion, name='reclamo-edicion'),
]

urlpatterns = format_suffix_patterns(urlpatterns)