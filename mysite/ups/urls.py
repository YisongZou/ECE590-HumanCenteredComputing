from django.urls import path
from .views import (
    ShipListView,
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)
from . import views

urlpatterns = [
    path('', views.home, name='ups-home'),
    path('shipments/', ShipListView.as_view(), name='shipments'),
    path('shipments/detail/<int:pkgId>/',
         views.shipdetail, name='shipments-detail'),
    path('search/', views.search, name='search'),
    path('searchdetail/', views.searchdetail, name='searchdetail'),
    path('editdestination/<int:pkgId>/',
         views.editdestination, name='editdestination'),
    path('editdestinationResult/', views.editdestinationResult,
         name='editdestinationResult'),
    path('addpackage/<int:pkId>/', views.addpackage, name='addpackage'),
    path('find_specialsts',  views.find_specialists, name='specialist'),
    path('reservation',  views.reservation, name='reservation'),
    path('reservation_success', views.reservation_success, name='reservation_success'),
     path('my_reservations', views.my_reservations, name='my_reservations'),
    path('blog/', PostListView.as_view(), name='post-home'),
    path('blog/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('blog/new/', PostCreateView.as_view(), name='post-create'),
    path('blog/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('blog/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('resources/', views.resources, name='resources'),
    path('rate/', views.moodRecord, name='mood'),
    path('profile/', views.search, name='profile'),
    path('sharemood/', views.shareMood, name='sharemood'),
    path('about/', views.about, name='about'),
]
