from django.contrib import admin
from masterdata.models import Questiongroup,Question,Answer
# Register your models here.

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Questiongroup)