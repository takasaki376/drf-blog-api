from .serializers import BlogSerializer
from .models import Blog
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def get_object(self):
        return self.request.user

class BlogListView(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = (AllowAny,)

    # insertを無効化する
    def create(self, serializer):
        response = {'message': 'INSERT method is not allowed'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    # deleteを無効化する
    def destroy(self, request, *args, **kwargs):
        response = {'message': 'DELETE method is not allowed'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    # updateを無効化する(全項目の更新)
    def update(self, request, *args, **kwargs):
        response = {'message': 'PATCH method is not allowed'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    # updateを無効化する(一部項目の更新)
    def partial_update(self, request, *args, **kwargs):
        response = {'message': 'PATCH method is not allowed'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)