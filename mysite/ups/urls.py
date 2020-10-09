from django.urls import path
from .views import ShipListView
from . import views

urlpatterns = [
    path('', views.home, name='ups-home'),
    path('shipments/', ShipListView.as_view(), name='shipments'),
    path('shipments/detail/<int:pkgId>/', views.shipdetail, name='shipments-detail'),
    path('search/', views.search, name='search'),
    path('searchdetail/', views.searchdetail, name='searchdetail'),
    path('editdestination/<int:pkgId>/', views.editdestination, name='editdestination'),
    path('editdestinationResult/', views.editdestinationResult, name='editdestinationResult'),
    path('addpackage/<int:pkId>/', views.addpackage, name='addpackage'),
]
