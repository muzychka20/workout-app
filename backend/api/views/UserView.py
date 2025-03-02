from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers import UserSerializer
from rest_framework import status
from ..models import User


class UserView(APIView):
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

    def post(self, request):        
        user = User.objects.get(id=request.data['user_id'])
        user_serialized = UserSerializer(user)
        return Response({
            'user': user_serialized.data,
        }, status=status.HTTP_200_OK)
