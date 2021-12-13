from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from rest_framework import serializers, status
from .serializers import *
import pickle
import joblib
import pandas as pd


# Create your views here.
class LabDetails(APIView):
    serializer_class = LabSerializer
    def get(self,request):
        try:
            labs = Lab.objects.all()
            lab_data = LabSerializer(labs,many=True)
            return Response({'lab':lab_data.data})
        except Exception as e:
            print(e)
            return Response({'status': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class TransportDetails(APIView):
    serializer_class = TransportSerializer
    def get(self,request):
        try:
            transports = Transport.objects.all()
            transport_data = TransportSerializer(transports,many=True)
            return Response({'lab':transport_data.data})
        except Exception as e:
            print(e)
            return Response({'status': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class InsuaranceDetails(APIView):
    serializer_class = InsuaranceSerializer
    def get(self,request):
        try:
            insuarances = Insuarance.objects.all()
            insuarance_data = InsuaranceSerializer(insuarances,many=True)
            return Response({'lab':insuarance_data.data})
        except Exception as e:
            print(e)
            return Response({'status': str(e)}, status=status.HTTP_400_BAD_REQUEST)





class CropAnalysis(APIView):
    serializer_class = CropAnalysisSerializer
    def post(self,request):
        serializer = self.serializer_class(data = request.data)
        
        if serializer.is_valid():
             
                n= serializer.validated_data.get("nitrogen")
                p=serializer.validated_data.get("phosphorus")
                k=serializer.validated_data.get("potassium")
                temp=serializer.validated_data.get("temperature")
                
                humidity=serializer.validated_data.get("humidity")
                ph=serializer.validated_data.get("ph")
                rainfall=serializer.validated_data.get("rainfall")

                mj=joblib.load('crop_analysis_prediction')

                temp=[n,p,k,temp,humidity,ph,rainfall]

                
                
                predi=mj.predict([temp])
               
                return Response({'predict':predi}, status=status.HTTP_200_OK)
        else:
                
                return Response({"status": "failed", "message": "in else"}, status=status.HTTP_400_BAD_REQUEST)
        
        