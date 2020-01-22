from django.urls import path
from .views import PersonList, PersonDetail

urlpatterns = [
    path('person/', PersonList.as_view(), name='person_list'),
    path('person/<int:pk>/', PersonDetail.as_view(), name='person_detail')
]