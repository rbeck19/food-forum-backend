from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import status, generics
from rest_framework.response import Response

from ..models.comment import Comment
from ..serializers import CommentSerializer, CommentReadSerializer

class CommentsView(generics.ListCreateAPIView):
    """
    View Comments
    """
    serializer_class = CommentSerializer
    #INDEX
    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentReadSerializer(comments, many=True)
        return Response({'comments': serializer.data})
    #CREATE
    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# /comments/id
class CommentDetailView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    
    # SHOW
    def get(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        serializer = CommentReadSerializer(comment)
        return Response(serializer.data)
    #UPDATE
    def patch(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #DELETE
    def delete(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)