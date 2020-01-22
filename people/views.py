from rest_framework import generics
from .models import People
from .serializers import PersonSerializer
from .permissions import IsAuthorOrReadOnly

class PersonList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = People.objects.all()
    serializer_class = PersonSerializer

class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = People.objects.all()
    serializer_class = PersonSerializer
