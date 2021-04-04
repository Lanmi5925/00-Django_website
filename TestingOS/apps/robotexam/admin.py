from django.contrib import admin
from apps.robotexam.models import QuestionPaper, RightOrWrong, SingleSel, MultiSel, Student, Teacher, Grade
# Register your models here.


class QuestionPaperAdmin(admin.ModelAdmin):
    pass


class RightOrWrongAdmin(admin.ModelAdmin):
    pass


class SingleSelAdmin(admin.ModelAdmin):
    pass


class MultiSelAdmin(admin.ModelAdmin):
    pass


class StudentAdmin(admin.ModelAdmin):
    pass


class TeacherAdmin(admin.ModelAdmin):
    pass


class GradeAdmin(admin.ModelAdmin):
    pass


admin.site.register(QuestionPaper, QuestionPaperAdmin)
admin.site.register(RightOrWrong, RightOrWrongAdmin)
admin.site.register(SingleSel, SingleSelAdmin)
admin.site.register(MultiSel, MultiSelAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Grade, GradeAdmin)