from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    AboutViewSet,
    SkillViewSet,
    ProjectViewSet,
    ExperienceViewSet,
    ContactMessageViewSet
)

router = DefaultRouter()
router.register(r'about', AboutViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'experiences', ExperienceViewSet)
router.register(r'contact', ContactMessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
