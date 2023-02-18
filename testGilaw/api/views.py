from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, generics
from .models import Notification, SMSNotification
from .serializers import NotificationSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, renderer_classes

class NotificationView(APIView):
    
    @api_view(('POST',))
    @csrf_exempt
    def getLogs(request):
        try:
            notifications = Notification.objects.all()
            if notifications:
                serializer = NotificationSerializer(notifications, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                Response(status=status.HTTP_404_NOT_FOUND)
        except:
            return Response({"status": "fail", "message": 'Error in the request'}, status=status.HTTP_400_BAD_REQUEST)
    
    @api_view(('POST',))
    @csrf_exempt   
    def submissionMessage(self, request):
        serializer = self.serializer_class(data=request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "success", "notification": serializer.data}, status=status.HTTP_201_CREATED)
            else:
                return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"status": "fail", "message": 'Error in the request'}, status=status.HTTP_400_BAD_REQUEST)


        
