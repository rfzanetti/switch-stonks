from django.urls import path
from wishlist_app import views


urlpatterns = [
    path('wishlist/', views.WishlistView.as_view()),
    path('wishlist/<int:pk>/', views.WishlistDetailView.as_view()),
]
