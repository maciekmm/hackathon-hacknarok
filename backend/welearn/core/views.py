from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from rest_framework import serializers, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework_jwt.views import ObtainJSONWebToken

from core.models import Room, RoomCategory, Profile


class RoomCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomCategory
        fields = ('pk', 'caption')  # pk serializing doesn't seem to work but for now let just filter by caption


class RoomSerializer(serializers.ModelSerializer):
    category = RoomCategorySerializer(many=False)

    class Meta:
        model = Room
        fields = ('pk', 'caption', 'description', 'limit', 'start', 'end', 'category',
                  'members', 'lon', 'lat', 'storey', 'building_name', 'room_number')

    def validate_category(self, value):
        room_category = RoomCategory.objects.get(caption=value.get('caption'))
        if room_category is None:
            raise serializers.ValidationError("Room with %s caption does not exist!" % value.get('caption', None))
        return room_category


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('pk', 'bio', 'lon', 'lat', 'building_name', 'room_number')


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(many=False)

    class Meta:
        model = User
        fields = ('pk', 'profile', 'username', 'first_name', 'last_name', 'email')


@api_view(['GET', 'POST'])
def rooms_list(request):
    if request.method == 'GET':
        print("Whatever")

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
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def users_list(request):
    if request.method == 'GET':
        serializer = UserSerializer(User.objects.all(), many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def users_details(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(data=serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ObtainJWTToken(ObtainJSONWebToken):

    # UTTERLY UGLY!
    def post(self, request, *args, **kwargs):
        jwt_response = super(ObtainJWTToken, self).post(request, *args, **kwargs)
        user = User.objects.get(username=request.data.get('username'))

        # print(UserSerializer(user).data)
        u_serializer_data = UserSerializer(user).data
        resp_serializer_data = jwt_response.data

        response_data = {**u_serializer_data, **resp_serializer_data}
        return Response(data=response_data)
