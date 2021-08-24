from .models import Event
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import EventSerializer


class EventView(APIView):
    def post(self, request):
        query = Event.objects.all()
        serializer = EventSerializer(query)
        return Response(serializer.data)
