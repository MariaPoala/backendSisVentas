from django.urls import path, include
from rest_framework import routers
from .views import HomeViewSet
from apps.admin.views import HomeViewSet
main_view = HomeViewSet.as_view({'get': 'main_view'})
router = routers.DefaultRouter()
urlpatterns = [
    path('', include(router.urls)),
    path('', main_view, name='/')
    # path('data-table-clientes/', ClienteViewSet.as_view({'post': 'list_datatable'})),
    ]
