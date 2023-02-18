from django.shortcuts import render
from rest_framework.views import APIView #as super to your class
from rest_framework.response import Response #to send data to frontend
from rest_framework import status # to include status codes in your response
from .models import Cards
from rest_framework import status #to include status codes in your response
from .serializers import CardsSerializers #to format data to and from the database, enforces schema

# Create your views here.

# class Card
#  GET     /card - index
#  POST    /card - create

# class  (CardDetail) - use primary key (pk) as argument to access id

#  GET     /card/:id - show
#  PUT     /card/:id - update
#  DELETE  /card/:id - delete

class Card(APIView):
    def get(self, request):
        #Index request
        print(request)
        #Get all cards from card table
        card = Cards.objects.all()
        #Use serializer to format table data to JSON
        data = CardsSerializers(card, many=True).data
        return Response(data)

class CardDetail(APIView):
    pass