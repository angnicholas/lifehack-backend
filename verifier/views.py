from datetime import timedelta
import datetime
import pytz

from django.shortcuts import render
from django.utils import timezone
from django.db.models import Q

from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from collections import OrderedDict

from authapi.models import User
from authapi.permissions import CanSendVerifiers, CanViewVerifiers
from .serializers import VerifierSerializer

class VerifierView(APIView):
    
    class Send(generics.CreateAPIView):
        permission_classes = [CanSendVerifiers] # To review
        serializer_class = VerifierSerializer

        def post(self, request, format=None):
            return super().post(request, format)

    class List(generics.ListAPIView):
        permission_classes = [CanViewVerifiers] # To review
        serializer_class = VerifierSerializer

        def get(self, request, format=None):
            print(request.user)
            return super().get(request, format)


