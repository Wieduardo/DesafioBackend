from django.urls import path

from .views import ListCNABView, ListOneCNABView, ListAllStoreCNABView, ListBalanceStoreView

urlpatterns = [
    path("cnab/", ListCNABView.as_view()),
    path("cnab/<pk>/", ListOneCNABView.as_view()),
    path("cnab/cpf/<int:cpf>/", ListBalanceStoreView.as_view())
]
