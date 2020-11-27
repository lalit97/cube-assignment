from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

from .models import Event
from .serializers import EventSerializer
from .utils import get_normalized_data

class EventCreateView(ListCreateAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()

    def post(self, request, *args, **kwargs):
        data = get_normalized_data(request.data)
        serializer = EventSerializer(data=data)
        if serializer.is_valid():
            event = serializer.save()
            return Response(
                EventSerializer(event).data,
                status=status.HTTP_201_CREATED 
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

