from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers import TrainingTypeSerializer
from rest_framework import status
from ..models import TrainingType


class TrainingTypeView(APIView):
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

    def get(self, request):
        trainig_types = TrainingType.objects.all()
        trainig_types_serialized = TrainingTypeSerializer(
            trainig_types, many=True)
        return Response({
            'trainig_types': trainig_types_serialized.data,
        }, status=status.HTTP_200_OK)
