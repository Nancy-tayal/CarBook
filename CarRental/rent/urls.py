from django.urls import path
from . import views

urlpatterns =[
    path('rentcar/<str:pk>/', views.rentcar, name="rentcar"),
    path('successful/<str:pk>/', views.successful, name="successful"),
    path('history/', views.historylist.as_view(), name="history")
]
