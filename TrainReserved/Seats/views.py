from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Train, Seats
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import TrainSerializer, SeatsSerializer, AdminLoginSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.permissions import IsAuthenticated

class TrainListCreateView(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Train.objects.all()
    serializer_class = TrainSerializer

class UpdateTrainDataView(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def put(self, request, pk, format=None):
        """
        Оновлення елемента в базі даних за його первинним ключем (pk).
        """
        try:
            instance = Train.objects.get(pk=pk)
        except Train.DoesNotExist:
            return Response({"error": "Елемент не знайдено"}, status=status.HTTP_404_NOT_FOUND)

        serializer = TrainSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Отримати список всіх ресурсів",
        responses={200: openapi.Response("Список ресурсів", TrainSerializer(many=True))},
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Створити новий ресурс",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'field1': openapi.Schema(type=openapi.TYPE_STRING),
                'field2': openapi.Schema(type=openapi.TYPE_STRING),

            },
            required=['field1', 'field2'],
        ),
        responses={201: openapi.Response("Новий ресурс", TrainSerializer)},
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class TrainRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Train.objects.all()
    serializer_class = TrainSerializer

    @swagger_auto_schema(
        operation_description="Отримати ресурс за id",
        responses={200: openapi.Response("Ресурс", TrainSerializer)},
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Змінити ресурс за id",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'train_number': openapi.Schema(type=openapi.TYPE_STRING),
                'departure_station': openapi.Schema(type=openapi.TYPE_STRING),
                'arrival_station': openapi.Schema(type=openapi.TYPE_STRING),
                'departure_time': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME),
                'arrival_time': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME),
                'total_seats': openapi.Schema(type=openapi.TYPE_INTEGER),
            },
            required=['train_number', 'departure_station', 'arrival_station', 'departure_time', 'arrival_time',
                      'total_seats'],
        ),
        responses={200: openapi.Response("Змінений ресурс", TrainSerializer)},
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Видалити ресурс за id",
        responses={204: openapi.Response("Ресурс видалено")},
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
class SeatsListCreateView(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Seats.objects.all()
    serializer_class = SeatsSerializer

    @swagger_auto_schema(
        operation_description="Отримати список всіх ресурсів",
        responses={200: openapi.Response("Список ресурсів", SeatsSerializer(many=True))},
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Створити новий ресурс",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'train': openapi.Schema(type=openapi.TYPE_INTEGER),
                'seat_number': openapi.Schema(type=openapi.TYPE_STRING),
                'is_booked': openapi.Schema(type=openapi.TYPE_BOOLEAN),
            },
            required=['train', 'seat_number', 'is_booked'],
        ),
        responses={201: openapi.Response("Новий ресурс", SeatsSerializer)},
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class UpdateSeatsDataView(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def put(self, request, pk, format=None):
        """
        Оновлення елемента в базі даних за його первинним ключем (pk).
        """
        try:
            instance = Seats.objects.get(pk=pk)
        except Seats.DoesNotExist:
            return Response({"error": "Елемент не знайдено"}, status=status.HTTP_404_NOT_FOUND)

        serializer = SeatsSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SeatsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Seats.objects.all()
    serializer_class = SeatsSerializer

    @swagger_auto_schema(
        operation_description="Отримати ресурс за id",
        responses={200: openapi.Response("Ресурс", SeatsSerializer)},
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Змінити ресурс за id",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'train': openapi.Schema(type=openapi.TYPE_INTEGER),
                'seat_number': openapi.Schema(type=openapi.TYPE_STRING),
                'is_booked': openapi.Schema(type=openapi.TYPE_BOOLEAN),
            },
            required=['train', 'seat_number', 'is_booked'],
        ),
        responses={200: openapi.Response("Змінений ресурс", SeatsSerializer)},
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Видалити ресурс за id",
        responses={204: openapi.Response("Ресурс видалено")},
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


