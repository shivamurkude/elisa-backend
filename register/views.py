from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Registration
from .helper import SendMail
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
from .serializers import RegistrationSerializer


import traceback

class RegistrationView(APIView):
    def post(self, request, format=None):
        try:
            data = request.data
            print(data)
            serializer = RegistrationSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                
                registration = serializer.data
                SendMail().send_email(sender_email=os.getenv("EMAIL"),receiver_emails=registration['email'], subject="Registration Successful", body="Thank you for registering with us. We will get back to you soon.",password=os.getenv('EMAIL_PASSWORD'))
                response_data = {'status': 'success', 'data': registration, 'status_code': status.HTTP_201_CREATED}
            else:
                response_data = {'status': 'error', 'errors': serializer.errors, 'status_code': status.HTTP_400_BAD_REQUEST}
        except Exception as e:
            traceback.print_exc()
            response_data = {'status': 'error', 'error_message': str(e), 'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR}
        
        return Response(response_data, status=response_data['status_code'])
    
    def get(self, request, format=None):
        try:
            registrations = Registration.objects.all()
            serializer = RegistrationSerializer(registrations, many=True)
            response_data = {'status': 'success', 'data': serializer.data, 'status_code': status.HTTP_200_OK}
        except Exception as e:
            traceback.print_exc()
            response_data = {'status': 'error', 'error_message': str(e), 'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR}
        
        return Response(response_data, status=response_data['status_code'])
