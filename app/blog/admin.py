from django.contrib import admin
from .models import BaseModel
from django_summernote.admin import SummernoteModelAdmin

class BaseModelAdmin(SummernoteModelAdmin):
    summernote_fields = ('text',)

admin.site.register(BaseModel, BaseModelAdmin)