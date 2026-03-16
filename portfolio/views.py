from rest_framework import viewsets
from drf_spectacular.utils import extend_schema

from .models import About, Skill, Project, Experience, ContactMessage
from .permissions import IsAdminOrReadOnly
from .serializers import (
    AboutSerializer,
    SkillSerializer,
    ProjectSerializer,
    ExperienceSerializer,
    ContactMessageSerializer
)


@extend_schema(tags=["About"])
class AboutViewSet(viewsets.ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    permission_classes = [IsAdminOrReadOnly]


@extend_schema(tags=["Skill"])
class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [IsAdminOrReadOnly]


@extend_schema(tags=["Project"])
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAdminOrReadOnly]


@extend_schema(tags=["Experience"])
class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = [IsAdminOrReadOnly]


@extend_schema(tags=["Contact"])
class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
    permission_classes = [IsAdminOrReadOnly]
