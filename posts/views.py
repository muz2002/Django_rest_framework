from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Post
from .serializers import PostSerializer
from django.shortcuts import get_object_or_404


@api_view(http_method_names=["GET", "POST"])
def homepage(request: Request):
    if request.method == "POST":
        data = request.data
        response = {"data": data}
        return Response(data=response, status=status.HTTP_201_CREATED)
    response = {"message": "Hello"}
    return Response(data=response, status=status.HTTP_200_OK)


@api_view(http_method_names=["GET", "POST"])
def list_posts(request: Request):
    posts = Post.objects.all()
    if request.method == "POST":
        data = request.data
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {"message": "Post Created", "data": serializer.data}
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    serializer = PostSerializer(instance=posts, many=True)
    response = {"message": "posts", "data": serializer.data}

    return Response(data=response, status=status.HTTP_200_OK)


@api_view(http_method_names=["GET"])
def post_detail(request: Request, post_id: int):
    post = get_object_or_404(Post, pk=post_id)
    serializer = PostSerializer(instance=post)

    response = {"message": " post ", "data": serializer.data}

    return Response(data=response, status=status.HTTP_200_OK)


@api_view(http_method_names=["PUT"])
def update_post(request: Request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    data = request.data
    serializer = PostSerializer(instance=post, data=data)
    if serializer.is_valid():
        serializer.save()
        response = {"message": "Successfully Updated", "data": serializer.data}
        return Response(data=response, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(http_method_names=["DELETE"])
def post_delete(request: Request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
