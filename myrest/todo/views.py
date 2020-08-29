from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ToDoItem
from .serialaizers import ToDoItemSerialaizer


def index_view(request):
    return HttpResponse('<h2>ToDo!</h2>')


class ToDoListView(APIView):

    def get(self, request):
        items = ToDoItem.objects.all()
        serializer = ToDoItemSerialaizer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ToDoItemSerialaizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ToDoDetailView(APIView):

    def get(self, request, pk):
        item = get_object_or_404(ToDoItem, pk=pk)
        serializer = ToDoItemSerialaizer(item)
        return Response(serializer.data)

    def delete(self, request, pk):
        item = get_object_or_404(ToDoItem, pk=pk)
        serializer = ToDoItemSerialaizer(item)
        data = serializer.data
        item.delete()
        return Response(data)
