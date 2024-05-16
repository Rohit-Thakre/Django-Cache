from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from base import models
from rest_framework import status

class Home(APIView):
    permission_classes =  [ IsAuthenticated]

    def initial(self, request, *args, **kwargs):
        return super().initial(request, *args, **kwargs)
    

    def get(self,request,*args, **kwargs): 
        students = models.Student.objects.all().values()
        return Response(data=students, status=status.HTTP_200_OK)
    
    def post(self,request,*args,**kwargs):
        return Response(data={}, status=status.HTTP_201_CREATED)
    
    def put(self,request,*args,**kwargs):
        return Response(data={}, status=status.HTTP_201_CREATED)

    def patch(self,request,  *args,**kwargs):
        return Response(data={}, status=status.HTTP_200_OK)