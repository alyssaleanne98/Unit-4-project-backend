from django.urls import path
from .views import Card, CardDetail

urlpatterns = [
    path('', Card.as_view(), name='card'), 
    path('<int:pk>', CardDetail.as_view(), name='card_detail')
]