from django.urls import path, include
from rest_framework.routers import DefaultRouter
from userreg.views import UserView


router_v1 = DefaultRouter()
router_v1.register(r'users', UserView)

urlpatterns = [
    path('', include(router_v1.urls)),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
