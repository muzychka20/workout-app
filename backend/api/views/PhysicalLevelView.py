
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers import PhysicalLevelSerializer
from rest_framework import status
from ..models import PhysicalLevel


class PhysicalLevelView(APIView):
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

    def get(self, request):
        levels = PhysicalLevel.objects.all()
        levels_serialized = PhysicalLevelSerializer(levels, many=True)
        return Response({
            'physical_levels': levels_serialized.data,
        }, status=status.HTTP_200_OK)
