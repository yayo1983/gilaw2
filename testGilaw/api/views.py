from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import NotificationSerializer
from django.views.decorators.csrf import csrf_exempt
from .models import Notification

class NotificationView(APIView):

    @api_view(('GET',))
    @csrf_exempt
    def getLogs(request):
        try:
            notifications = Notification.objects.all().order_by('created_at')
            if notifications and len(notifications) > 0:
                serializer = NotificationSerializer(notifications, many=True)
                return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
            else:
                Response({"status": "success", "data": []}, status=status.HTTP_200_OK)
        except Notification.DoesNotExist:
            Response({"status": "success", "data": []}, status=status.HTTP_200_OK)
        except:
            return Response({"status": "fail", "message": 'Error in the request'}, status=status.HTTP_400_BAD_REQUEST)

    
    @api_view(('POST',))
    @csrf_exempt
    # pass de any user: user123qwe
    def submissionMessage(request):
        if (request.POST.get('message', False) and request.POST.get('category', False)):
                serializer = NotificationSerializer()
                result = serializer.save_notification(request.POST.get('message', False), request.POST.get('category', False))
                if result:
                    return Response({"status": "success"}, status=status.HTTP_201_CREATED)
                return Response({"status": "fail", "message": 'Error saving the notification'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"status": "fail", "message": request.POST.get('message')}, status=status.HTTP_406_NOT_ACCEPTABLE)
