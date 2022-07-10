from django.urls import path

from .views import RegisterView

urlpatterns = [
    path('listallinstitutions', RegisterView.ListAllInstitutions.as_view()),
    path('listmyinstitutions', RegisterView.ListMyInstitutions.as_view()),
    path('deleteinstitution', RegisterView.DeleteInstitution.as_view()),
    path('addinstitution', RegisterView.AddInstitution.as_view()),
    path('listendusers', RegisterView.ListEndUsers.as_view()),
]