from django.contrib import admin

from .models import Choice, Question, Response

# Register your models here.


admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Response)
