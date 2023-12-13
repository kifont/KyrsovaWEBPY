from django.urls import path
from .views import TrainListCreateView, TrainRetrieveUpdateDestroyView, SeatsListCreateView, SeatsRetrieveUpdateDestroyView


urlpatterns = [
    path('trains/', TrainListCreateView.as_view(), name='train-list-create'),
    path('trains/<int:pk>/', TrainRetrieveUpdateDestroyView.as_view(), name='train-retrieve-update-destroy'),
    path('seats/', SeatsListCreateView.as_view(), name='seats-list-create'),
    path('seats/<int:pk>/', SeatsRetrieveUpdateDestroyView.as_view(), name='seats-retrieve-update-destroy'),
]