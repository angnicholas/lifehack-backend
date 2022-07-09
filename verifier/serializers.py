
from django.forms import IntegerField
from rest_framework import serializers

from .models import Verifier
#from contact.serializers import ContactSerializer

class VerifierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Verifier
        fields = '__all__'
        read_only_fields = ('create_at', 'update_at')
