from django.contrib import admin
from .models import Question

#관리자 기능 https://docs.djangoproject.com/en/3.0/ref/contrib/admin/
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']


admin.site.register(Question, QuestionAdmin)