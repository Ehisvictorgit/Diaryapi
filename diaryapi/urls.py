from django.urls import path
from .views import Diaryview
from .views import Diarydetailview

urlpatterns = [
    path('diary/', Diaryview.as_view()),
    path('diary/<int:id>/', Diarydetailview.as_view()), 
]