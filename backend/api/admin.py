from django.contrib import admin
from .models import PhysicalLevel, Sex, BodyType, User, Article, TrainingType, Training, Goal

admin.site.register(PhysicalLevel)
admin.site.register(Sex)
admin.site.register(BodyType)
admin.site.register(User)
admin.site.register(Article)
admin.site.register(TrainingType)
admin.site.register(Training)
admin.site.register(Goal)
