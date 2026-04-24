from django.contrib import admin
from .models import Course

admin.site.register(Course)
<<<<<<< HEAD

# Register your models here.
=======
# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display=('Course_name','price','status')
>>>>>>> 7f36e1d (added files)
