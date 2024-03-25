from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from resume_builder.resume.urls import router as router_resume
from resume_builder.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.registry.extend(router_resume.registry)

app_name = "api"
urlpatterns = router.urls
