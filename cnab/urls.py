from django.urls import path

from .views import ListCNABView, ListOneCNABView, ListAllStoreCNABView

urlpatterns = [
    path("cnab/", ListCNABView.as_view()),
    path("cnab/<pk>/", ListOneCNABView.as_view()),
    path("cnab/cpf/<int:cpf>/", ListAllStoreCNABView.as_view())
]
