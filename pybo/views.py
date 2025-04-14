from django.shortcuts import render
# from django.http import HttpResponse
from django.shortcuts import render
from .models import Question

def index(request):
    question_list = Question.objects.order_by("-create_date") #question_list (변수) 생성, 오름차순으로 create_Date 작성 일시로 정리해라
    context = {'question_list':question_list} #context 변수의 question_list (속성)으로 지정, 생성
    return render(request,'pybo/question_list.html',context)
    #question_list를 pybo/question_list.html 템플릿을 적용하여 html 형태로 변환 후 반환
    
    # return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")
# Create your views here.
