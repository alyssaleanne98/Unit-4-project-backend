from django.shortcuts import get_object_or_404
from rest_framework.views import APIView #as super to your class
from rest_framework.response import Response #to send data to frontend
from rest_framework import status # to include status codes in your response
from .models import Cards
from django.http import HttpResponse
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


    def post(self, request):
    #     #Post request
        print(request.data)
    #     #format data for postgres
        cards = CardsSerializers(data=request.data)
        if cards.is_valid():
            cards.save()
            return Response(cards.data, status=status.HTTP_201_CREATED)
        else:
            return Response(cards.errors, status=status.HTTP_400_BAD_REQUEST)
    



class CardDetail(APIView):
    def get(self, request, pk):
        #Show request
        print(request)
        cards = get_object_or_404(Cards, pk=pk) #get book
        data = CardsSerializers(cards).data #format it
        return Response(data) #send it back
    
    def put(self, request, pk):
        #Update request
        print(request)
        cards = get_object_or_404(Cards, pk=pk)
        updated = CardsSerializers(cards, data=request.data, partial=True)
        if updated.is_valid():
            updated.save()
            return Response(updated.data)
        else: 
            return Response(updated.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        #Delete request
        print(request)
        cards = get_object_or_404(Cards, pk=pk)
        cards.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)