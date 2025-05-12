from django.urls import path

from . import views

app_name = 'pybo'

urlpatterns = [
    path('',views.index, name = 'index'),
    path('<int:question_id>/', views.detail, name = 'detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
] #id로 만든 url과 질문 상세 화면을 연결, 정수형:질문id/ 된 url을 views파일의 detail함수와 연결