Skip to content
Search or jump to…
Pull requests
Issues
Marketplace
Explore
 
@bywell-cloud 
codedoga
/
final-cloud-app-with-database
Public
Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
final-cloud-app-with-database/onlinecourse/admin.py /
@codedoga
codedoga lab3
Latest commit 02fbbc7 on Apr 30
 History
 1 contributor
46 lines (33 sloc)  1.13 KB

from django.contrib import admin
# <HINT> Import any new Models here
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission

# <HINT> Register QuestionInline and ChoiceInline classes here



class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 3 


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = [QuestionInline]

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['text']
    inlines = [ChoiceInline]

# <HINT> Register Question and Choice models here

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
