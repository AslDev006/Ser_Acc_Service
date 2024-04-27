from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .bot import get_post
from .models import *
from .serializers import *


class ContactCreateView(APIView):
    def post(self, request, format=None):
        serializer = Contact_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            get_post(serializer.data)
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CalledContactView(APIView):
    def get(self, request, format=None):
        called = Contact_Model.objects.filter(called="Bog'lanildi")
        serializer = Contact_Serializer(called, many=True)
        return Response(serializer.data)

class UnCalledContactView(APIView):
    def get(self, request, format=None):
        called = Contact_Model.objects.filter(called="Bog'lanilmadi")
        serializer = Contact_Serializer(called, many=True)
        return Response(serializer.data)

class AllContactView(APIView):
    def get(self, request, format=None):
        service = Contact_Model.objects.all()
        serializer = Contact_Serializer(service, many=True)
        return Response(serializer.data)

class ContactDetailView(APIView):

    def get_object(self, pk):
        try:
            return Contact_Model.objects.get(pk=pk)
        except Contact_Model.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
            conatct = self.get_object(pk)
            serializer = Contact_Serializer(conatct)
            return Response(serializer.data)

    def put(self, request, pk, format=None):
            conatct = self.get_object(pk)
            serializer = Contact_Serializer(conatct, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
            conatct = self.get_object(pk)
            serializer = Contact_Serializer(conatct,
                                               data=request.data,
                                               partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
            conatct = self.get_object(pk)
            conatct.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)