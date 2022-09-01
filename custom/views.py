from django.shortcuts import render
from .models import Company
from .serializers import CompanySer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class Companyview(APIView):
    def get(self,r):
        cdata = Company.objects.all()
        serdata = CompanySer(cdata,many=True)
        return Response(serdata.data)

    def post(self,r):
        serobj = CompanySer(data=r.data)
        if serobj.is_valid():
            serobj.save()
            return Response(serobj.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serobj.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,r,x):
        cdata = Company.objects.get(id=x)
        serdata = CompanySer(cdata,data=r.data)
        if serdata.is_valid():
            serdata.save()
            return Response(serdata.data,status=status.HTTP_201_CREATED)
        return Response(serdata.erros,status=status.HTTP_200_OK)

    def delete(self,r,x):
        cdata = Company.objects.get(id=x)
        cdata.delete()
        return Response(status=status.HTTP_200_OK)


    def hy(self):
        return Response(status=status.HTTP_200_OK)

    def hello(self):
        return Response(status=status.HTTP_200_OK)



