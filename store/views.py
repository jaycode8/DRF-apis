from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser,MultiPartParser, FormParser

from .models import eBooks, authors, test, test4
from .serializers import BookSerializer, AuthorsSerializer, testSerializer, test4Serializer
# Create your views here.

@api_view(['GET'])
def home(req):
    return Response({'msg':"Welcome.... this is the home route"})

# ----------------------- Books Views ---------------------------

def addBook(req):
    serializer = BookSerializer(data=req.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"eBook":serializer.data})
    return Response({"msg":serializer.errors})

def allBooks(req):
    books = eBooks.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response({"message":serializer.data})

def specificBook(req, book):
    serializer = BookSerializer(book)
    return Response({"Book":serializer.data})

def updateBook(req, book):
    serializer = BookSerializer(book, data=req.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message":"successfully updated the book", "book":serializer.data})
    return Response({"errors":serializer.errors, "data":serializer.data})

def patchBook(req, book):
    serializer = BookSerializer(book, data=req.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({"message":"successfully patched the book", "book":serializer.data})
    return Response({"errors":serializer.errors, "data":serializer.data})

def deleteBook(req, book):
    title = BookSerializer(book).data['title']
    book.delete()
    return Response({"message":f"{title} was deleted successfully"})

@api_view(['GET', 'POST'])
def book_view(req):
    if req.method == 'GET':
        return allBooks(req)
    if req.method == 'POST':
        return addBook(req)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def book_view2(req):
    id = req.query_params.get('id')
    try:
        book = eBooks.objects.get(_id=id)
    except eBooks.DoesNotExist:
        return Response({"message":"The requested book does not exist"})
    if req.method == 'GET':
        return specificBook(req, book)
    if req.method == 'PUT':
        return updateBook(req, book)
    if req.method == 'PATCH':
        return patchBook(req, book)
    if req.method == 'DELETE':
        return deleteBook(req, book)
    return Response({"message":f"ecpected PATCH but received {req.method}"})

# ---------------------------- Authors Views --------------------------------------------

def addAuthor(req):
    serializer = AuthorsSerializer(data=req.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"Auyhor":serializer.data})
    return Response({"msg":serializer.errors})

def allAuthors(req):
    author = authors.objects.all()
    serializer = AuthorsSerializer(author, many=True)
    return Response({"message":serializer.data})

def specificAuthor(req, author):
    serializer = AuthorsSerializer(author)
    return Response({"Author":serializer.data})

def updateAuthor(req, author):
    serializer = AuthorsSerializer(author, data=req.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message":"successfully updated the author", "author":serializer.data})
    return Response({"errors":serializer.errors, "data":serializer.data})

def patchAuthor(req, author):
    serializer = AuthorsSerializer(author, data=req.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({"message":"successfully patched the author", "author":serializer.data})
    return Response({"errors":serializer.errors, "data":serializer.data})

def deleteAuthor(req, author):
    name = AuthorsSerializer(author).data['name']
    author.delete()
    return Response({"message":f"{name} was deleted successfully"})

@api_view(['GET', 'POST'])
def author_view(req):
    if req.method == 'GET':
        return allAuthors(req)
    if req.method == 'POST':
        return addAuthor(req)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def author_view2(req):
    id = req.query_params.get('id')
    try:
        author = authors.objects.get(_id=id)
    except authors.DoesNotExist:
        return Response({"message":"The requested book does not exist"})
    if req.method == 'GET':
        return specificAuthor(req, author)
    if req.method == 'PUT':
        return updateAuthor(req, author)
    if req.method == 'PATCH':
        return patchAuthor(req, author)
    if req.method == 'DELETE':
        return deleteAuthor(req, author)
    return Response({"message":f"ecpected PATCH but received {req.method}"})

def test_get_view(req):
    id = req.query_params.get('id')
    return Response({"message":"this is a get request called on another method", "id":id})

def test_post_view(req):
    serializer = test4Serializer(data=req.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message":serializer.data, "data":'file'})
    return Response({"message":"this is a post request called through another method", "errors":serializer.errors})


@api_view(['GET', 'POST', 'PUT'])
def test(req):
    if req.method == 'GET':
        return test_get_view(req)
    if req.method == 'POST':
        return test_post_view(req)
    else:
        return Response({"message":req.method})
