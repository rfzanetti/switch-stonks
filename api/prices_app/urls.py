from django.urls import path
from prices_app import views


urlpatterns = [
    path('games', views.list_game_by_title),
    path('history/<int:pk>/', views.game_listing_history),
]
