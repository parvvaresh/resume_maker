from django.contrib import admin

from .models import Education, Experience, Language, Project, Resume, Skill

admin.site.register(Resume)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Language)
