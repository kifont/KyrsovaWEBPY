from rest_framework import generics
from .models import Train, Seats
from .serializers import TrainSerializer, SeatsSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class TrainListCreateView(generics.ListCreateAPIView):
    queryset = Train.objects.all()
    serializer_class = TrainSerializer

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
                # Додайте інші поля, які очікує ваша модель
            },
            required=['field1', 'field2'],
        ),
        responses={201: openapi.Response("Новий ресурс", TrainSerializer)},
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class TrainRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
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

class SeatsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
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
