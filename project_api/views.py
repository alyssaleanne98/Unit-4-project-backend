from django.shortcuts import render
from rest_framework.views import APIView #as super to your class
from rest_framework.response import Response #to send data to frontend
from rest_framework import status # to include status codes in your response
from .models import Cards


# Create your views here.


class Cards(APIView):
    pass

class CardsDetail(APIView):
    pass