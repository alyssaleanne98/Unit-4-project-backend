from django.urls import path
from .views import Cards, CardsDetail

urlpatterns = [
    path('', Cards.as_view(), name='cards'), 
    path('<int:pk>', CardsDetail.as_view(), name='cards_detail')
]