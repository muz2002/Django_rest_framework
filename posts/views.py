from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status


class PostViewSet(viewsets.ViewSet):
    def list(self, request: Request):
        queryset = Post.objects.all()
        serializer = PostSerializer(instance=queryset, many=True)
        return Response(data=serializer.data)

    def retrieve(self, request: Request, pk):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(instance=post)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    # This piece of code is For viewsets.ModelViewSet
    # queryset = Post.objects.all()
    # serializer_class = PostSerializer
