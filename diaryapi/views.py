from django.shortcuts import render
from rest_framework import status,serializers
from rest_framework.response import Response    
from rest_framework import APIView    
from .models import Diary
from .serializers import DiarySerializer 


# Create your views here.

class Diaryview(APIView):
    def get(self, request):
        try:
            diary = Diary.objects.all()
            serializer = DiarySerializer(diary, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def post(self, request):
        try:
            serializer = DiarySerializer(data = request.data)
            if serializer.is_valid(): 
                serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class Diarydetailview(APIView):
    
    def get(self, request, id):
        try:
            diary = Diary.objects.get(id=id)
            serializer = DiarySerializer(diary) 
            return Response(serializer.data, status=status.HTTP_200_OK)  
        except Diary.DoesNotExist:
            return Response({"message": "Diary not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, id):
        try:
            diary = Diary.objects.get(id=id)
            serializer = DiarySerializer(diary, data=request.data, partial=True)  
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)  
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Diary.DoesNotExist:
            return Response({"message": "Diary not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
