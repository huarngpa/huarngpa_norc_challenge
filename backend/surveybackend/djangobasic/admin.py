from django.contrib import admin

from .models import Choice, Question, Response, Survey

# Register your models here.


admin.site.register(Choice)
admin.site.register(Question)
admin.site.register(Response)
admin.site.register(Survey)
