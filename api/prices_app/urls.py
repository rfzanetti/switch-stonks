from django.conf.urls import url, include
from rest_framework import routers
from prices_app.views import GameViewSet

router = routers.DefaultRouter()
router.register(r'game', GameViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
