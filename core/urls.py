from django.contrib import admin  # type: ignore[reportMissingImports]
from django.urls import path, include  # type: ignore[reportMissingImports]
from rest_framework import routers  # type: ignore[reportMissingImports]
from importlib import import_module

jwt_views = import_module('rest_framework_simplejwt.views')
TokenObtainPairView = jwt_views.TokenObtainPairView
TokenRefreshView = jwt_views.TokenRefreshView
from todo import views

router = routers.DefaultRouter()
router.register(r'todos', views.TodoView, 'todo')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]