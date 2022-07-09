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
from authapi.permissions import IsInstitution, IsInstitutionOrEndUser
from .serializers import VerifierSerializer, VerifierSerializerCreate
from .models import Verifier

class VerifierView(APIView):
    
    class Send(generics.CreateAPIView):
        permission_classes = [IsInstitution] # To review
        serializer_class = VerifierSerializerCreate

        def post(self, request, format=None):  
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                svd = serializer.validated_data
                user_to_send_to = User.objects.get(pk=svd['user_to'].pk)
                me = User.objects.get(pk=request.user.pk)

                if not me.can_send_to_user(user_to_send_to):
                    return Response('Can only send a code to an end user that is registered!')

                svd['user_from'] = me

                Verifier.objects.create(**svd)
                return Response('Created.', status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            

    class List(generics.ListAPIView):
        permission_classes = [IsInstitutionOrEndUser] # To review
        serializer_class = VerifierSerializer
        
        def get(self, request, format=None):

            user = User.objects.get(pk=request.user.pk)
            queryset = Verifier.objects.filter(user_to=user)
            serializer = self.get_serializer(queryset, many=True)
            
            return Response(serializer.data)


