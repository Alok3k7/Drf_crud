from django.core.serializers import serialize
from django.http import JsonResponse
from .models import Drf_Curd
from .serializers import Drf_curdSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def Drf_curd_list(request,formate=None):
    if request.method == 'GET':
        drf_curd = Drf_Curd.objects.all()
        serializer = Drf_curdSerializer(drf_curd, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = Drf_curdSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def Drf_curd_detail(request, id):
    try:
        Drf_curd = Drf_Curd.objects.get(pk=id)
    except Drf_Curd.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = Drf_curdSerializer(Drf_curd)
        return Response(serializer.data)


    elif request.method == 'PUT':
        serializer = Drf_curdSerializer(Drf_curd, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    elif request.method == "DELETE":
        Drf_curd.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
