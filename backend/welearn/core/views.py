from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from core.models import Room, RoomCategory


class RoomCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomCategory
        fields = ('pk', 'caption')  # pk serializing doesn't seem to work but for now let just filter by caption


class RoomSerializer(serializers.ModelSerializer):
    category = RoomCategorySerializer(many=False)

    class Meta:
        model = Room
        fields = ('pk','caption', 'description', 'limit', 'start', 'end', 'category',
                  'members', 'lon', 'lat', 'storey', 'building_name', 'room_number')

    def validate_category(self, value):
        room_category = RoomCategory.objects.get(caption=value.get('caption'))
        if room_category is None:
            raise serializers.ValidationError("Room with %s caption does not exist!" % value.get('caption', None))
        return room_category


@api_view(['GET', 'POST'])
def rooms_list(request):
    if request.method == 'GET':
        rooms = Room.objects.all()

        range = request.query_params.get('range', None)
        if range is not None:
            location_lon = request.query_params.get('location_lon', None)
            location_lat = request.query_params.get('location_lat', None)
            if location_lat is not None and location_lon is not None:
                rooms = rooms.filter(lon__gte=location_lon - range,
                                     lon__lte=location_lon + range,
                                     lat__gte=location_lat - range,
                                     lat__lte=location_lat + range)

        category_filter = request.query_params.get('category', None)
        if category_filter is not None:
            rooms = rooms.filter(category__pk=category_filter.get('pk'))

        serializer = RoomSerializer(rooms, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        print(request.data)
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE', 'PUT'])
def room_detail(request, pk):

    try:
        room = Room.objects.get(pk=pk)
    except Room.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RoomSerializer(room)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        room.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = RoomSerializer(room, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def categories_list(request):

    if request.method == 'GET':
        serializer = RoomCategorySerializer(RoomCategory.objects.all(), many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RoomCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE', 'PUT'])
def categories_detail(request, pk):
    try:
        category = RoomCategory.objects.get(pk=pk)
    except RoomCategory.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = RoomCategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
