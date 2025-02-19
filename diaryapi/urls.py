from django.urls import path
from .views import Diaryview
from .views import Diarydetailview
from . import views

urlpatterns = [
    path('dairy',views.Diaryview.as_view()),
    path('diary/<int:id>/', views.Diarydetailview.as_view()), 
]