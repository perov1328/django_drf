
from django.urls import path
from subscription.apps import SubscriptionConfig
from subscription.apiviews import SubscriptionCreateAPIView, SubscriptionDeleteAPIView


app_name = SubscriptionConfig.name


urlpatterns = [
    path('create/', SubscriptionCreateAPIView.as_view(), name='subscription_create'),
    path('delete/<int:pk>', SubscriptionDeleteAPIView.as_view(), name='subscription_delete'),
]