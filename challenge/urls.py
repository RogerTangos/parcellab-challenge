from django.urls import path, include

from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'tracking', views.TrackingViewSet)
router.register(r'checkpoint', views.CheckpointViewSet)


app_name = 'challenge'
urlpatterns = [
    path('', views.get_email, name='email'),
    path('orders/', views.TrackingView.as_view(), name='index'),
    path('tracking/<int:tracking_number>/', views.DetailView.as_view(), name='detail'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
