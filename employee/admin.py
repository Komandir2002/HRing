from django.contrib import admin
from .models import Post,Department,Employee
# Register your models here.
admin.site.register(Post)
admin.site.register(Department)
admin.site.register(Employee)