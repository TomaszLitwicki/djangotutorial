from django.contrib import admin
from .models import Question, Choice

# Register your models here.
class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields" : ["question_text"]}),
        ("Info o dacie", {"fields" : ["publicate_date"]})
        ]
    inlines = [ChoiceInLine]
    list_display = ["question_text", "publicate_date", "was_published_recently", "was_published_this_week", "in_the_future"]
    list_filter = ["publicate_date"]
    search_fields = ["question_text"]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)