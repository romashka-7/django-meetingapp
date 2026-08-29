
from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.event_list, name="event_list"),
    path('create/', views.event_create, name="event_create"),
    path('event/<int:pk>', views.event_detail, name="event_detail"),
    path('event/<int:pk>/vote/', views.event_detail, name="event_detail_vote"),
]
