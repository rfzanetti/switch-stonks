from django.conf.urls import url, include
from rest_framework import routers
from prices_app.views import CountryViewSet, GameViewSet, ListingViewSet


router = routers.DefaultRouter()
router.register(r'country', CountryViewSet)
router.register(r'game', GameViewSet)
router.register(r'listing', ListingViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
