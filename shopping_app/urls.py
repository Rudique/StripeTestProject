from . import views
from django.urls import path


urlpatterns = [
    path('item/<int:id>/', views.ItemView.as_view(), name='item'),
    path('buy/<int:id>/', views.BuyView.as_view(), name='buy'),
    path('success/', views.SuccessView.as_view(), name='success'),
    path('cancel/', views.CancelView.as_view(), name='cancel')
]
