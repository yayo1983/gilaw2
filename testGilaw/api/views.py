from rest_framework.response import Response
from rest_framework import status, generics


class NotificationView(generics.GenericAPIView):
    def get(self, request):
        return Response({"status": "success"}, status=status.HTTP_201_CREATED)
    

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "note": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
