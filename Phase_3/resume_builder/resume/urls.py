from django.conf import settings
from rest_framework import routers

from .views import EducationViewSet, ExperienceViewSet, LanguageViewSet, ProjectViewSet, ResumeViewSet, SkillViewSet

router = routers.DefaultRouter() if settings.DEBUG else routers.SimpleRouter()

router.register("resumes", ResumeViewSet, basename="resume")
router.register("educations", EducationViewSet, basename="education")
router.register("experiences", ExperienceViewSet, basename="experience")
router.register("skills", SkillViewSet, basename="skill")
router.register("projects", ProjectViewSet, basename="project")
router.register("languages", LanguageViewSet, basename="language")
