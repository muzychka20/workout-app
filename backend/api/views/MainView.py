from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


class MainView(APIView):
    permission_classes = [IsAuthenticated]
