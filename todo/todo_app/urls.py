from django.urls import path 
from . import views

urlpatterns = [
    path('',views.index,name = "todo"),
    path('task_update/<str:primaryKey>/',views.taskUpdate,name="task_update"),
    path('confirm/<str:primaryKey>/',views.confirmDel,name="confirm")
]