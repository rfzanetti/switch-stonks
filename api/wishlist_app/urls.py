from django.urls import path
from wishlist_app import views


urlpatterns = [
    path('wishlist/all', views.list_user_wishlist_games),
    path('wishlist/add', views.add_game_to_user_wishlist)
]
