from django.shortcuts import render

from rest_framework import mixins
from rest_framework import generics

from .serializer import StockSerializer
from .models import Stock


class StockManager(mixins.ListModelMixin,
                mixins.CreateModelMixin,
                generics.GenericAPIView):
    """
    This API handles returning a filtered (or not filered) query set of stock and
    adding an validated entry to the the model.
    """

    serializer_class = StockSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Stock.objects.all()

        # checking filter options
        color = self.request.query_params.get('color', None)
        size = self.request.query_params.get('size', None)
        name = self.request.query_params.get('name', None)
        
        # filtering for color
        if color is not None:
            queryset = queryset.filter(color=color)

        # filtering for size
        if size is not None:
            queryset = queryset.filter(size=size)

        # filtering for size
        if name is not None:
            queryset = queryset.filter(name=name)


        return queryset

    # GET REQUEST
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    # POST REQUEST
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
