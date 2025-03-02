from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers import GoalSerializer
from rest_framework import status
from ..models import Goal


class GoalView(APIView):
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

    def get(self, request):
        goals = Goal.objects.all()
        goals_serialized = GoalSerializer(goals, many=True)
        return Response({
            'goals': goals_serialized.data,
        }, status=status.HTTP_200_OK)
