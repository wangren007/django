from django.contrib import admin

# Register your models here.
from .models import Grades,Students
#注册
class StudentsInfo(admin.TabularInline):#StackedInline
	model = Students
	extra = 2
class GradesAdmin(admin.ModelAdmin):
	inlines = [StudentsInfo]
	#自定义列表页属性
	list_display=["id","gname","gdate","ggirlnum","gboynum","isDelete"] #显示字段的属性名和字段
	list_filter=["gname"]   #显示过滤器过滤字段
	search_fields=["gname"] #按字段名搜索
	list_per_page=5 #每5条分页
	#添加、修改页属性
	# fields=["ggirlnum","gboynum","gname","gdate","isDelete"]   #调整增加页面属性的先后顺序
	fieldsets=[
		("num",{"fields":["ggirlnum","gboynum"]}),
		("base",{"fields":["gname","gdate","isDelete"]}),
	]    #给属性分组,注意field和fieldsets不能同时使用
admin.site.register(Grades,GradesAdmin)

@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
	def gender(self):
		if self.sgender:
			return "男"
		else:
			return "女"
	gender.short_description = "性别"
	# 自定义列表页属性
	list_display = ["id", "sname",gender, "sage", "scontend", "isDelete","sgrade"]  # 显示字段的属性名和字段
	list_filter = ["sname"]  # 显示过滤器过滤字段
	search_fields = ["sname"]  # 按字段名搜索
	list_per_page = 5  # 每5条分页
	# 添加、修改页属性
	# fields=["sname", "sgender", "sage", "scontend", "isDelete","sgrade"]   #调整增加页面属性的先后顺序
	fieldsets = [
		("num", {"fields": ["sgrade"]}),
		("base", {"fields": ["sname", "sgender","sage","scontend","isDelete"]}),
	]  # 给属性分组,注意field和fieldsets不能同时使用
	actions_on_bottom = True  #执行动作的位置
	actions_on_top = False  #执行动作的位置
# admin.site.register(Students,StudentsAdmin)

