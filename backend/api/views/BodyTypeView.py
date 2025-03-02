from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers import BodyTypeSerializer
from rest_framework import status
from ..models import BodyType


class BodyTypeView(APIView):
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

    def get(self, request):
        goals = BodyType.objects.all()
        goals_serialized = BodyTypeSerializer(goals, many=True)
        return Response({
            'body_types': goals_serialized.data,
        }, status=status.HTTP_200_OK)
