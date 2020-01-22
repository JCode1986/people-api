from rest_framework import generics
from .models import People
from .serializers import PersonSerializer

class PersonList(generics.ListCreateAPIView):
    queryset = People.objects.all()
    serializer_class = PersonSerializer

class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = People.objects.all()
    serializer_class = PersonSerializer
