from .serializers import PaintSerializer
from .models import Paint
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status


class PaintView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        posts = Paint.objects.all()
        serializer = PaintSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        paint_serializer = PaintSerializer(data=request.data)
        if paint_serializer.is_valid():
            paint_serializer.save()
            return Response(paint_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print("error", paint_serializer.errors)
            return Response(paint_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
