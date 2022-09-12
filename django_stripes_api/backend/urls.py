from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('item/<int:pk>/', views.item_detail),
    path('buy/<int:pk>/', views.create_checkout_session),
    path('config/', views.stripe_config),
    path('success/', views.SuccessView.as_view()),
    path('cancelled/', views.CancelledView.as_view()),
]