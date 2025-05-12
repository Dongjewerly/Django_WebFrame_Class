from django.shortcuts import render
# from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question

def index(request):
    question_list = Question.objects.order_by("-create_date") # question_list (변수) 생성, 오름차순으로 create_Date 작성 일시로 정리해라
    context = {'question_list':question_list} #context 변수의 question_list (속성)으로 지정, 생성
    return render(request,'pybo/question_list.html',context)
    #question_list를 pybo/question_list.html 템플릿을 적용하여 html 형태로 변환 후 반환

def detail(request, question_id):
    # question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)
    context = {'question':question}
    return render(request,'pybo/question_detail.html',context)
    # return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    question.answer_set.create(content=request.POST.get('content'),  create_date=timezone.now())
    return redirect('pybo:detail', question_id=question_id)
# Create your views here.

