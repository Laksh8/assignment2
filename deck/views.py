from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q

from .utils import build

from .models import Deck

@api_view(['GET'])
def probability_of_card(request):
    """
    Api function that can find the probability fro given constraints.
    assuming the key word to find the probability id "OR"
    """

    build()

    deck = Deck.objects.all()

    # checking filter options
    color = request.query_params.get('color', None)
    value = request.query_params.get('value', None)
    suit = request.query_params.get('suit', None)
    face = request.query_params.get('face', None)

    # filtering for color
    count = deck.filter(Q(color=color)| Q(value=value)|Q(face=face)|Q(suit=suit)).count()
    probability = count/52

    return Response({"probability":probability}, status=status.HTTP_200_OK)
