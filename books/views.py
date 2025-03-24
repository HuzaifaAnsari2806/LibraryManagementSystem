from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Book
from .serializer import BookSerializer, StudentViewSerializer


class AdminAPIs(APIView):
    serializer_class = BookSerializer

    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            try:
                book = Book.objects.get(pk=pk)
                serializer = self.serializer_class(book)
                return Response({"error": False, "data": serializer.data}, status=200)
            except:
                return Response(
                    {"error": True, "message": f"Book with id {pk} does not exist."},
                    status=400,
                )
        else:
            books = Book.objects.all()
            serializer = self.serializer_class(books, many=True)
            return Response({"error": False, "data": serializer.data}, status=200)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"error": False, "message": "Book stored successfully!"}, status=201
            )
        return Response({"error": True, "message": serializer.errors}, status=400)

    def put(self, request, pk, *args, **kwargs):
        data = request.data
        try:
            book = Book.objects.get(pk=pk)
            serializer = self.serializer_class(book, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"error": False, "message": "Book updated successfully!"},
                    status=200,
                )
            return Response({"error": True, "message": serializer.errors}, status=400)
        except:
            return Response(
                {"error": True, "message": f"Book with id {pk} does not exist."},
                status=400,
            )

    def delete(self, request, pk, *args, **kwargs):
        try:
            book = Book.objects.get(pk=pk)
            book.delete()
            return Response(
                {"error": False, "message": "Book deleted successfully!"}, status=204
            )
        except:
            return Response(
                {"error": True, "message": f"Book with id {pk} does not exist."},
                status=400,
            )


class StudentAPI(APIView):
    serializer_class = StudentViewSerializer

    def get(self, request, *args, **kwargs):
        books = Book.objects.all()
        serializer = self.serializer_class(books, many=True)
        return Response({"error": False, "data": serializer.data}, status=200)
