from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Question

class QuestionAdmin (admin.ModelAdmin):  #QuestionAdmin 클래스 생성(admin 모듈의 ModelAdmin 속성 가져옴)
    search_fields = ['subject'] #검색 필드 생성, subject로 검색

admin.site.register(Question, QuestionAdmin) #admin.site(admin화면)에 QuestionAdmin 클래스 추가