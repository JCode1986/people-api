from django.urls import path
from .views import PersonList, PersonDetail

urlpatterns = [
    path('posts/', PersonList.as_view(), name='person_list'),
    path('posts/<int:pk>/', PersonDetail.as_view(), name='person_detail')
]