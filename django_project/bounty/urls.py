from django.contrib import admin
from django.urls import path
from .views import ( BountyListView, 
                        BountyCreateView, 
                        BountyDetailView, 
                        UserBountyListView, 
                        BountyUpdateView, 
                        BountyDeleteView, 
                        CompletionCreateView, 
                        CompletionDetailView,
                        CompletionDeleteView )
from . import views

urlpatterns = [
    path('', BountyListView.as_view(),name="bounty-home"),
    path("about", views.about, name="bounty-about"),
    path('user/<str:username>/', UserBountyListView.as_view(),name="user-bounties"),
    path("bounty/new/", BountyCreateView.as_view(),name="bounty-create"),
    path("bounty/<int:pk>/", BountyDetailView.as_view(),name="bounty-detail"),
    path("bounty/<int:pk>/update/", BountyUpdateView.as_view(),name="bounty-update"),
    path("bounty/<int:pk>/delete/", BountyDeleteView.as_view(),name="bounty-delete"),
    path("completion/new/(?P<int:bounty>\d+)/", CompletionCreateView.as_view(),name="completion-create"),
    path("completion/<int:pk>/", CompletionDetailView.as_view(),name="completion-detail"),
    path("completion/<int:pk>/delete/", CompletionDeleteView.as_view(),name="completion-delete"),
]