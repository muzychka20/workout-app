from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers import SexTypeSerializer
from rest_framework import status
from ..models import Sex


class SexTypeView(APIView):
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

    def get(self, request):
        sex = Sex.objects.all()
        sex_serialized = SexTypeSerializer(sex, many=True)
        return Response({
            'sex_types': sex_serialized.data,
        }, status=status.HTTP_200_OK)
