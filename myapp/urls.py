from django.urls import path
from . import views 

app_name = 'myapp'
urlpatterns = [
    path('events/', views.EventCreateView.as_view(), name='events'),
]
