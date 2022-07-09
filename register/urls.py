from django.urls import path

from .views import RegisterView

urlpatterns = [
    path('listinstitutions', RegisterView.ListInstitutions.as_view()),
    path('addinstitution', RegisterView.AddInstitution.as_view()),
    path('listendusers', RegisterView.ListEndUsers.as_view()),
]