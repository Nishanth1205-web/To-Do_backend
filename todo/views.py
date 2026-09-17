from django.shortcuts import render  # type: ignore[import-not-found]
from rest_framework import viewsets  # type: ignore[import-not-found]
from .serializers import TodoSerializer
from .models import Todo
# Create your views here.

class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()