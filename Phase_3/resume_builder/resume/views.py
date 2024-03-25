from rest_framework import filters, viewsets

from .models import Education, Experience, Language, Project, Resume, Skill
from .serializers import (
    EducationSerializer,
    ExperienceSerializer,
    LanguageSerializer,
    ProjectSerializer,
    ResumeSerializer,
    SkillSerializer,
)

from django.contrib.auth import get_user_model

User = get_user_model()

# import render
from django.shortcuts import render

# template view
from django.views.generic import TemplateView


class BaseViewSet(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name"]
    ordering_fields = ["name"]


class ResumeViewSet(BaseViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer


class EducationViewSet(BaseViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer


class ExperienceViewSet(BaseViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer


class SkillViewSet(BaseViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class ProjectViewSet(BaseViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class LanguageViewSet(BaseViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


from .forms import ResumeForm

class ResumeTemplate(TemplateView):
    template_name = "resume.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = ResumeForm()
        return context