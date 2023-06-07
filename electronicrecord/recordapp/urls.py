from django.urls import path
from . import views
urlpatterns = [
    path('client/', views.getClient),
    path('client/add', views.add_client),
    path('specialist/', views.get_specialist),
    path('specialist/add', views.add_specialist)
 ]
