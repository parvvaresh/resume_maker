from django.forms import ModelForm

from .models import Education, Experience, Language, Project, Resume, Skill


class ResumeForm(ModelForm):
    class Meta:
        model = Resume
        fields = '__all__'

class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = '__all__'

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = '__all__'

class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'

class LanguageForm(ModelForm):
    class Meta:
        model = Language
        fields = '__all__'

class ResumeForm(ModelForm):
    class Meta:
        model = Resume
        fields = '__all__'

