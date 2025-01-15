from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import NoteViewSet

# Create the router and register the NoteViewSet
router = DefaultRouter()
router.register(r'notes', NoteViewSet)  # Include the viewset

urlpatterns = [
    path('landing', views.landing, name='landing_page'),
    path('', views.note, name="note"),
    path('api/', include(router.urls)),  # Include the API routes from the router
]