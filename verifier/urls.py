from django.urls import path

from .views import VerifierView

urlpatterns = [
    #Patterns for technician dashboard views
    path('send', VerifierView.Send.as_view()), 
    path('', VerifierView.List.as_view()),
]