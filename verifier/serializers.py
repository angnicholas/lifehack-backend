from django.forms import IntegerField
from rest_framework import serializers

from .models import Verifier
#from contact.serializers import ContactSerializer

class VerifierSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Verifier
        exclude = ['user_from',]
        read_only_fields = ('create_at', 'update_at')


class VerifierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Verifier
        fields = '__all__'
        read_only_fields = ('create_at', 'update_at')
