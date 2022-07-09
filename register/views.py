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
from authapi.serializers import UserSerializer
from authapi.permissions import IsInstitution, IsEndUser, IsInstitutionOrEndUser

class RegisterView(APIView):
    
    class AddInstitution(generics.CreateAPIView):
        permission_classes = [IsEndUser] # To review
        #serializer_class = VerifierSerializerCreate

        def post(self, request, format=None):  
            user = User.objects.get(pk=request.user.pk)
            
            institution_user_id = request.data.get('institution_id', False)
            if not institution_user_id:
                return Response('No Institution ID specified!', status=status.HTTP_400_BAD_REQUEST)
            try:
                institution_user = User.objects.get(pk=institution_user_id)
            except:
                return Response(
                    f'Institution with id {institution_user_id} is not found.', 
                    status=status.HTTP_404_NOT_FOUND
                )

            user.registered_institutions.add(institution_user)
            return Response('Institution Added successfully.', status=status.HTTP_200_OK)
            

    class ListInstitutions(generics.ListAPIView):
        permission_classes = [IsInstitutionOrEndUser] # To review
        serializer_class = UserSerializer
        
        def get(self, request, format=None):

            queryset = User.objects.filter(role='IN')
            serializer = self.get_serializer(queryset, many=True)
            
            return Response(serializer.data)


    class ListEndUsers(generics.ListAPIView):
        permission_classes = [IsInstitution] # To review
        serializer_class = UserSerializer

        def get(self, request, format=None):
            institution_user = User.objects.get(pk=request.user.pk)
            queryset = User.objects.filter(registered_institutions=institution_user)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)



