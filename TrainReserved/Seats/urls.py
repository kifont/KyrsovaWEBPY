from django.urls import path
from .views import TrainListCreateView, TrainRetrieveUpdateDestroyView, SeatsListCreateView, SeatsRetrieveUpdateDestroyView
from .auth_view import CustomAuthToken, RegisterUserView


urlpatterns = [
    path('trains/', TrainListCreateView.as_view(), name='train-list-create'),
    path('trains/<int:pk>/', TrainRetrieveUpdateDestroyView.as_view(), name='train-retrieve-update-destroy'),
    path('seats/', SeatsListCreateView.as_view(), name='seats-list-create'),
    path('seats/<int:pk>/', SeatsRetrieveUpdateDestroyView.as_view(), name='seats-retrieve-update-destroy'),
    path('api-token-auth/', CustomAuthToken.as_view(), name='api_token_auth'),
    path('register/', RegisterUserView.as_view(), name='register'),
]