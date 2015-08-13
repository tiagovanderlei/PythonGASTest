from django.contrib import admin

# Register your models here.
from .models import Question, Choice

#class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 1

# separa os campos em grupos (fieldsets)
class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
	(None,	{'fields':['question_text']}), 
	('Date information', {'fields':['pub_date'], 'classes':['collapse']})
	]
	inlines = [ChoiceInline]
	list_display = ('question_text', 'pub_date', 'was_published_recently')
	list_filter = ['pub_date']
	search_fields = ['question_text'] #['question_text','pub_date']
	list_per_page = 2

# altera ordem dos campos data de publicacao e texto da questao
#class QuestionAdmin(admin.ModelAdmin):
#	fields = ['pub_date', 'question_text']	


admin.site.register(Question, QuestionAdmin)
#admin.site.register(Choice)