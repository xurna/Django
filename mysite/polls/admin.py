from django.contrib import admin

# Register your models here.
from .models import Choice,Question

# Choice对象在Question的管理界面中编辑。默认提供足够3个Choice的空间。
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

# 默认每页显示100条记录
class QuestionAdmin(admin.ModelAdmin):
	"""docstring for QuestionAdmin"""
	# fields = ['pub_date', 'question_text']
	fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
	list_display = ('question_text', 'pub_date','was_published_recently')
	inlines = [ChoiceInline]
	# 通过pub_date字段对变更列表进行过滤
	list_filter = ['pub_date']
	# 搜索功能
	search_fields = ['question_text']

    


admin.site.register(Question,QuestionAdmin)
# admin.site.register(Choice)
