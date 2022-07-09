from django.urls import path

from .views import RegisterView

urlpatterns = [
    path('listinstitutions', RegisterView.ListInstitutions.as_view()),
    path('', RegisterView.Register.as_view()),
]